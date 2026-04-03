"""
Tests for API Server and Manager
"""
import unittest
import time
import requests
import jwt
from api_manager import APIManager

class TestAPISystem(unittest.TestCase):
    
    def setUp(self):
        """Set up test fixtures"""
        self.manager = APIManager(port=5001)  # Use different port for testing
        
    def tearDown(self):
        """Clean up after tests"""
        if self.manager.is_running():
            self.manager.stop()
    
    def test_api_manager_start(self):
        """Test starting the API server"""
        result = self.manager.start()
        self.assertTrue(result['success'], "API should start successfully")
        self.assertTrue(self.manager.is_running(), "API should be running")
    
    def test_api_manager_stop(self):
        """Test stopping the API server"""
        self.manager.start()
        time.sleep(1)
        
        result = self.manager.stop()
        self.assertTrue(result['success'], "API should stop successfully")
        self.assertFalse(self.manager.is_running(), "API should not be running")
    
    def test_api_manager_double_start(self):
        """Test that starting an already running server fails gracefully"""
        self.manager.start()
        time.sleep(1)
        
        result = self.manager.start()
        self.assertFalse(result['success'], "Second start should fail")
    
    def test_api_manager_status(self):
        """Test getting API status"""
        # When stopped
        status = self.manager.get_status()
        self.assertEqual(status['status'], 'stopped')
        
        # When running
        self.manager.start()
        time.sleep(1)
        status = self.manager.get_status()
        self.assertIn(status['status'], ['running', 'active'])
    
    def test_health_endpoint(self):
        """Test the health check endpoint"""
        self.manager.start()
        time.sleep(1)
        
        response = requests.get('http://localhost:5001/health')
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data['status'], 'running')
    
    def test_status_endpoint(self):
        """Test the status endpoint"""
        self.manager.start()
        time.sleep(1)
        
        response = requests.get('http://localhost:5001/api/status')
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIn('status', data)
        self.assertIn('service', data)
        self.assertIn('version', data)
    
    def test_login_endpoint_success(self):
        """Test successful JWT login"""
        self.manager.start()
        time.sleep(1)
        
        response = requests.post('http://localhost:5001/api/login', json={
            'username': 'admin',
            'password': 'admin123'
        })
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertTrue(data['success'])
        self.assertIn('token', data)
        self.assertEqual(data['username'], 'admin')
        self.assertIn('expires_in', data)
        
        # Verify token is valid JWT
        token = data['token']
        SECRET_KEY = 'dev-secret-key-change-in-production'
        decoded = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        self.assertEqual(decoded['username'], 'admin')
    
    def test_login_endpoint_invalid_credentials(self):
        """Test login with invalid credentials"""
        self.manager.start()
        time.sleep(1)
        
        response = requests.post('http://localhost:5001/api/login', json={
            'username': 'admin',
            'password': 'wrongpassword'
        })
        self.assertEqual(response.status_code, 401)
        data = response.json()
        self.assertIn('error', data)
    
    def test_login_endpoint_missing_username(self):
        """Test login with missing username"""
        self.manager.start()
        time.sleep(1)
        
        response = requests.post('http://localhost:5001/api/login', json={
            'password': 'admin123'
        })
        self.assertEqual(response.status_code, 400)
        data = response.json()
        self.assertIn('error', data)
    
    def test_login_endpoint_missing_password(self):
        """Test login with missing password"""
        self.manager.start()
        time.sleep(1)
        
        response = requests.post('http://localhost:5001/api/login', json={
            'username': 'admin'
        })
        self.assertEqual(response.status_code, 400)
        data = response.json()
        self.assertIn('error', data)
    
    def test_login_endpoint_not_json(self):
        """Test login with non-JSON request"""
        self.manager.start()
        time.sleep(1)
        
        response = requests.post('http://localhost:5001/api/login', data='not json')
        # Flask returns 415 for non-JSON content type
        self.assertIn(response.status_code, [400, 415])
        # Response may not be JSON when content-type is wrong
    
    def test_login_endpoint_nonexistent_user(self):
        """Test login with nonexistent user"""
        self.manager.start()
        time.sleep(1)
        
        response = requests.post('http://localhost:5001/api/login', json={
            'username': 'nonexistent',
            'password': 'password'
        })
        self.assertEqual(response.status_code, 401)
        data = response.json()
        self.assertIn('error', data)

if __name__ == '__main__':
    unittest.main()
