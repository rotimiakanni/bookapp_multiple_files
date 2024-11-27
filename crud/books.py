from fastapi import HTTPException
from typing import Optional
from schemas.books import Book, BookBase, BookCreate, BookUpdate, BookPatch


books = [
    Book(id=1, name="carter", author="lewis capaldi", isbn=123456789),
    Book(id=2, name="pitcher", author="dantes peters", isbn=23456789),
    Book(id=3, name="lifted", author="john doe", isbn=3456789)
]

    
class BookCRUD:
    @staticmethod
    def get_book(book_id: int):
        book: Optional[Book]
        for current_book in books:
            if current_book.id == book_id:  # Ensure exact match
                return current_book
        return None  # Return None if no match is found

            
    @staticmethod
    def get_books():
        return books
    
    @staticmethod
    def create_book(book: BookCreate):
        new_book = Book(id=len(book_crud.get_books()) +1, **book.model_dump())
        books.append(new_book)
        return new_book

    @staticmethod
    def update_book(book : Optional[Book], data: BookUpdate):
        if not book:
            raise HTTPException(
                status_code=404, detail= "book not found"
            )
        book.name = data.name
        book.author = data.author
        book.isbn = data.isbn
        return book
    
    @staticmethod
    def partially_update_book(book: Optional[Book], data: BookPatch):
        if not book:
            raise HTTPException(
                status_code=404, detail="Book not found"
            )
        if data.name is not None:
            book.name = data.name
        if data.author is not None:
            book.author = data.author
        if data.isbn is not None:
            book.isbn = data.isbn
        return book


    @staticmethod
    def delete_book(book_id: int):
        book = book_crud.get_book(book_id)
        if not book:
            raise HTTPException (
                status_code=404, detail="book not found"
            )
        books.remove(book)
        return {"message": "book deleted"}
    
    

    
book_crud = BookCRUD()