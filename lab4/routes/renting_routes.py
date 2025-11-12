from flask import Blueprint, request, jsonify
from config.db import SessionLocal
from controllers.renting_controller import RentingController
from domain.renting import Renting

renting_bp = Blueprint('rentings', __name__, url_prefix='/api/rentings')


@renting_bp.route('/', methods=['GET'])
def get_all_rentings():
    """
    GET /api/rentings - Get all rentings
    Query parameters:
    - nested: if 'true', includes nested user, vehicle, fines, and payments
    """
    controller = RentingController(SessionLocal())
    include_nested = request.args.get('nested', 'false').lower() == 'true'

    if include_nested:
        rentings = controller.find_all_with_nested()
        return jsonify([renting.to_dict(include_nested=True) for renting in rentings]), 200
    else:
        rentings = controller.find_all()
        return jsonify([renting.to_dict() for renting in rentings]), 200


@renting_bp.route('/active', methods=['GET'])
def get_active_rentings():
    """
    GET /api/rentings/active - Get all active rentings
    Query parameters:
    - nested: if 'true', includes nested user, vehicle, fines, and payments
    """
    controller = RentingController(SessionLocal())
    include_nested = request.args.get('nested', 'false').lower() == 'true'

    if include_nested:
        rentings = controller.find_active_rentings_with_nested()
        return jsonify([renting.to_dict(include_nested=True) for renting in rentings]), 200
    else:
        rentings = controller.find_active_rentings()
        return jsonify([renting.to_dict() for renting in rentings]), 200


@renting_bp.route('/<int:renting_id>', methods=['GET'])
def get_renting(renting_id):
    """
    GET /api/rentings/<id> - Get a renting by ID
    Query parameters:
    - nested: if 'true', includes nested user, vehicle, fines, and payments
    """
    controller = RentingController(SessionLocal())
    include_nested = request.args.get('nested', 'false').lower() == 'true'

    if include_nested:
        renting = controller.find_by_id_with_nested(renting_id)
    else:
        renting = controller.find_by_id(renting_id)

    if renting:
        return jsonify(renting.to_dict(include_nested=include_nested)), 200
    return jsonify({'error': 'Renting not found'}), 404


@renting_bp.route('/', methods=['POST'])
def create_renting():
    """
    POST /api/rentings - Create a new renting
    Expected JSON body:
    {
        "user_id": integer,
        "vehicle_id": integer,
        "start_at": "YYYY-MM-DD HH:MM:SS",
        "end_at": "YYYY-MM-DD HH:MM:SS" (optional)
    }
    """
    data = request.get_json()

    required_fields = ['user_id', 'vehicle_id', 'start_at']
    if not data or not all(field in data for field in required_fields):
        return jsonify({'error': f'Missing required fields: {", ".join(required_fields)}'}), 400

    controller = RentingController(SessionLocal())

    # Create new renting
    new_renting = Renting(
        user_id=data['user_id'],
        vehicle_id=data['vehicle_id'],
        start_at=data['start_at'],
        end_at=data.get('end_at')
    )

    created_renting = controller.create(new_renting)
    return jsonify(created_renting.to_dict()), 201


@renting_bp.route('/<int:renting_id>', methods=['PUT'])
def update_renting(renting_id):
    """
    PUT /api/rentings/<id> - Update a renting
    """
    data = request.get_json()

    if not data:
        return jsonify({'error': 'No data provided'}), 400

    controller = RentingController(SessionLocal())
    renting = controller.find_by_id(renting_id)

    if not renting:
        return jsonify({'error': 'Renting not found'}), 404

    # Update renting
    controller.update(renting_id, data)

    # Fetch updated renting
    updated_renting = controller.find_by_id(renting_id)
    return jsonify(updated_renting.to_dict()), 200


@renting_bp.route('/<int:renting_id>', methods=['DELETE'])
def delete_renting(renting_id):
    """
    DELETE /api/rentings/<id> - Delete a renting
    """
    controller = RentingController(SessionLocal())
    renting = controller.find_by_id(renting_id)

    if not renting:
        return jsonify({'error': 'Renting not found'}), 404

    controller.delete(renting_id)
    return jsonify({'message': 'Renting deleted successfully'}), 200


@renting_bp.route('/<int:renting_id>/fines', methods=['GET'])
def get_renting_fines(renting_id):
    controller = RentingController(SessionLocal())
    renting = controller.find_by_id(renting_id)

    if not renting:
        return jsonify({'error': 'Renting not found'}), 404

    fines = controller.find_fines(renting_id)
    return jsonify([fine.to_dict() for fine in fines]), 200


@renting_bp.route('/<int:renting_id>/payments', methods=['GET'])
def get_renting_payments(renting_id):
    controller = RentingController(SessionLocal())
    renting = controller.find_by_id(renting_id)

    if not renting:
        return jsonify({'error': 'Renting not found'}), 404

    payments = controller.find_payments(renting_id)
    return jsonify([payment.to_dict() for payment in payments]), 200
