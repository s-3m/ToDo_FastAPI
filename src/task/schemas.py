import datetime
import uuid
from typing import Optional, List

from pydantic import BaseModel

from src.auth.schemas import UserRead


class MyUserRead(BaseModel):
    login: str
    first_name: str
    last_name: str

    class Config:
        orm_mode = True


class ShowTask(BaseModel):
    title: str
    text: str
    is_finished: bool
    created: datetime.datetime
    user: MyUserRead

    class Config:
        orm_mode = True


class CreateTask(BaseModel):
    title: str
    text: str
    user_id: uuid.UUID
