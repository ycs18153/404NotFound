from model import Web
from fastapi import FastAPI, HTTPException
from fastapi.params import Body
from fastapi.responses import HTMLResponse
import json
from fastapi.middleware.cors import CORSMiddleware
from motor.motor_asyncio import AsyncIOMotorClient

from model import Todo, UpdateTodo, EmployeeId, Web
from controller import fetch_user_todo_by_date, fetch_all_todos, create_todo, update_todo, remove_todo
from controller import create_emplyee_id, fetch_userID_with_employeeID,create_myehr
from controller import get_tsmc_url
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
    "https://tsmc-todolist.de.r.appspot.com",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# region @To-do list CRUD operations


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


@app.post("/api/employee-id/", response_model=EmployeeId)
async def post_todo(employee_id: EmployeeId):
    print(f'post body: {employee_id.dict()}')
    response = await create_emplyee_id(employee_id.dict())
    if response:
        return response
    raise HTTPException(400, "Please check with server or post body.")

# Get all todos by employee ID


@app.get("/api/todo/{user_id}")
def get_todo_by_employee_id(user_id):
    response = fetch_all_todos(user_id)

    resp = []
    for i in response:
        resp.append(i)

    if resp:
        return resp
    raise HTTPException(
        404, f"There is no employee with the ID: {user_id}")

# # Get all todos by date
# @app.get("/api/todo/{employee_id}/{date}", response_model=Todo)
# async def get_todo_by_employee_id_and_date(todo_name):
#     response = await fetch_user_todo_by_date(todo_name)
#     if response:
#         return response
#     raise HTTPException(404, f"There is no todo with the title {todo_name}")


@app.post("/api/todo/{user_id}", response_model=Todo)
async def post_todo(user_id: str, todo: Todo):
    print(f'post body: {todo.dict()}')
    response = await create_todo(user_id, todo.dict())
    if response:
        return response
    raise HTTPException(400, "Please check with server or post body.")


@app.put("/api/todo/{user_id}/{todo_id}", response_model=Todo)
async def put_todo(user_id: str, todo_id: str, payload: UpdateTodo = Body(...)):
    payload = {k: v for k, v in payload.dict().items() if v is not None}
    response = await update_todo(user_id, todo_id, payload)
    if response:
        print(f'response: {response}')
        return response
    raise HTTPException(404, f"There is no todo with the title {todo_id}")


@app.delete("/api/todo/{user_id}/{todo_id}")
async def delete_todo(user_id, todo_id):
    response = await remove_todo(user_id, todo_id)
    if response:
        return "Successfully deleted todo"
    raise HTTPException(404, f"There is no todo with the id: {todo_id}")
# endregion

# region @myeHR api


@app.get("/api/myehr")
async def get_tsmc_website():
    response = await get_tsmc_url()
    resp = []
    for i in response:
        resp.append(i)

    if resp:
        return resp
    raise HTTPException(404, f"There is no website!")

# For Todolist Web


@app.get("/api/todo/web/{employee_id}")
def fetch_all_todo_for_web(employee_id):
    response = fetch_userID_with_employeeID(employee_id)
    if response:
        res = response["user_id"]
        return res
    raise HTTPException(404, f"There is no employee id with {employee_id}")

@app.post("/api/myehr/", response_model=Web)
async def new_myehr(web:Web):
    print(f'post body: {web.dict()}')
    response = await create_myehr(web.dict())
    if response:
        return response
    raise HTTPException(400, "Please check with server or post body.")
