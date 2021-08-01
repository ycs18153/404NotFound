from fastapi import FastAPI, HTTPException
from fastapi.params import Body
from fastapi.responses import HTMLResponse
import json
from fastapi.middleware.cors import CORSMiddleware
from motor.motor_asyncio import AsyncIOMotorClient

from model import Todo, UpdateTodo
from controller import fetch_user_todo, fetch_all_todos, create_todo, update_todo, remove_todo
from config import settings


app = FastAPI()


@app.on_event("startup")
async def startup_db_client():
    app.mongodb_client = AsyncIOMotorClient(settings.DB_URL)
    app.mongodb = app.mongodb_client[settings.DB_NAME]


@app.on_event("shutdown")
async def shutdown_db_client():
    app.mongodb_client.close()

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/", response_class=HTMLResponse)
async def root_page():
    return """<html>
        <head>
            <title>TODO List</title>
        </head>
        <body>
            <h1>Hello TODO List</h1>
        </body>
    </html>"""


@app.get("/api/todo/")
async def get_todo():
    response = await fetch_all_todos()
    return response


# @app.get("/api/todo/{todo_name}", response_model=Todo)
# async def get_todo_by_todo_name(todo_name):
#     response = await fetch_user_todo(todo_name)
#     if response:
#         return response
#     raise HTTPException(404, f"There is no todo with the title {todo_name}")

@app.get("/api/todo/{user_id}", response_model=Todo)
async def get_todo_by_user_id(user_id):
    response = await fetch_user_todo(user_id)
    if response:
        return response
    raise HTTPException(404, f"This user doesn't have any Todo")


@app.post("/api/todo/", response_model=Todo)
async def post_todo(todo: Todo):
    print(f'post body: {todo.dict()}')
    response = await create_todo(todo.dict())
    if response:
        return response
    raise HTTPException(400, "Please check with server or post body.")


@app.put("/api/todo/{todo_name}", response_model=Todo)
async def put_todo(todo_name: str, payload: UpdateTodo = Body(...)):
    payload = {k: v for k, v in payload.dict().items() if v is not None}
    response = await update_todo(todo_name, payload)
    if response:
        return response
    raise HTTPException(404, f"There is no todo with the title {todo_name}")


@app.delete("/api/todo/{todo_name}")
async def delete_todo(todo_name):
    response = await remove_todo(todo_name)
    if response:
        return "Successfully deleted todo"
    raise HTTPException(404, f"There is no todo with the title {todo_name}")
