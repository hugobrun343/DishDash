from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)

def test_root() -> None:
    """Test the root endpoint"""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "DishDash API is running!"}

def test_health() -> None:
    """Test the health endpoint"""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}
