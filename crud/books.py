from fastapi import HTTPException
from typing import Optional
from schemas.books import Book, BookCreate, BookUpdate

books = [
    Book(id=1, name="Book 1", author="Author 1", isbn="1234567890"),
    Book(id=2, name="Book 2", author="Author 2", isbn="9876543210"),
    Book(id=3, name="Book 3", author="Author 3", isbn="0123456789"),
]



class BookCrud:
    @staticmethod
    def get_books():
        return books


    @staticmethod
    def get_book(book_id):
        book: Optional[Book] = None
        for current_book in books:
            if current_book.id == book_id:
                book = current_book
                break
        return book


    @staticmethod
    def create_book(book: BookCreate):
        new_book = Book(id=len(books) + 1, **book.model_dump())
        books.append(new_book)
        return new_book


    @staticmethod
    def update_book(book: Optional[Book], data: BookUpdate):
        if not book:
            raise HTTPException(
                status_code=404, detail="Book not found"
            )
        book.name = data.name
        book.author = data.author
        book.isbn = data.isbn
        return book    


    # @staticmethod
    # def delete_book(book_id: int):
    #     for current_book in books:
    #         if current_book.id not in books:
    #             raise HTTPException(status_code=404, detail="Book not found")    
    #         books.remove(current_book)
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
