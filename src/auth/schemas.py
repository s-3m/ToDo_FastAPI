import uuid

from fastapi_users import schemas
from pydantic import EmailStr


class UserRead(schemas.BaseUser[uuid.UUID]):
    login: str
    first_name: str
    last_name: str


class UserCreate(schemas.BaseUserCreate):
    login: str
    first_name: str
    last_name: str


class UserUpdate(schemas.BaseUserUpdate):
    first_name: str
    last_name: str
