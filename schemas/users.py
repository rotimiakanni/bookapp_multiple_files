from pydantic import BaseModel


class UserBase(BaseModel):
    username: str
    email: str
    name: str


class User(UserBase):
    id: int


class UserCreate(UserBase):
    pass


class UserUpdate(UserBase):
    pass
