from flask import Blueprint, request, jsonify
from config.db import db
from controllers.parking_controller import ParkingController
from domain.parking import Parking

parking_bp = Blueprint('parkings', __name__, url_prefix='/api/parkings')


@parking_bp.route('/', methods=['GET'])
def get_all_parkings():
    """
    GET /api/parkings - Get all parkings
    """
    controller = ParkingController(db.session)
    parkings = controller.find_all()
    return jsonify([parking.to_dict() for parking in parkings]), 200


@parking_bp.route('/<int:parking_id>', methods=['GET'])
def get_parking(parking_id):
    """
    GET /api/parkings/<id> - Get a parking by ID
    """
    controller = ParkingController(db.session)
    parking = controller.find_by_id(parking_id)
    if parking:
        return jsonify(parking.to_dict()), 200
    return jsonify({'error': 'Parking not found'}), 404


@parking_bp.route('/', methods=['POST'])
def create_parking():
    """
    POST /api/parkings - Create a new parking
    Expected JSON body:
    {
        "address": "string" (optional),
        "country": "string" (optional),
        "city": "string" (optional),
        "latitude": decimal,
        "longitude": decimal
    }
    """
    data = request.get_json()

    required_fields = ['latitude', 'longitude']
    if not data or not all(field in data for field in required_fields):
        return jsonify({'error': f'Missing required fields: {", ".join(required_fields)}'}), 400

    controller = ParkingController(db.session)
    new_parking = Parking(
        address=data.get('address'),
        country=data.get('country'),
        city=data.get('city'),
        latitude=data['latitude'],
        longitude=data['longitude']
    )

    created_parking = controller.create(new_parking)
    return jsonify(created_parking.to_dict()), 201


@parking_bp.route('/<int:parking_id>', methods=['PUT'])
def update_parking(parking_id):
    """
    PUT /api/parkings/<id> - Update a parking
    """
    data = request.get_json()

    if not data:
        return jsonify({'error': 'No data provided'}), 400

    controller = ParkingController(db.session)
    parking = controller.find_by_id(parking_id)

    if not parking:
        return jsonify({'error': 'Parking not found'}), 404

    controller.update(parking_id, data)
    updated_parking = controller.find_by_id(parking_id)
    return jsonify(updated_parking.to_dict()), 200


@parking_bp.route('/<int:parking_id>', methods=['DELETE'])
def delete_parking(parking_id):
    """
    DELETE /api/parkings/<id> - Delete a parking
    """
    controller = ParkingController(db.session)
    parking = controller.find_by_id(parking_id)

    if not parking:
        return jsonify({'error': 'Parking not found'}), 404

    controller.delete(parking_id)
    return jsonify({'message': 'Parking deleted successfully'}), 200


@parking_bp.route('/<int:parking_id>/vehicles', methods=['GET'])
def get_parking_vehicles(parking_id):
    controller = ParkingController(db.session)
    parking = controller.find_by_id(parking_id)

    if not parking:
        return jsonify({'error': 'Parking not found'}), 404

    vehicles = controller.find_vehicles(parking_id)
    return jsonify([vehicle.to_dict() for vehicle in vehicles]), 200
