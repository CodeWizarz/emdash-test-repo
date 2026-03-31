import pytest
import jwt
from datetime import datetime, timedelta
from api import app, users_db, hash_password

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client
    users_db.clear()

def test_health_endpoint(client):
    response = client.get('/health')
    assert response.status_code == 200
    assert response.json['status'] == 'healthy'

def test_register_success(client):
    response = client.post('/register', json={
        'username': 'testuser',
        'password': 'testpass123'
    })
    assert response.status_code == 201
    assert response.json['message'] == 'User registered successfully'

def test_register_missing_fields(client):
    response = client.post('/register', json={'username': 'testuser'})
    assert response.status_code == 400
    assert 'required' in response.json['message'].lower()

def test_register_duplicate_user(client):
    client.post('/register', json={
        'username': 'testuser',
        'password': 'testpass123'
    })
    response = client.post('/register', json={
        'username': 'testuser',
        'password': 'testpass123'
    })
    assert response.status_code == 409
    assert 'exists' in response.json['message'].lower()

def test_login_success(client):
    client.post('/register', json={
        'username': 'testuser',
        'password': 'testpass123'
    })
    
    response = client.post('/login', json={
        'username': 'testuser',
        'password': 'testpass123'
    })
    assert response.status_code == 200
    assert 'token' in response.json
    assert response.json['message'] == 'Login successful'
    
    token = response.json['token']
    decoded = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
    assert decoded['user'] == 'testuser'

def test_login_invalid_credentials(client):
    client.post('/register', json={
        'username': 'testuser',
        'password': 'testpass123'
    })
    
    response = client.post('/login', json={
        'username': 'testuser',
        'password': 'wrongpass'
    })
    assert response.status_code == 401
    assert 'Invalid credentials' in response.json['message']

def test_login_nonexistent_user(client):
    response = client.post('/login', json={
        'username': 'nonexistent',
        'password': 'testpass123'
    })
    assert response.status_code == 401
    assert 'Invalid credentials' in response.json['message']

def test_login_missing_fields(client):
    response = client.post('/login', json={'username': 'testuser'})
    assert response.status_code == 400
    assert 'required' in response.json['message'].lower()

def test_protected_endpoint_with_valid_token(client):
    client.post('/register', json={
        'username': 'testuser',
        'password': 'testpass123'
    })
    
    login_response = client.post('/login', json={
        'username': 'testuser',
        'password': 'testpass123'
    })
    token = login_response.json['token']
    
    response = client.get('/protected', headers={
        'Authorization': f'Bearer {token}'
    })
    assert response.status_code == 200
    assert response.json['user'] == 'testuser'
    assert 'Hello testuser' in response.json['message']

def test_protected_endpoint_without_token(client):
    response = client.get('/protected')
    assert response.status_code == 401
    assert 'missing' in response.json['message'].lower()

def test_protected_endpoint_with_invalid_token(client):
    response = client.get('/protected', headers={
        'Authorization': 'Bearer invalid.token.here'
    })
    assert response.status_code == 401
    assert 'invalid' in response.json['message'].lower()

def test_protected_endpoint_with_expired_token(client):
    client.post('/register', json={
        'username': 'testuser',
        'password': 'testpass123'
    })
    
    expired_token = jwt.encode(
        {
            'user': 'testuser',
            'exp': datetime.utcnow() - timedelta(hours=1)
        },
        app.config['SECRET_KEY'],
        algorithm='HS256'
    )
    
    response = client.get('/protected', headers={
        'Authorization': f'Bearer {expired_token}'
    })
    assert response.status_code == 401
    assert 'expired' in response.json['message'].lower()

def test_jwt_token_structure(client):
    client.post('/register', json={
        'username': 'testuser',
        'password': 'testpass123'
    })
    
    response = client.post('/login', json={
        'username': 'testuser',
        'password': 'testpass123'
    })
    
    token = response.json['token']
    decoded = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
    
    assert 'user' in decoded
    assert 'exp' in decoded
    assert decoded['user'] == 'testuser'

def test_password_hashing():
    password = 'testpass123'
    hashed = hash_password(password)
    
    assert hashed != password
    assert len(hashed) > 50
