"""
API Manager for controlling the orchestration API server
"""
import subprocess
import requests
import time
import signal
import os

class APIManager:
    def __init__(self, port=5000):
        self.port = port
        self.process = None
        self.base_url = f"http://localhost:{port}"
    
    def start(self):
        """Start the API server"""
        if self.is_running():
            return {'success': False, 'message': 'API server already running'}
        
        try:
            self.process = subprocess.Popen(
                ['python', 'api_server.py'],
                env={**os.environ, 'PORT': str(self.port)},
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE
            )
            
            # Wait for server to be ready
            max_retries = 10
            for _ in range(max_retries):
                time.sleep(0.5)
                if self.is_running():
                    return {'success': True, 'message': f'API server started on port {self.port}'}
            
            return {'success': False, 'message': 'API server failed to start'}
        except Exception as e:
            return {'success': False, 'message': f'Error starting server: {str(e)}'}
    
    def stop(self):
        """Stop the API server"""
        if not self.is_running():
            return {'success': False, 'message': 'API server not running'}
        
        try:
            # Try graceful shutdown via API
            requests.post(f"{self.base_url}/api/stop", timeout=2)
            time.sleep(1)
        except:
            pass
        
        # Force kill if still running
        if self.process:
            try:
                self.process.terminate()
                self.process.wait(timeout=5)
            except:
                self.process.kill()
            self.process = None
        
        return {'success': True, 'message': 'API server stopped'}
    
    def is_running(self):
        """Check if API server is running"""
        try:
            response = requests.get(f"{self.base_url}/health", timeout=1)
            return response.status_code == 200
        except:
            return False
    
    def get_status(self):
        """Get current status of API server"""
        if self.is_running():
            try:
                response = requests.get(f"{self.base_url}/api/status", timeout=2)
                return response.json()
            except:
                return {'status': 'running', 'message': 'Connected but status unavailable'}
        return {'status': 'stopped', 'message': 'API server not running'}

if __name__ == '__main__':
    manager = APIManager()
    print("API Manager CLI")
    print("Commands: start, stop, status, quit")
    
    while True:
        cmd = input("\n> ").strip().lower()
        if cmd == 'start':
            result = manager.start()
            print(result['message'])
        elif cmd == 'stop':
            result = manager.stop()
            print(result['message'])
        elif cmd == 'status':
            status = manager.get_status()
            print(f"Status: {status}")
        elif cmd == 'quit':
            if manager.is_running():
                manager.stop()
            break
        else:
            print("Unknown command")
