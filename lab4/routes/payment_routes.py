from flask import Blueprint, request, jsonify
from config.db import SessionLocal
from controllers.payment_controller import PaymentController
from domain.payment import Payment

payment_bp = Blueprint('payments', __name__, url_prefix='/api/payments')


@payment_bp.route('/', methods=['GET'])
def get_all_payments():
    """
    GET /api/payments - Get all payments
    """
    controller = PaymentController(SessionLocal())
    payments = controller.find_all()
    return jsonify([payment.to_dict() for payment in payments]), 200


@payment_bp.route('/<int:payment_id>', methods=['GET'])
def get_payment(payment_id):
    """
    GET /api/payments/<id> - Get a payment by ID
    """
    controller = PaymentController(SessionLocal())
    payment = controller.find_by_id(payment_id)
    if payment:
        return jsonify(payment.to_dict()), 200
    return jsonify({'error': 'Payment not found'}), 404


@payment_bp.route('/', methods=['POST'])
def create_payment():
    """
    POST /api/payments - Create a new payment
    Expected JSON body:
    {
        "status": "pending|paid|failed|refunded",
        "amount": decimal,
        "currency": "USD|EUR|UAH"
    }
    """
    data = request.get_json()

    required_fields = ['status', 'amount', 'currency']
    if not data or not all(field in data for field in required_fields):
        return jsonify({'error': f'Missing required fields: {", ".join(required_fields)}'}), 400

    controller = PaymentController(SessionLocal())
    new_payment = Payment(
        status=data['status'],
        amount=data['amount'],
        currency=data['currency']
    )

    created_payment = controller.create(new_payment)
    return jsonify(created_payment.to_dict()), 201


@payment_bp.route('/<int:payment_id>', methods=['PUT'])
def update_payment(payment_id):
    """
    PUT /api/payments/<id> - Update a payment
    """
    data = request.get_json()

    if not data:
        return jsonify({'error': 'No data provided'}), 400

    controller = PaymentController(SessionLocal())
    payment = controller.find_by_id(payment_id)

    if not payment:
        return jsonify({'error': 'Payment not found'}), 404

    controller.update(payment_id, data)
    updated_payment = controller.find_by_id(payment_id)
    return jsonify(updated_payment.to_dict()), 200


@payment_bp.route('/<int:payment_id>', methods=['DELETE'])
def delete_payment(payment_id):
    """
    DELETE /api/payments/<id> - Delete a payment
    """
    controller = PaymentController(SessionLocal())
    payment = controller.find_by_id(payment_id)

    if not payment:
        return jsonify({'error': 'Payment not found'}), 404

    controller.delete(payment_id)
    return jsonify({'message': 'Payment deleted successfully'}), 200
