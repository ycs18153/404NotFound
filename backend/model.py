from threading import setprofile
from pydantic import BaseModel
import datetime
from typing import Optional
from uuid import UUID, uuid4
import random
import string

from datetime import datetime

class Todo(BaseModel):
    todo_id: str = ''.join(random.choices(
        string.ascii_letters + string.digits, k=10))
    todo_name: str
    todo_date: datetime
    todo_contents: Optional[str]
    todo_update_date: str
    todo_completed: bool = False
    employee_id: Optional[str]


class EmployeeId(BaseModel):
    employee_id: str
    user_id: str


class UpdateTodo(BaseModel):
    todo_id: Optional[str]
    todo_name: Optional[str]
    todo_date: Optional[datetime]
    todo_contents: Optional[str]
    todo_update_date: Optional[str]
    todo_completed: Optional[bool]
    employee_id: Optional[str]


class Web(BaseModel):
    name: str
    url: str
    category: str = "other"
    description: str = "null"
