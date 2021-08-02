from pydantic import BaseModel
import datetime
from typing import Optional
from uuid import UUID, uuid4


class Todo(BaseModel):
    todo_id: UUID = uuid4()
    todo_name: str
    todo_date: str
    todo_contents: Optional[str]
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


class Web(BaseModel):
    name: str
    url: str
    category: str = "other"
    description: str = "null"
