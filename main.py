import uuid

import uvicorn
from fastapi import FastAPI
from starlette.middleware.authentication import AuthenticationMiddleware
from starlette.middleware import Middleware
from fastapi_users import FastAPIUsers

from src.auth.models import User
from src.auth.manager import get_user_manager
from src.auth.config import auth_backend, BasicAuthBackend
from src.auth.schemas import UserRead, UserCreate
from src.task.router import task_router


fastapi_users = FastAPIUsers[User, uuid.UUID](
    get_user_manager,
    [auth_backend],
)

current_user = fastapi_users.current_user()

middleware = [
    Middleware(AuthenticationMiddleware, backend=BasicAuthBackend())
]

app = FastAPI(middleware=middleware)

app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)
app.include_router(task_router)

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
