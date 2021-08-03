import motor.motor_asyncio
from model import Todo
from fastapi.encoders import jsonable_encoder
import pymongo


# client = motor.motor_asyncio.AsyncIOMotorClient(
#     'mongodb+srv://admin:admin@cluster0.gitsk.mongodb.net/myFirstDatabase?retryWrites=true')
client = pymongo.MongoClient(
    'mongodb+srv://admin:admin@cluster0.gitsk.mongodb.net/myFirstDatabase?retryWrites=true')


database = client.myFirstDatabase
# TodoList

todo_collection = database.todo
myeHR_collection = database.myehr
employee_id_collection = database.employee_id_mapping


async def create_emplyee_id(employee_id):
    document = employee_id
    result = employee_id_collection.insert_one(document)
    return document


async def fetch_user_todo_by_date(todo_name):
    document = todo_collection.find_one({"todo_name": todo_name})
    return document


def mapping_employee_id(user_id):
    id_info = employee_id_collection.find_one({"user_id": user_id})
    employee_id = id_info.get('employee_id')
    print(f'Query employee id: {employee_id}')

    return employee_id

# [BUG] 需按照時間排序，並過濾掉 todo_completed = true 的 record


def fetch_all_todos(user_id):

    employee_id = mapping_employee_id(user_id)
    print(employee_id)
    document = todo_collection.find(
        {"employee_id": employee_id}, {'_id': False})

    return document


async def create_todo(todo, user_id):
    document = todo
    employeeId = employee_id_collection.find_one({"user_id": user_id})
    document.employee_id = employeeId.get("employee_id") 
    result = todo_collection.insert_one(document)
    return document


async def update_todo(user_id, todo_id, payload):
    # todo_name = todo_name.replace('%20', ' ')

    employee_id = mapping_employee_id(user_id)

    todo_collection.update_one(
        {"employee_id": employee_id, "todo_id": todo_id}, {"$set": payload})
    document = todo_collection.find_one(
        {"employee_id": employee_id}, {'todo_id': False})
    return document


async def remove_todo(user_id, todo_name):
    todo_name = todo_name.replace('%20', ' ')

    employee_id = mapping_employee_id(user_id)

    todo_collection.delete_one(
        {"employee_id": employee_id, "todo_name": todo_name})
    return True


# region @myeHR API
async def get_tsmc_url():
    document = myeHR_collection.find({'_id': False})
    return document

# for Todolist Web


def fetch_all_todos_by_employee_id(employee_id):
    document = todo_collection.find(
        {"employee_id": employee_id}, {'_id': False})
    return document
