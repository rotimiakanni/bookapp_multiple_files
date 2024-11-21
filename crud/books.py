from typing import Optional
from fastapi import HTTPException
from schemas.books import Book, BookCreate, BookUpdate


books = [
    Book(id=1, name="Book 1", author="Author 1", isbn="1234567890"),
    Book(id=2, name="Book 2", author="Author 2", isbn="9876543210"),
    Book(id=3, name="Book 3", author="Author 3", isbn="0123456789"),
]

class Bookcrud:

    @staticmethod
    def get_book(user_id):
        one_book: Optional[Book] = None
        for current_book in books:
            if current_book.id == user_id:
                one_book = current_book
                break
        return one_book

    @staticmethod
    def get_books():
        return {"message": "success", "data": books}
    
    @staticmethod
    def create_book(payload: BookCreate):
        new_book = Book(**payload.model_dump(), id=len(books) + 1)
        books.append(new_book)
        return {"message": "success", "data": new_book}
    
    @staticmethod
    def update_book(new: Optional[Book], old: BookUpdate):
        if not new:
            raise HTTPException(
                status_code=404, detail="Book not found"
            )
        new.name = old.name
        new.author = old.author
        new.isbn = old.isbn
        return new
    
    @staticmethod
    def delete_book(user_id: int):
        book = Bookcrud.get_book(user_id)
        if not book:
            raise HTTPException(status_code=404, detail = "Book not found")
        books.remove(book)
        return {"message": "Book deleted"}




book_crud = Bookcrud()