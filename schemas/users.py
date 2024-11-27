from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional


class UserBase(BaseModel):
    username:str
    email:str
    name:str

class User(UserBase):
    id:int

class UserCreate(UserBase):
    pass

class UserUpdate(UserBase):
    pass

class UserPatch(UserBase):
    username: Optional[str] = None
    emai: Optional[str] = None
    name: Optional[int] = None

class UserDelete(UserBase):
    pass
