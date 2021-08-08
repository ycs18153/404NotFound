import pymongo
from datetime import datetime, timedelta
import requests
import sys


client = pymongo.MongoClient(
    'mongodb+srv://admin:admin@cluster0.gitsk.mongodb.net/myFirstDatabase?retryWrites=true')


database = client.myFirstDatabase
# TodoList

todo_collection = database.todo
employee_id_collection = database.employee_id_mapping


start = datetime.now()
end = start + timedelta(minutes = 60)
print(f'start: {start}')
print(f'end: {end}')

url = 'https://azure-bot-framework.herokuapp.com/api/v1/cron-messages'


for todo_doc in todo_collection.find({'todo_date': {'$gte': start, '$lt': end}}, {'_id': False}c):
    id_doc = employee_id_collection.find({'employee_id': todo_doc['employee_id']}, {'_id': False})
    todo_doc['todo_date'] = todo_doc['todo_date'].strftime('%Y-%m-%d %H:%M')
    id_doc = list({v['user_id']:v for v in id_doc}.values())

    if len(id_doc) == 0:
        break

    for doc in id_doc:

        if 'tenant_id' not in doc.keys():
            continue

        try:
            body = {
                'tenant_id': doc['tenant_id'],
                'user_id': doc['user_id'],
                'todo': todo_doc
            }
            r = requests.post(url=url, json=body)
            print(body)
            print("success")

        except:
            print('[ERROR]')
            print(body)

