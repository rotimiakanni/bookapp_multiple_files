from typing import Optional
from fastapi import APIRouter, HTTPException
from schemas.books import(
    Book,
    BookCreate,
    BookUpdate,
    BookPatch
)
from crud.books import book_crud, books

book_router=APIRouter()


@book_router.get("/")
def get_books():
    return {"message":"successful","data" : books }


@book_router.post("/")
def create_book(payload: BookCreate):
    new_book = Book(id=len(books) +1, **payload.model_dump())
    books.append(new_book)
    return {"message":"success", "data":(new_book)}

@book_router.put("/{book_id}")
def update_book(book_id:int, payload: BookUpdate):
    book: Optional[Book]
    for current_book in books:
        if current_book.id == book_id:
            book = current_book
            break
    if book:
        book.name = payload.name
        book.author = payload.author
        book.isbn = payload.isbn
        return {"message": "successful", "data":book}
    else :
        return{"message":"user not found"}
    
@book_router.patch("/{book_id}")
def partially_update_book(book_id: int, payload:BookPatch):
    #Find book
    book: Optional[Book] = None
    for current_book in books:
        if current_book.id == book_id:
            book = current_book
            break

    updated_book = book_crud.partially_update_book(book, payload)
    return {"message": "Book updated successfully", "data": updated_book}