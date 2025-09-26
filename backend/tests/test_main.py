from fastapi.testclient import TestClient
from backend.main import app

client = TestClient(app)

def test_ping():
    response = client.get("/ping")
    assert response.status_code == 200
    assert response.json() == {"message": "pong"}

def test_get_movies():
    response = client.get("/movies")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert "title" in data[0]
