from typing import Optional
from fastapi import APIRouter, status
from schemas.users import (
    User,
    UserCreate,
    UserUpdate
)
from crud.users import user_crud

user_router = APIRouter()

@user_router.get("/{user_id}", status_code=200)
def get_user(user_id: int):
    return {"message": "success", "data": user_crud.get_user(user_id)}

@user_router.get("/", status_code=200)
def get_users():
    return {"message": "success", "data": user_crud.get_users()}


@user_router.post("/", status_code=201)
def create_user(payload: UserCreate):
    new_user = user_crud.create_user(payload)
    return {"message": "success", "data": new_user}


@user_router.put("/{user_id}", status_code=201)
def update_user(user_id: int, payload: UserUpdate):
    user: Optional[User] = user_crud.get_user(user_id)
    updated_user: User = user_crud.update_user(user, payload)
    return {"message": "success", "data": updated_user}


@user_router.delete("/{user_id}", status_code=204)
def delete_user(user_id: int):
    return user_crud.delete_user(user_id)
