from fastapi.testclient import TestClient
from unittest.mock import patch
from pydantic import BaseModel
from schemas.users import User
from main import app

client = TestClient(app)

mock_users = [
    User(id=1, username="user1", email="user1@example.com", name="User 1"),
    User(id=2, username="user2", email="user2@example.com", name="User 2")
]

@patch("crud.users.users", mock_users)
def test_get_user_by_id():
    """test getting a user using their id"""
    response = client.get("/users/1")
    assert response.status_code == 200
    assert response.json() == {"message":"success", "data": mock_users[0].model_dump()}

@patch("crud.users.users", mock_users)
def test_get_users():
    """test getting all users"""
    response = client.get("/users")
    expected_data = [user.model_dump() for user in mock_users]
    response_data=response.json()
    assert response.status_code == 200
    assert response.json() == {"message": "success", "data": expected_data}

@patch("crud.users.users", mock_users)
def test_get_user_not_found():
    """test getting a non-existent user"""
    response = client.get("/users/5")
    assert response.status_code == 404
    assert response.json()["detail"] == "User not found"


@patch("crud.users.users", mock_users)
def test_create_user():
    """test creating a with valid data"""
    data={
        "username": "new_guy",
        "email": "new@example.com",
        "name": "New Guy"
    }
    correct_id = len(mock_users) + 1

    response = client.post("/users", json = data)
    new_user = User(**response.json()['data'])
    correct_user = User(**data, id=correct_id)
    assert response.status_code == 201
    assert new_user == correct_user
    assert new_user in mock_users


@patch("crud.users.users", mock_users)
def test_update_user():
    """test updating a user with valid data"""
    data = {
        "username": "updatedHuman",
        "email": "new@example.com",
        "name": "New Human"
    }
    response = client.put("/users/1", json=data)

    assert response.status_code == 200
    assert response.json()["data"]["username"] == "updatedHuman"
    assert response.json()["data"]["email"] == "new@example.com"
    assert response.json()["data"]["name"] == "New Human"
    assert User(**response.json()["data"]) in mock_users

@patch("crud.users.users", mock_users)
def test_delete_user():
    """test deleting an existing user"""
    response=client.delete("/users/1")
    assert response.status_code == 204

    response = client.get("/users/1")
    assert response.status_code == 404
    assert response.json()["detail"] == "User not found"


