from typing import Optional
from fastapi import APIRouter
from schemas.books import (
    Book,
    BookCreate,
    BookUpdate
)
from crud.books import book_crud

book_router = APIRouter()


@book_router.get("/")
def get_books():
    return {"message": "success", "data": book_crud.get_books()}


@book_router.post("/")
def create_book(payload: BookCreate):
    new_book = book_crud.create_book(payload)
    return {"message": "success", "data": new_book}

@book_router.put("/{user_id}")
def update_book(user_id: int, payload:BookUpdate):
    user : Optional[Book] = book_crud.get_book(user_id)
    update_book = book_crud.update_book(user, payload)
    return {"message": "success", "data": update_book}

@book_router.delete("/{user_id}")
def delete_book(user_id :int):
    deleted_book = book_crud.delete_book(user_id)
    return {"message": "sucess", "data": deleted_book}
