from fastapi import APIRouter, status
from typing import Optional
from schemas.books import (
    BookCreate,
    BookUpdate,
    Book
)

from crud.books import book_crud

book_router = APIRouter()

@book_router.get("/{book_id}", status_code=200)
def get_book(book_id: int):
    return {"message": "success", "data": book_crud.get_book(book_id)}

@book_router.get("/",  status_code=200)
def get_books():
    return {"message": "success", "data": book_crud.get_books()}

@book_router.post("/", status_code=201)
def create_book(payload: BookCreate):
    new_book = book_crud.create_book(payload)
    return {"message": "success", "data": new_book}

@book_router.put("/{book_id}", status_code=201)
def update_book(book_id: int, payload: BookUpdate):
    book: Optional[Book] = book_crud.get_book(book_id)
    updated_book = book_crud.update_book(book, payload)
    return {"message": "success", "data": updated_book}

@book_router.delete("/{book_id}", status_code=204)
def delete_book(book_id: int):
    return book_crud.delete_book(book_id)