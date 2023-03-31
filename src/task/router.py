from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from pydantic import parse_obj_as
from sqlalchemy.orm import selectinload

from database import get_db
from src.auth.models import User
from src.task.models import Task
from src.task.schemas import ShowTask, CreateTask


task_router = APIRouter(prefix='/tasks', tags=['tasks'])


@task_router.get('/show', response_model=List[ShowTask])
async def get_tasks(db: AsyncSession = Depends(get_db)) -> List[ShowTask]:
    stmt = select(Task).options(selectinload(Task.user))
    result = await db.scalars(stmt)
    task_list = parse_obj_as(List[ShowTask], result.all())
    return task_list


@task_router.post('/add', response_model=ShowTask)
async def create_task(body: CreateTask, db: AsyncSession = Depends(get_db)) -> ShowTask:
    async with db.begin():
        stmt = select(User).where(User.login == 's-3m')
        user = await db.scalar(stmt)
        new_task = Task(title=body.title, text=body.text, user_id=user.id)
        print(new_task.title, new_task.is_finished)
        await db.commit()
        return ShowTask(title=new_task.title, text=new_task.text, user_id=new_task.user_id, is_finished=new_task.is_finished, created=new_task.created)
