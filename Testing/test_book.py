from fastapi.testclient import TestClient
from main import *



client = TestClient(app)


books = [
    {"id": 1, "name": "Book 1", "author": "Author 1", "isbn": "1234567890"},
    {"id": 2, "name": "Book 2", "author": "Author 2", "isbn": "9876543210"},
    {"id": 3, "name": "Book 3", "author": "Author 3", "isbn": "0123456789"},
]

new_book = {"id": 4, "name": "Book 4", "author": "Author 4", "isbn": "1122334955"}

updated_book = {"id": 3,"name": "Harry Potter", "author": "Minabade", "isbn": "9876543210"}
update_book = {"name": "Harry Potter", "author": "Minabade", "isbn": "9876543210"}


def test_get_book():
    response = client.get("/books/1")
    assert response.status_code == 200
    assert response.json() == {"message": "success", "data": {"id": 1, "name": "Book 1", "author": "Author 1", "isbn": "1234567890"}}

def test_book_not_found():
    response = client.get("/books/7")
    assert response.status_code == 404
    assert response.json()["detail"] == "Book not found"


def test_get_books():
    response = client.get("/books")
    assert response.status_code == 200
    assert response.json() == {"message": "success", "data": [{"id": 1, "name": "Book 1", "author": "Author 1", "isbn": "1234567890"},
    {"id": 2, "name": "Book 2", "author": "Author 2", "isbn": "9876543210"},
    {"id": 3, "name": "Book 3", "author": "Author 3", "isbn": "0123456789"}]}


def test_create_books():
    response = client.post("/books", json=new_book)
    assert response.status_code == 201
    assert response.json() == {"message": "success", "data": new_book}


def test_update_books():
    response = client.put("/books/3", json=updated_book)
    assert response.status_code == 201
    assert response.json() == {"message": "success", "data": updated_book}

def test_delete_book():
    response = client.delete("/books/1")
    assert response.status_code == 204
    response = client.get("/books/1")
    assert response.status_code == 404
    assert response.json()["detail"] == "Book not found"

    


