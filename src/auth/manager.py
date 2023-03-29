import uuid
from typing import Optional

from fastapi import Depends, Request
from fastapi_users import BaseUserManager, UUIDIDMixin

from .models import User, get_user_db
from settings import AUTH_TOKEN_SECRET


class UserManager(UUIDIDMixin, BaseUserManager[User, uuid.UUID]):
    reset_password_token_secret = AUTH_TOKEN_SECRET
    verification_token_secret = AUTH_TOKEN_SECRET

    async def on_after_register(self, user: User, request: Optional[Request] = None):
        print(f"Пользователь --> {user.id} был зарегистрирован.")

    async def on_after_forgot_password(
        self, user: User, token: str, request: Optional[Request] = None
    ):
        print(f"User {user.id} has forgot their password. Reset token: {token}")

    async def on_after_request_verify(
        self, user: User, token: str, request: Optional[Request] = None
    ):
        print(f"Verification requested for user {user.id}. Verification token: {token}")


async def get_user_manager(user_db=Depends(get_user_db)):
    yield UserManager(user_db)
