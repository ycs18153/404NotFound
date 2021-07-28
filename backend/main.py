from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse

from fastapi.middleware.cors import CORSMiddleware
from motor.motor_asyncio import AsyncIOMotorClient

from model import Todo
from controller import fetch_one_todo, fetch_all_todos, create_todo, update_todo, remove_todo
from config import settings
from todo.routers import router as todo_router



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

app.include_router(todo_router, tags=["todo"], prefix="/api")


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


@app.get("/api/todo")
async def get_todo():
    response = await fetch_all_todos()
    return response


@app.get("/api/todo/{title}", response_model=Todo)
async def get_todo_by_title(title):
    response = await fetch_one_todo(title)
    if response:
        return response
    raise HTTPException(404, f"There is no todo with the title {title}")


@app.post("/api/todo/", response_model=Todo)
async def post_todo(todo: Todo):
    print(f'post body: {todo.dict()}')
    response = await create_todo(todo.dict())
    if response:
        return response
    raise HTTPException(400, "Please check with server or post body.")


@app.put("/api/todo/{title}/", response_model=Todo)
async def put_todo(title: str, desc: str):
    response = await update_todo(title, desc)
    if response:
        return response
    raise HTTPException(404, f"There is no todo with the title {title}")


@app.delete("/api/todo/{todo_name}")
async def delete_todo(todo_name):
    response = await remove_todo(todo_name)
    if response:
        return "Successfully deleted todo"
    raise HTTPException(404, f"There is no todo with the title {todo_name}")
