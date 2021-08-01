import motor.motor_asyncio
from model import Todo
from fastapi.encoders import jsonable_encoder
import pymongo


# client = motor.motor_asyncio.AsyncIOMotorClient(
#     'mongodb+srv://admin:admin@cluster0.gitsk.mongodb.net/myFirstDatabase?retryWrites=true')
client = pymongo.MongoClient('mongodb+srv://admin:admin@cluster0.gitsk.mongodb.net/myFirstDatabase?retryWrites=true')


database = client.myFirstDatabase
# TodoList

todo_collection = database.todo
myeHR_collection = database.myehr
employee_id_collection = database.employee_id_mapping

# [BUG] Description: Needs to return all of todos that the date is matched

async def create_emplyee_id(employee_id):
    document = employee_id
    result = employee_id_collection.insert_one(document)
    return document


async def fetch_user_todo_by_date(todo_name):
    document = todo_collection.find_one({"todo_name": todo_name})
    return document


# [BUG]: Needs to return all of todos that the person whose employee_id is matched
def mapping_employee_id(user_id):

    id_info = employee_id_collection.find_one({"user_id": user_id})
    employee_id = id_info.get('employee_id')
    print(f'Query employee id: {employee_id}')

    return employee_id

def fetch_all_todos(user_id):

    employee_id = mapping_employee_id(user_id)
    document = todo_collection.find({"employee_id": employee_id}, {'_id': False})

    return document


async def create_todo(todo):
    document = todo
    result = todo_collection.insert_one(document)
    return document


async def update_todo(employee_id, todo_name, payload):
    todo_name = todo_name.replace('%20', ' ')
    todo_collection.update_one({"employee_id": employee_id, "todo_name": todo_name}, {"$set": payload})
    document = await todo_collection.find_one({"todo_name": todo_name})
    return document


async def remove_todo(employee_id, todo_name):
    todo_name = todo_name.replace('%20', ' ')
    todo_collection.delete_one({"employee_id": employee_id, "todo_name": todo_name})
    return True


# region @myeHR API
async def get_tsmc_url(web_name):
    document = myeHR_collection.find_one({"name": web_name})
    return document
