from fastapi import HTTPException
from typing import Optional
from schemas.users import User, UserCreate, UserUpdate


users = [
    User(id=1, username="user1", email="user1@example.com", name="User 1"),
    User(id=2, username="user2", email="user2@example.com", name="User 2"),
    User(id=3, username="user3", email="user3@example.com", name="User 3"),
]


class UserCrud:
    @staticmethod
    def get_user(user_id):
        user: Optional[User] = None
        for current_user in users:
            if current_user.id == user_id:
                user = current_user
                break
        if user == None:
                raise HTTPException(
                    status_code=404, detail="User not found"
                )
        return user

    @staticmethod
    def get_users():
        return users

    @staticmethod
    def create_user(user: UserCreate):
        new_user = User(id=len(user_crud.get_users()) + 1, **user.model_dump())
        users.append(new_user)
        return new_user

    @staticmethod
    def update_user(user: Optional[User], data: UserUpdate):
        if not user:
            raise HTTPException(
                status_code=404, detail="User not found"
            )
        user.username = data.username
        user.email = data.email
        user.name = data.name
        return user

    @staticmethod
    def delete_user(user_id: int):
        user = UserCrud.get_user(user_id)
        if not user:
            raise HTTPException(
                status_code=404, detail="User not found"
            )
        users.remove(user)
        return {"message": "User deleted"}


user_crud = UserCrud()
