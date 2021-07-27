from pydantic import BaseModel
import datetime


class Todo(BaseModel):
    user: str
    title: str
    description: str
    update_dt: datetime.datetime = datetime.datetime.now()
