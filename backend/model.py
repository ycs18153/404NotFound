from pydantic import BaseModel
import datetime
from typing import Optional


class Todo(BaseModel):
    todo_name: str
    todo_date: str
    todo_contents: str
    todo_update_date: str
    todo_completed: bool = False
    employee_id: str

class EmployeeId(BaseModel):
    employee_id: str
    user_id: str


class UpdateTodo(BaseModel):
    todo_name: Optional[str]
    todo_date: Optional[str]
    todo_contents: Optional[str]
    todo_update_date: Optional[str]
    todo_completed: Optional[bool]
    employee_id: Optional[str]
    line_user_id: Optional[str]
    teams_user_id: Optional[str]


class web(BaseModel):
    name: str
    url: str

