import pytest
import json
import jwt
from api import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_health_endpoint(client):
    response = client.get('/api/health')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['status'] == 'healthy'

def test_login_success(client):
    response = client.post('/api/login',
                          data=json.dumps({'username': 'admin', 'password': 'admin123'}),
                          content_type='application/json')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert 'token' in data
    assert len(data['token']) > 0

def test_login_invalid_credentials(client):
    response = client.post('/api/login',
                          data=json.dumps({'username': 'admin', 'password': 'wrongpass'}),
                          content_type='application/json')
    assert response.status_code == 401
    data = json.loads(response.data)
    assert data['message'] == 'Invalid credentials'

def test_login_missing_username(client):
    response = client.post('/api/login',
                          data=json.dumps({'password': 'admin123'}),
                          content_type='application/json')
    assert response.status_code == 400
    data = json.loads(response.data)
    assert 'Missing username or password' in data['message']

def test_login_missing_password(client):
    response = client.post('/api/login',
                          data=json.dumps({'username': 'admin'}),
                          content_type='application/json')
    assert response.status_code == 400
    data = json.loads(response.data)
    assert 'Missing username or password' in data['message']

def test_login_nonexistent_user(client):
    response = client.post('/api/login',
                          data=json.dumps({'username': 'hacker', 'password': 'test123'}),
                          content_type='application/json')
    assert response.status_code == 401
    data = json.loads(response.data)
    assert data['message'] == 'Invalid credentials'

def test_protected_endpoint_with_valid_token(client):
    login_response = client.post('/api/login',
                                 data=json.dumps({'username': 'admin', 'password': 'admin123'}),
                                 content_type='application/json')
    token = json.loads(login_response.data)['token']
    
    response = client.get('/api/protected',
                         headers={'Authorization': f'Bearer {token}'})
    assert response.status_code == 200
    data = json.loads(response.data)
    assert 'Access granted' in data['message']

def test_protected_endpoint_without_token(client):
    response = client.get('/api/protected')
    assert response.status_code == 401
    data = json.loads(response.data)
    assert data['message'] == 'Token is missing'

def test_protected_endpoint_with_invalid_token(client):
    response = client.get('/api/protected',
                         headers={'Authorization': 'Bearer invalid.token.here'})
    assert response.status_code == 401
    data = json.loads(response.data)
    assert data['message'] == 'Invalid token'

def test_token_contains_correct_payload(client):
    response = client.post('/api/login',
                          data=json.dumps({'username': 'user', 'password': 'user123'}),
                          content_type='application/json')
    token = json.loads(response.data)['token']
    
    decoded = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
    assert decoded['user'] == 'user'
    assert 'exp' in decoded
