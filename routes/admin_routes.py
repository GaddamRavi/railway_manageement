from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from services.auth_service import admin_api_key_required

admin_routes = Blueprint('admin_routes', __name__)

@admin_routes.route('/add-train', methods=['POST'])
@admin_api_key_required
def add_train():
    data = request.get_json()
    # Logic to add train
    return jsonify({"message": "Train added successfully"})
