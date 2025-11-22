from flask import Blueprint, request, jsonify
from config.db import db
from controllers.fine_controller import FineController
from domain.fine import Fine

fine_bp = Blueprint('fines', __name__, url_prefix='/api/fines')


@fine_bp.route('/', methods=['GET'])
def get_all_fines():
    """
    GET /api/fines - Get all fines
    """
    controller = FineController(db.session)
    fines = controller.find_all()
    return jsonify([fine.to_dict() for fine in fines]), 200

@fine_bp.route('/<int:fine_id>', methods=['GET'])
def get_fine(fine_id):
    """
    GET /api/fines/<id> - Get a fine by ID
    """
    controller = FineController(db.session)
    fine = controller.find_by_id(fine_id)
    if fine:
        return jsonify(fine.to_dict()), 200
    return jsonify({'error': 'Fine not found'}), 404


@fine_bp.route('/', methods=['POST'])
def create_fine():
    """
    POST /api/fines - Create a new fine
    Expected JSON body:
    {
        "status": "paid|unpaid|disputed|waived",
        "amount": decimal,
        "currency": "USD|EUR|UAH",
        "violation": "string"
    }
    """
    data = request.get_json()

    required_fields = ['status', 'amount', 'currency', 'violation']
    if not data or not all(field in data for field in required_fields):
        return jsonify({'error': f'Missing required fields: {", ".join(required_fields)}'}), 400

    controller = FineController(db.session)

    new_fine = Fine(
        status=data['status'],
        amount=data['amount'],
        currency=data['currency'],
        violation=data['violation']
    )

    created_fine = controller.create(new_fine)
    return jsonify(created_fine.to_dict()), 201


@fine_bp.route('/<int:fine_id>', methods=['PUT'])
def update_fine(fine_id):
    """
    PUT /api/fines/<id> - Update a fine
    """
    data = request.get_json()

    if not data:
        return jsonify({'error': 'No data provided'}), 400

    controller = FineController(db.session)
    fine = controller.find_by_id(fine_id)

    if not fine:
        return jsonify({'error': 'Fine not found'}), 404

    controller.update(fine_id, data)
    updated_fine = controller.find_by_id(fine_id)
    return jsonify(updated_fine.to_dict()), 200


@fine_bp.route('/<int:fine_id>', methods=['DELETE'])
def delete_fine(fine_id):
    """
    DELETE /api/fines/<id> - Delete a fine
    """
    controller = FineController(db.session)
    fine = controller.find_by_id(fine_id)

    if not fine:
        return jsonify({'error': 'Fine not found'}), 404

    controller.delete(fine_id)
    return jsonify({'message': 'Fine deleted successfully'}), 200


@fine_bp.route('/<int:fine_id>/payments', methods=['GET'])
def get_fine_payments(fine_id):
    controller = FineController(db.session)
    fine = controller.find_by_id(fine_id)

    if not fine:
        return jsonify({'error': 'Fine not found'}), 404

    payments = controller.find_payments(fine_id)
    return jsonify([payment.to_dict() for payment in payments]), 200
