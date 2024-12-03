
from fastapi.testclient import TestClient
from unittest.mock import patch
from pydantic import BaseModel
from schemas.books import Book
from main import app

client = TestClient(app)

mock_books = [
    Book(id=1, name="Book 1", author="Author 1", isbn="123456789"),
    Book(id=2, name="Book 2", author="Author 2", isbn="123356789"),
]

@patch("crud.books.books", mock_books)
def test_get_book_by_id():
    """test getting a book using its id"""
    response = client.get("/books/1")
    assert response.status_code == 200
    assert response.json() == {"message":"success", "data": mock_books[0].model_dump()}

@patch("crud.books.books", mock_books)
def test_get_books():
    """test getting all books"""
    response = client.get("/books")
    expected_data = [book.model_dump() for book in mock_books]
    response_data=response.json()
    assert response.status_code == 200
    assert response.json() == {"message": "success", "data": expected_data}


@patch("crud.books.books", mock_books)
def test_get_book_not_found():
    """test getting a non-existent book"""
    response = client.get("/books/5")
    assert response.status_code == 404
    assert response.json()["detail"] == "Book not found"


@patch("crud.books.books", mock_books)
def test_create_book():
    """test creating a book with valid data"""
    data={
        "name": "Book 3",
        "author": "Author 3",
        "isbn": "123456799"
    }
    correct_id = len(mock_books) + 1
    response = client.post("/books", json = data)
    new_book = Book(**response.json()['data'])
    correct_book = Book(**data, id=correct_id)
    assert response.status_code == 201
    assert new_book == correct_book
    assert new_book in mock_books


@patch("crud.books.books", mock_books)
def test_update_book():
    """test update a book with valid data"""
    data = {
        "name": "Book New",
        "author": "Author New",
        "isbn": "123450000"
    }
    response = client.put("/books/1", json=data)

    assert response.status_code == 200
    print(response.json())
    assert response.json()["data"]["author"] == "Author New"
    assert response.json()["data"]["isbn"] == "123450000"
    assert response.json()["data"]["name"] == "Book New"
    assert Book(**response.json()['data']) in mock_books

@patch("crud.books.books", mock_books)
def test_delete_book():
    response=client.delete("/books/1")
    assert response.status_code == 204

    response = client.get("/books/1")
    assert response.status_code == 404
    assert response.json()["detail"] == "Book not found"