from main import *
from schemas.books import Book
from fastapi.testclient import TestClient
from crud.books import books

client=TestClient(app)

mock_books = [
    Book(id=1, name="Book 1", author="Author 1", isbn="1234567890"),
    Book(id=2, name="Book 2", author="Author 2", isbn="9876543210")
    ]

expected_book_data = {
            "author": "Author 1",
            "id": 1,
            "isbn": "1234567890",
            "name": "Book 1",
        }

def test_get_book_by_id():
    response = client.get("/books/1")
    print("Actual response:", response.json())
    print("Expected response:", {"message": "success", "data": expected_book_data})
    assert response.status_code == 200
    assert response.json() == {"message": "success", "data": expected_book_data}

def test_get_book_by_name():
    response = client.get("/books/Book%201")
    assert response.status_code == 200
    assert response.json() == {"message":"success", "data": expected_book_data}

def test_get_book_not_found():
    response = client.get("/books/5")
    assert response.status_code == 404
    assert response.json()["detail"] == "Book with id 5 not found"

def test_get_books():
    response=client.get("/books")
    assert response.status_code == 200
    assert books == [Book(**item) for item in response.json()['data']]

def test_create_book():
    data=data = {
            "author": "Author 3",
            "isbn": "1234567890",
            "name": "Book 7",
        }
    correct_id = len(books) + 1

    response = client.post("/books", json = data)
    new_book = Book(**response.json()['data'])
    correct_book = Book(**data, id=correct_id)
    assert response.status_code == 201
    assert new_book == correct_book
    assert new_book in books

def test_update_book_by_name():
    data = {
        "author": "Author New",
        "isbn": "1234567000",
        "name": "Book New",
    }
    response = client.put("/books/Book%201", json=data)

    assert response.status_code == 200
    print(response.json())
    assert response.json()["data"]["author"] == "Author New"
    assert response.json()["data"]["isbn"] == "1234567000"
    assert response.json()["data"]["name"] == "Book New"

def test_update_book_by_id():
    data = {
        "author": "Author New",
        "isbn": "1234567000",
        "name": "Book New",
    }
    response = client.put("/books/1", json=data)

    assert response.status_code == 200
    print(response.json())
    assert response.json()["data"]["author"] == "Author New"
    assert response.json()["data"]["isbn"] == "1234567000"
    assert response.json()["data"]["name"] == "Book New"

def test_delete_book_by_id():
    response=client.delete("/books/1")
    assert response.status_code == 204

    response = client.get("/books/1")
    assert response.status_code == 404
    assert response.json()["detail"] == "Book with id 1 not found"

def test_delete_book_by_name():
    response=client.delete("/books/Book%202")
    assert response.status_code == 204

    response = client.get("/books/book2")
    assert response.status_code == 404
    assert response.json()["detail"] == "Book with name 'Book2' not found"

def test_delete_book_not_found():
    response = client.delete("/books/5")
    assert response.status_code == 404
    assert response.json()["detail"] == "Book with id 5 not found"