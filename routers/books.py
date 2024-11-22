from fastapi import APIRouter
from typing import Optional
from schemas.books import (
    BookCreate,
    BookUpdate,
    Book
)

from crud.books import book_crud

book_router = APIRouter()

@book_router.get("/{value}")
def get_book(value: str):
    return {"message": "success", "data": book_crud.get_book(value)}

@book_router.get("/")
def get_books():
    return {"message": "success", "data": book_crud.get_books()}

@book_router.post("/", status_code=201)
def create_book(payload: BookCreate):
    new_book = book_crud.create_book(payload)
    return {"message": "success", "data": new_book}

@book_router.put("/{value}")
def update_book(value: str, payload: BookUpdate):
    book: Optional[Book] = book_crud.get_book(value)
    updated_book = book_crud.update_book(book, payload)
    return {"message": "success", "data": updated_book}

@book_router.delete("/{value}", status_code=204)
def delete_book(value: str):
    return book_crud.delete_book(value)