from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional


class BookBase(BaseModel):
    name:str
    author:str
    isbn:int

class Book(BookBase):
    id:int

class BookCreate(BookBase):
    pass

class BookUpdate(BookBase):
    pass

class BookPatch(BookBase):
    name: Optional[str] = None
    author: Optional[str] = None
    isbn: Optional[int] = None

class BookDelete(BookBase):
    pass
