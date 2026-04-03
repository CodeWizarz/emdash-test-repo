"""
API Server for Acme AI Labs Orchestration System
Provides endpoints for system status and control
"""
from flask import Flask, jsonify, request
import os
import jwt
from datetime import datetime, timedelta

app = Flask(__name__)

# JWT Configuration
SECRET_KEY = os.environ.get('JWT_SECRET_KEY', 'dev-secret-key-change-in-production')

# Mock user database (in production, use real database)
USERS = {
    'admin': 'admin123',
    'user': 'user123'
}

@app.route('/health', methods=['GET'])
def health():
    """Health check endpoint"""
    return jsonify({'status': 'running', 'message': 'API server is healthy'})

@app.route('/api/status', methods=['GET'])
def status():
    """Get orchestration system status"""
    return jsonify({
        'status': 'active',
        'service': 'Acme AI Labs Orchestration',
        'version': '0.1.0'
    })

@app.route('/api/stop', methods=['POST'])
def stop():
    """Endpoint to signal server shutdown"""
    return jsonify({'status': 'stopping', 'message': 'Shutdown signal received'})

@app.route('/api/login', methods=['POST'])
def login():
    """JWT login endpoint"""
    if not request.json:
        return jsonify({'error': 'Request must be JSON'}), 400
    
    username = request.json.get('username')
    password = request.json.get('password')
    
    if not username or not password:
        return jsonify({'error': 'Username and password required'}), 400
    
    # Validate credentials
    if username not in USERS or USERS[username] != password:
        return jsonify({'error': 'Invalid credentials'}), 401
    
    # Generate JWT token
    try:
        payload = {
            'username': username,
            'exp': datetime.utcnow() + timedelta(hours=24),
            'iat': datetime.utcnow()
        }
        token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
        
        return jsonify({
            'success': True,
            'token': token,
            'username': username,
            'expires_in': 86400  # 24 hours in seconds
        }), 200
    except Exception as e:
        return jsonify({'error': f'Token generation failed: {str(e)}'}), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
