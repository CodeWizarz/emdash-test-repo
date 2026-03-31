"""
Tests for API Server and Manager
"""
import unittest
import time
import requests
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

if __name__ == '__main__':
    unittest.main()
