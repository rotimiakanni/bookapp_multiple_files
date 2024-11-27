from fastapi import APIRouter, HTTPException
from typing import Optional
from schemas.users import(
    User,
    UserCreate,
    UserUpdate,UserPatch
)
from crud.users import user_crud, users


user_router= APIRouter()


@user_router.get("/")
def get_users():
    return{"message":"successful", "data": user_crud.get_users()}

@user_router.post("/")
def create_user(payload: UserCreate):
    new_user = user_crud.create_user(payload)
    users.append(new_user)
    return {"message": "success", "data":(new_user)}

@user_router.put("/{user_id}")
def update_user(user_id:int, payload: UserUpdate):
    user: Optional[User] = user_crud.get_user(user_id)
    updated_user: User = user_crud.update_user(user, payload)
    return {"message": "success", "data": updated_user}

@user_router.patch("/{user_id}")
def partially_update_user(user_id: int, payload:UserPatch):
    #Find User
    user: Optional[User] = None
    for current_user in users:
        if current_user.id == user_id:
            user = current_user
            break

    updated_user = user_crud.partially_update_user(user, payload)
    return {"message": "User updated successfully", "data": updated_user}
   
@user_router.delete("/{user_id}")
def delete_user(user_id: int):
    try:
        result = user_crud.delete_user(user_id)
        return result
    except HTTPException as e:
        raise e