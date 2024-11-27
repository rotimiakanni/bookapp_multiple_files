from fastapi import HTTPException
from typing import Optional
from schemas.users import User, UserCreate, UserUpdate, UserDelete, UserPatch

users = [
    User(id=1, username="user1", email="üser1@gmail.com", name="User1"),
    User(id=2, username="user2", email="üser2@gmail.com", name="User2"),
    User(id=3, username="user3", email="üser3@gmail.com", name="User3"),
]

class UserCRUD:
    @staticmethod
    def get_user(user_id: int):
        user: Optional[User]
        for current_user in users:
            if current_user.id == user_id:
                return current_user
        return None
    
    @staticmethod
    def get_users():
        return users
    
    @staticmethod
    def create_user(user: UserCreate):
        new_user = User(id=len(user_crud.get_users()) +1, **user.model_dump())
        users.append(new_user)
        return new_user
    
    @staticmethod
    def update_user(user : Optional[User], data: UserUpdate):
        if not user:
            raise HTTPException(
                status_code=404, detail= "user not found"
            )
        user.username = data.username
        user.email = data.email
        user.name = data.name
        return user
    
    @staticmethod
    def partially_update_user(user: Optional[User], data: UserPatch):
        if not user:
            raise HTTPException(
                status_code=404, detail="User not found"
            )
        if data.username is not None:
            user.username = data.username
        if data.email is not None:
            user.email = data.email
        if data.name is not None:
            user.name = data.name
        return user

    @staticmethod
    def delete_user(user_id: int):
        User = user_crud.get_user(user_id)
        if not User:
            raise HTTPException (
                status_code=404, detail="user not found"
            )
        users.remove(User)
        return {"message": "user deleted"}

    
user_crud = UserCRUD()