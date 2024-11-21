from fastapi import APIRouter
from typing import Optional
from schemas.books import (
    Book,
    BookCreate,
    BookUpdate
)
from crud.books import book_crud

book_router = APIRouter()



books = [
    Book(id=1, name="Book 1", author="Author 1", isbn="1234567890"),
    Book(id=2, name="Book 2", author="Author 2", isbn="9876543210"),
    Book(id=3, name="Book 3", author="Author 3", isbn="0123456789"),
]


@book_router.get("/")
def get_books():
    return {"message": "success", "data": book_crud.get_books()}



@book_router.post("/")
def create_book(payload: BookCreate):
    book = Book(**payload.model_dump(), id=len(books) + 1)
    books.append(book)
    return {"message": "success", "data": book}


@book_router.put("/{book_id}")
def update_book(book_id: int, payload: BookUpdate):
    book: Optional[Book] = book_crud.get_book(book_id)
    updated_book: Book = book_crud.update_book(book, payload)
    return {"message": "success", "data": updated_book}


@book_router.delete("/{book_id}")
def delete_book(book_id: int):
    return book_crud.delete_book(book_id)
