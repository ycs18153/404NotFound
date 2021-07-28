from pydantic import BaseModel
import datetime


class Todo(BaseModel):
    user_id: str
    todo_name: str
    todo_date: str
    todo_contents: str
    todo_update_date: str
    todo_completed: bool = False