from fastapi import HTTPException
from schemas.books import Book, BookCreate, BookUpdate
from typing import Optional

books=[
    Book(id=1, name="Book 1", author="Author 1", isbn="1234567890"),
    Book(id=2, name="Book 2", author="Author 2", isbn="9876543210"),
    Book(id=3, name="Book 3", author="Author 3", isbn="0123456789"),
]

class BookCrud:
    @staticmethod
    def get_books():
        return books

    @staticmethod
    def get_book(value: str) -> Book:
        if not value:
            raise HTTPException(status_code=400, detail="Value cannot be empty")
        if value.isnumeric():  # user must be searching by id since its an integer
            value = int(value)
            book = next((book for book in books if book.id == value), None)
            if not book:
                raise HTTPException(status_code=404, detail=f"Book with id {value} not found")
        else:  # otherwise user must be searching by book name
            value = value.strip().casefold()
            book = next((book for book in books if book.name.casefold() == value), None)
            if not book:
                raise HTTPException(status_code=404, detail=f"Book with name '{value.title()}' not found")
        return book

    @staticmethod
    def create_book(payload: BookCreate):
        new_book = Book(id=len(books) + 1, **payload.model_dump())
        books.append(new_book)
        return new_book

    @staticmethod
    def update_book(book: Optional[Book], payload: BookUpdate):
        if not book:
            raise HTTPException(
                status_code=404, detail="Book not found"
            )
        book.name = payload.name
        book.author = payload.author
        book.isbn = payload.isbn
        return book

    @staticmethod
    def delete_book(value: str):
        book = BookCrud.get_book(value)
        if not book:
            raise HTTPException(
                status_code=404, detail="Book not found"
            )
        books.remove(book)
        return {"message": "Book deleted"}

book_crud = BookCrud()