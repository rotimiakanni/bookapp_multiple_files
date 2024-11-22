from main import *
from fastapi.testclient import TestClient

client=TestClient(app)

def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to bookapp!"}

