"""
API Server for Acme AI Labs Orchestration System
Provides endpoints for system status and control
"""
from flask import Flask, jsonify
import os

app = Flask(__name__)

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

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
