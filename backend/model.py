from pydantic import BaseModel
import datetime


class Todo(BaseModel):
    user_id: str = 'default'
    user: str = 'default'
    title: str = 'default'
    description: str = 'default'
    update_dt: datetime.datetime = datetime.datetime.now()
