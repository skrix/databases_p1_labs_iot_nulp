from flask import Blueprint, request, jsonify
from config.db import SessionLocal
from controllers.user_controller import UserController
from domain.user import User

user_bp = Blueprint('users', __name__, url_prefix='/api/users')


@user_bp.route('/', methods=['GET'])
def get_all_users():
    """
    GET /api/users - Get all users
    """
    controller = UserController(SessionLocal())
    users = controller.find_all()
    return jsonify([user.to_dict() for user in users]), 200


@user_bp.route('/<int:user_id>', methods=['GET'])
def get_user(user_id):
    """
    GET /api/users/<id> - Get a user by ID
    """
    controller = UserController(SessionLocal())
    user = controller.find_by_id(user_id)
    if user:
        return jsonify(user.to_dict()), 200
    return jsonify({'error': 'User not found'}), 404


@user_bp.route('/', methods=['POST'])
def create_user():
    """
    POST /api/users - Create a new user
    Expected JSON body:
    {
        "first_name": "string",
        "middle_name": "string" (optional),
        "last_name": "string",
        "dob": "YYYY-MM-DD",
        "email": "string",
        "password": "string",
        "driver_license": "string",
        "gender": "male|female|other|prefer_not_to_say"
    }
    """
    data = request.get_json()

    required_fields = ['first_name', 'last_name', 'dob', 'email', 'password', 'driver_license', 'gender']
    if not data or not all(field in data for field in required_fields):
        return jsonify({'error': f'Missing required fields: {", ".join(required_fields)}'}), 400

    controller = UserController(SessionLocal())

    if controller.find_by_email(data['email']):
        return jsonify({'error': 'Email already exists'}), 400

    if controller.find_by_driver_license(data['driver_license']):
        return jsonify({'error': 'Driver license already exists'}), 400

    new_user = User(
        first_name=data['first_name'],
        middle_name=data.get('middle_name'),
        last_name=data['last_name'],
        dob=data['dob'],
        email=data['email'],
        password=data['password'],
        driver_license=data['driver_license'],
        gender=data['gender']
    )

    created_user = controller.create(new_user)
    return jsonify(created_user.to_dict()), 201


@user_bp.route('/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    """
    PUT /api/users/<id> - Update a user
    Expected JSON body (all optional):
    {
        "first_name": "string",
        "middle_name": "string",
        "last_name": "string",
        "dob": "YYYY-MM-DD",
        "email": "string",
        "password": "string",
        "driver_license": "string",
        "gender": "male|female|other|prefer_not_to_say"
    }
    """
    data = request.get_json()

    if not data:
        return jsonify({'error': 'No data provided'}), 400

    controller = UserController(SessionLocal())
    user = controller.find_by_id(user_id)

    if not user:
        return jsonify({'error': 'User not found'}), 404

    if 'email' in data and data['email'] != user.email:
        existing_user = controller.find_by_email(data['email'])
        if existing_user:
            return jsonify({'error': 'Email already exists'}), 400

    if 'driver_license' in data and data['driver_license'] != user.driver_license:
        existing_user = controller.find_by_driver_license(data['driver_license'])
        if existing_user:
            return jsonify({'error': 'Driver license already exists'}), 400

    controller.update(user_id, data)

    updated_user = controller.find_by_id(user_id)
    return jsonify(updated_user.to_dict()), 200


@user_bp.route('/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    """
    DELETE /api/users/<id> - Delete a user
    """
    controller = UserController(SessionLocal())
    user = controller.find_by_id(user_id)

    if not user:
        return jsonify({'error': 'User not found'}), 404

    controller.delete(user_id)
    return jsonify({'message': 'User deleted successfully'}), 200
