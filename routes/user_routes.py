from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from services.auth_service import authenticate_user

user_routes = Blueprint('user_routes', __name__)

@user_routes.route('/register', methods=['POST'])
def register():
     
    return jsonify({"message": "User registered successfully"})

@user_routes.route('/login', methods=['POST'])
def login():
     
    pass
