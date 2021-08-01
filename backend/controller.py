import motor.motor_asyncio
from model import Todo
from fastapi.encoders import jsonable_encoder

client = motor.motor_asyncio.AsyncIOMotorClient(
    'mongodb+srv://admin:admin@cluster0.gitsk.mongodb.net/myFirstDatabase?retryWrites=true')

database = client.myFirstDatabase
# TodoList

todo_collection = database.todo
myeHR_collection = database.myehr

# [BUG] Description: Needs to return all of todos that the date is matched


async def fetch_user_todo_by_date(todo_name):
    document = await todo_collection.find_one({"todo_name": todo_name})
    return document


# [BUG]: Needs to return all of todos that the person whose employee_id is matched
async def fetch_all_todos(employee_id):
    document = await todo_collection.find_one({"employee_id": employee_id})
    return document


async def create_todo(todo):
    document = todo
    result = await todo_collection.insert_one(document)
    return document


async def update_todo(employee_id, todo_name, payload):
    await todo_collection.update_one({"employee_id": employee_id, "todo_name": todo_name}, {"$set": payload})
    document = await todo_collection.find_one({"todo_name": todo_name})
    return document


async def remove_todo(employee_id, todo_name):
    await todo_collection.delete_one({"employee_id": employee_id, "todo_name": todo_name})
    return True


# region @myeHR API
async def get_tsmc_url(web_name):
    document = await myeHR_collection.find_one({"name": web_name})
    return document
