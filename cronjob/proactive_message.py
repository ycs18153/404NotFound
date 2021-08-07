import pymongo
from datetime import datetime, timedelta
import requests
import sys


args = sys.argv[1:]


client = pymongo.MongoClient(
    'mongodb+srv://admin:admin@cluster0.gitsk.mongodb.net/myFirstDatabase?retryWrites=true')


database = client.myFirstDatabase
# TodoList

todo_collection = database.todo
employee_id_collection = database.employee_id_mapping


start = datetime.now()
end = start + timedelta(minutes = 60)

url = 'https://azure-bot-framework.herokuapp.com/api/v1/cron-messages'


for todo_doc in todo_collection.find({'todo_date': {'$gte': start, '$lt': end}}, {'_id': False}):
    id_doc = employee_id_collection.find({'employee_id': todo_doc['employee_id']}, {'_id': False})
    todo_doc['todo_date'] = todo_doc['todo_date'].strftime('%Y-%m-%d %H:%M')
    id_doc = list({v['user_id']:v for v in id_doc}.values())
    for id in id_doc:

        if 'tenant_id' not in id.keys():
            continue

        try:
            body = {
                'tenant_id': id['tenant_id'],
                'user_id': id['user_id'],
                'todo': todo_doc
            }
            if args[0] == 'prod':
                r = requests.post(url=url, json=body)
                print(todo_doc['employee_id'])
                print("success")
                r.close()
            else:
                print(body)
        except:
            print('[ERROR]')
            print(body)