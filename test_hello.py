from fastapi.testclient import TestClient
from hello import app

client = TestClient(app)

def test_hello_endpoint():
    """Test GET /hello returns correct JSON response"""
    response = client.get("/hello")
    assert response.status_code == 200
    assert response.json() == {"message": "hello"}

def test_hello_endpoint_content_type():
    """Test GET /hello returns JSON content type"""
    response = client.get("/hello")
    assert response.headers["content-type"] == "application/json"
