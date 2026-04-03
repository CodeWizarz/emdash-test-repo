import jwt
from datetime import datetime, timedelta, UTC
from flask import Flask, request, jsonify
from werkzeug.security import check_password_hash, generate_password_hash
from functools import wraps

app = Flask(__name__)
app.config['SECRET_KEY'] = 'dev-secret-key-change-in-production'

users_db = {
    'admin': generate_password_hash('admin123'),
    'user': generate_password_hash('user123')
}

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('Authorization')
        
        if not token:
            return jsonify({'message': 'Token is missing'}), 401
        
        if token.startswith('Bearer '):
            token = token[7:]
        
        try:
            jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            return jsonify({'message': 'Token has expired'}), 401
        except jwt.InvalidTokenError:
            return jsonify({'message': 'Invalid token'}), 401
        
        return f(*args, **kwargs)
    
    return decorated

@app.route('/api/login', methods=['POST'])
def login():
    data = request.get_json()
    
    if not data or not data.get('username') or not data.get('password'):
        return jsonify({'message': 'Missing username or password'}), 400
    
    username = data.get('username')
    password = data.get('password')
    
    if username not in users_db:
        return jsonify({'message': 'Invalid credentials'}), 401
    
    if not check_password_hash(users_db[username], password):
        return jsonify({'message': 'Invalid credentials'}), 401
    
    token = jwt.encode({
        'user': username,
        'exp': datetime.now(UTC) + timedelta(hours=24)
    }, app.config['SECRET_KEY'], algorithm='HS256')
    
    return jsonify({'token': token}), 200

@app.route('/api/protected', methods=['GET'])
@token_required
def protected():
    return jsonify({'message': 'Access granted to protected resource'}), 200

@app.route('/api/health', methods=['GET'])
def health():
    return jsonify({'status': 'healthy'}), 200

if __name__ == '__main__':
    app.run(debug=True, port=5000)
