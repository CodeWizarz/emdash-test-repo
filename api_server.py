"""
API Server - Flask application with control endpoints
Provides REST API for starting/stopping services and serving UI
"""

from flask import Flask, jsonify, send_from_directory
from flask_cors import CORS
from api_manager import APIManager

app = Flask(__name__, static_folder='static')
CORS(app)

# Global API manager instance
api_manager = APIManager()


@app.route('/')
def index():
    """Serve the main UI"""
    return send_from_directory('static', 'index.html')


@app.route('/api/start', methods=['POST'])
def start_api():
    """Start the API service"""
    try:
        result = api_manager.start()
        if result['success']:
            return jsonify({"status": "started", "message": result['message']}), 200
        else:
            return jsonify({"status": "error", "message": result['message']}), 400
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500


@app.route('/api/stop', methods=['POST'])
def stop_api():
    """Stop the API service"""
    try:
        result = api_manager.stop()
        if result['success']:
            return jsonify({"status": "stopped", "message": result['message']}), 200
        else:
            return jsonify({"status": "error", "message": result['message']}), 400
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500


@app.route('/api/status', methods=['GET'])
def get_status():
    """Get current API status"""
    try:
        status = api_manager.get_status()
        return jsonify(status), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500


if __name__ == '__main__':
    print("🚀 API Control Server starting on http://localhost:5000")
    print("📋 Open http://localhost:5000 in your browser to use the button interface")
    app.run(debug=True, host='0.0.0.0', port=5000)
