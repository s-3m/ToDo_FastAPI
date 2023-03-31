from typing import List

from fastapi import Depends
from fastapi_users.db import SQLAlchemyBaseUserTableUUID, SQLAlchemyUserDatabase
from sqlalchemy import String, Column
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import relationship, backref, Mapped

from database import Base, get_db
from src.task.models import Task


class User(SQLAlchemyBaseUserTableUUID, Base):
    __tablename__ = "users"

    login = Column(String, nullable=False)
    first_name = Column(String, nullable=False)
    last_name = Column(String)
    email = Column(String, nullable=False)

    tasks = relationship('Task', back_populates='user')

    def __repr__(self):
        return f'User object --> login: {self.login}, name: {self.first_name} {self.last_name}'


async def get_user_db(session: AsyncSession = Depends(get_db)):
    yield SQLAlchemyUserDatabase(session, User)
