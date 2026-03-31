import pytest
import json
import jwt
from api import app, users_db


@pytest.fixture
def client():
    """Create a test client"""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_health_endpoint(client):
    """Test health check endpoint"""
    response = client.get('/api/health')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['status'] == 'healthy'


def test_login_success(client):
    """Test successful login"""
    response = client.post('/api/login',
                          json={'username': 'admin', 'password': 'admin123'},
                          content_type='application/json')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert 'token' in data
    assert data['username'] == 'admin'
    assert data['role'] == 'admin'
    assert data['expires_in'] == 86400


def test_login_invalid_credentials(client):
    """Test login with invalid credentials"""
    response = client.post('/api/login',
                          json={'username': 'admin', 'password': 'wrongpassword'},
                          content_type='application/json')
    assert response.status_code == 401
    data = json.loads(response.data)
    assert data['message'] == 'Invalid credentials'


def test_login_missing_username(client):
    """Test login with missing username"""
    response = client.post('/api/login',
                          json={'password': 'admin123'},
                          content_type='application/json')
    assert response.status_code == 400
    data = json.loads(response.data)
    assert data['message'] == 'Missing username or password'


def test_login_missing_password(client):
    """Test login with missing password"""
    response = client.post('/api/login',
                          json={'username': 'admin'},
                          content_type='application/json')
    assert response.status_code == 400
    data = json.loads(response.data)
    assert data['message'] == 'Missing username or password'


def test_login_nonexistent_user(client):
    """Test login with non-existent user"""
    response = client.post('/api/login',
                          json={'username': 'nonexistent', 'password': 'password'},
                          content_type='application/json')
    assert response.status_code == 401
    data = json.loads(response.data)
    assert data['message'] == 'Invalid credentials'


def test_protected_endpoint_with_valid_token(client):
    """Test protected endpoint with valid token"""
    # First login to get token
    login_response = client.post('/api/login',
                                 json={'username': 'user', 'password': 'user123'},
                                 content_type='application/json')
    token = json.loads(login_response.data)['token']
    
    # Access protected endpoint
    response = client.get('/api/protected',
                         headers={'Authorization': f'Bearer {token}'})
    assert response.status_code == 200
    data = json.loads(response.data)
    assert 'Hello user' in data['message']
    assert data['user'] == 'user'


def test_protected_endpoint_without_token(client):
    """Test protected endpoint without token"""
    response = client.get('/api/protected')
    assert response.status_code == 401
    data = json.loads(response.data)
    assert data['message'] == 'Token is missing'


def test_protected_endpoint_with_invalid_token(client):
    """Test protected endpoint with invalid token"""
    response = client.get('/api/protected',
                         headers={'Authorization': 'Bearer invalid_token'})
    assert response.status_code == 401
    data = json.loads(response.data)
    assert data['message'] == 'Invalid token'


def test_protected_endpoint_with_expired_token(client):
    """Test protected endpoint with expired token"""
    import datetime
    
    # Create an expired token
    expired_token = jwt.encode({
        'username': 'user',
        'role': 'user',
        'exp': datetime.datetime.utcnow() - datetime.timedelta(hours=1)
    }, app.config['SECRET_KEY'], algorithm='HS256')
    
    response = client.get('/api/protected',
                         headers={'Authorization': f'Bearer {expired_token}'})
    assert response.status_code == 401
    data = json.loads(response.data)
    assert data['message'] == 'Token has expired'


def test_token_contains_correct_claims(client):
    """Test that token contains correct claims"""
    response = client.post('/api/login',
                          json={'username': 'admin', 'password': 'admin123'},
                          content_type='application/json')
    token = json.loads(response.data)['token']
    
    # Decode and verify token
    decoded = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
    assert decoded['username'] == 'admin'
    assert decoded['role'] == 'admin'
    assert 'exp' in decoded
