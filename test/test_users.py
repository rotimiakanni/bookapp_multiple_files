from main import *
from routers.users import get_user
from schemas.users import User
from fastapi.testclient import TestClient
from main import app
from schemas.users import User
from crud.users import users

client=TestClient(app)

mock_users = [
    User(id=1, username="user1", email="user1@example.com", name="User 1"),
    User(id=2, username="user2", email="user2@example.com", name="User 2")
    ]

expected_user_data = {
            "id": 1,
            "username": "user1",
            "email": "user1@example.com",
            "name": "User 1"
        }
def test_get_user_by_id():
    response = client.get("/users/1")
    assert response.status_code == 200
    assert response.json() == {"message":"success", "data": expected_user_data}

def test_get_user_by_name():
    response = client.get("/users/user1")
    assert response.status_code == 200
    assert response.json() == {"message": "success", "data": expected_user_data}

def test_get_user_not_found():
    response = client.get("/users/user5")
    assert response.status_code == 404
    assert response.json()["detail"] == "User with username 'User5' not found"

def test_get_users():
    response=client.get("/users")
    assert response.status_code == 200
    assert users == [User(**user) for user in response.json()['data']]

def test_create_user():
    data={
        "username": "newguy",
        "email": "new@example.com",
        "name": "New Person"
    }
    correct_id = len(users) + 1

    response = client.post("/users", json = data)
    new_user = User(**response.json()['data'])
    correct_user = User(**data, id=correct_id)
    assert response.status_code == 201
    assert new_user == correct_user
    assert new_user in users

def test_update_user_by_name():
    data = {
        "username": "updatedHuman",
        "email": "new@example.com",
        "name": "New Human"
    }
    response = client.put("/users/user1", json=data)

    assert response.status_code == 200
    print(response.json())
    assert response.json()["data"]["username"] == "updatedHuman"
    assert response.json()["data"]["email"] == "new@example.com"
    assert response.json()["data"]["name"] == "New Human"

def test_update_user_by_id():
    data = {
        "username": "updatedHuman",
        "email": "new@example.com",
        "name": "New Human"
    }
    response = client.put("/users/1", json=data)

    assert response.status_code == 200
    print(response.json())
    assert response.json()["data"]["username"] == "updatedHuman"
    assert response.json()["data"]["email"] == "new@example.com"
    assert response.json()["data"]["name"] == "New Human"

def test_delete_user_by_id():
    response=client.delete("/users/1")
    assert response.status_code == 204

    response = client.get("/users/1")
    assert response.status_code == 404
    assert response.json()["detail"] == "User with id 1 not found"

def test_delete_user_by_username():
    response=client.delete("/users/user2")
    assert response.status_code == 204

    response = client.get("/users/user2")
    assert response.status_code == 404
    assert response.json()["detail"] == "User with username 'User2' not found"

def test_delete_user_not_found():
    response = client.delete("/users/user5")
    assert response.status_code == 404
    assert response.json()["detail"] == "User with username 'User5' not found"