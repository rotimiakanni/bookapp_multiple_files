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
    def get_book(book_id: int):
        book = next((book for book in books if book.id == book_id), None)
        if not book:
            raise HTTPException(status_code=404, detail="Book not found")
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
    def delete_book(book_id: int):
        book = BookCrud.get_book(book_id)
        if not book:
            raise HTTPException(
                status_code=404, detail="Book not found"
            )
        books.remove(book)
        return {"message": "Book deleted"}

book_crud = BookCrud()