from fastapi.testclient import TestClient
from hello import app

client = TestClient(app)

def test_hello_endpoint():
    response = client.get("/hello")
    assert response.status_code == 200
    assert response.json() == {"message": "hello"}
