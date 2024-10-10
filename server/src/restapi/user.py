from fastapi import APIRouter

from ..modules.user.controller import UserController
from ..modules.user.schema import (
    User,
    UserAddressCreate,
    UserCreate,
    UserUpsert,
)

router = APIRouter()


@router.get("/users", tags=["users"])
def list_users() -> list[User]:
    return UserController().get_all_users()


@router.get("/users/{user_id}", tags=["users"])
def get_user(user_id: int) -> User:
    return UserController().get_user(user_id)


@router.post("/user", tags=["users"])
def create_user(user: UserCreate) -> User:
    return UserController().create_user(user)


@router.post("/upsert_user", tags=["users"])
def upsert_user(user: UserUpsert):
    return UserController().upsert_user(user)
