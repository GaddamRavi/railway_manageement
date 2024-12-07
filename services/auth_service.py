from flask_jwt_extended import create_access_token
from werkzeug.security import generate_password_hash, check_password_hash
from utils.db import db
from flask import request, jsonify

def admin_api_key_required(func):
    def wrapper(*args, **kwargs):
        api_key = request.headers.get('x-api-key')
        if not api_key or api_key != os.getenv('ADMIN_API_KEY'):
            return jsonify({"message": "Unauthorized: Invalid API Key"}), 401
        return func(*args, **kwargs)
    wrapper.__name__ = func.__name__  # Preserve original function name
    return wrapper

def authenticate_user(username, password):
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM users WHERE username=%s", (username,))
    user = cursor.fetchone()
    if user and check_password_hash(user['password_hash'], password):
        return create_access_token(identity=user['id'])
    return None

def register_user(username, password, role='user'):
    password_hash = generate_password_hash(password)
    cursor = db.cursor()
    try:
        cursor.execute("INSERT INTO users (username, password_hash, role) VALUES (%s, %s, %s)", 
                       (username, password_hash, role))
        db.commit()
        return True
    except Exception as e:
        db.rollback()
        return False
