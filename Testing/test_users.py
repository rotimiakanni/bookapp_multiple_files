from fastapi.testclient import TestClient
from main import *


client = TestClient(app)

users = [
    {"id": 1, "username": "user1", "email": "user1@example.com", "name": "User 1"},
    {"id": 2, "username": "user2", "email": "user2@example.com", "name": "User 2"},
    {"id": 3, "username": "user3", "email": "user3@example.com", "name": "User 3"},
]


new_user = {"id":4,"username":"user4", "email":"user4@example.com", "name":"User 4"}
updated_user = {"id":2,"username":"Mina", "email":"mina@example.com", "name":"Mina"}


def test_get_user():
    response = client.get("/users/1")
    assert response.status_code == 200
    assert response.json() == {"message": "success", "data": {"id":1, "username":"user1", "email":"user1@example.com", "name":"User 1"}}

def test_user_not_found():
    response = client.get("/users/7")
    assert response.status_code == 404
    assert response.json()["detail"] == "User not found"

def test_get_users():
    response = client.get("/users")
    assert response.status_code == 200
    assert response.json() == {"message": "success", "data": [{"id":1, "username":"user1", "email":"user1@example.com", "name":"User 1"},{"id":2, "username":"user2", "email":"user2@example.com", "name":"User 2"},{"id":3, "username":"user3", "email":"user3@example.com", "name":"User 3"}]}

def test_create_users():
    response = client.post("/users", json=new_user)
    assert response.status_code == 201
    assert response.json() == {"message": "success", "data": new_user}

def test_update_user():
    response = client.put("/users/2", json=updated_user)
    assert response.status_code == 201
    assert response.json() == {"message": "success", "data": updated_user}

def test_delete_users():
    response = client.delete("/users/1")
    assert response.status_code == 204
    response = client.get("/users/1")
    assert response.status_code == 404
    assert response.json()["detail"] == "User not found"




