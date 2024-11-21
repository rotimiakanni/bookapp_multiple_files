
from pydantic import BaseModel


class BookBase(BaseModel):
    name: str
    author: str
    isbn: str


class Book(BookBase):
    id: int


class BookCreate(BookBase):
    pass


class BookUpdate(BookBase):
    pass
