# ToDoList_FARM-stack
[Teams Bot Link](https://teams.microsoft.com/l/chat/0/0?users=28:30eba4f2-6e15-458b-9fdf-f8bbf25efb4f)
## MongoDB
Start local mongodb
```docker
cd mongodb
docker compose up -d
```
![Image of mongo start](./img/mongo_docker.PNG)
create Databases & todo collection
![Image of mongo start](./img/mongo_create_db.PNG)


## FastAPI
```python
pip install -r requirements.txt
```

Start main.py
```python
uvicorn main:app --reload
```
After start it:
![Image of FastAPI start](./img/start.PNG)

### FastAPI
Auto gen API documents
![Image of FastAPI docs](./img/auto_gen_docs.PNG)

Post Result
![Image of mongo get](./img/mongo_get.PNG)
