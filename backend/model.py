from pydantic import BaseModel
import datetime
from typing import Optional

class Todo(BaseModel):
    user_id: str
    todo_name: str
    todo_date: str
    todo_contents: str
    todo_update_date: str
    todo_completed: bool = False

class UpdateTodo(BaseModel):
    user_id: Optional[str]
    todo_name: Optional[str]
    todo_date: Optional[str]
    todo_contents: Optional[str]
    todo_update_date: Optional[str]
    todo_completed: Optional[bool]