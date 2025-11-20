from flask import Blueprint, request, jsonify
from config.db import SessionLocal
from controllers.vehicle_controller import VehicleController
from domain.vehicle import Vehicle

vehicle_bp = Blueprint('vehicles', __name__, url_prefix='/api/vehicles')


@vehicle_bp.route('/', methods=['GET'])
def get_all_vehicles():
    """
    GET /api/vehicles - Get all vehicles
    Query parameters:
    - nested: if 'true', includes nested rentings and parkings
    """
    controller = VehicleController(SessionLocal())
    include_nested = request.args.get('nested', 'false').lower() == 'true'

    if include_nested:
        vehicles = controller.find_all_with_nested()
        return jsonify([vehicle.to_dict(include_nested=True) for vehicle in vehicles]), 200
    else:
        vehicles = controller.find_all()
        return jsonify([vehicle.to_dict() for vehicle in vehicles]), 200


@vehicle_bp.route('/<int:vehicle_id>', methods=['GET'])
def get_vehicle(vehicle_id):
    """
    GET /api/vehicles/<id> - Get a vehicle by ID
    Query parameters:
    - nested: if 'true', includes nested rentings and parkings
    """
    controller = VehicleController(SessionLocal())
    include_nested = request.args.get('nested', 'false').lower() == 'true'

    if include_nested:
        vehicle = controller.find_by_id_with_nested(vehicle_id)
    else:
        vehicle = controller.find_by_id(vehicle_id)

    if vehicle:
        return jsonify(vehicle.to_dict(include_nested=include_nested)), 200
    return jsonify({'error': 'Vehicle not found'}), 404


@vehicle_bp.route('/', methods=['POST'])
def create_vehicle():
    """
    POST /api/vehicles - Create a new vehicle
    Expected JSON body:
    {
        "make": "string",
        "model": "string",
        "year": integer,
        "vin": "string",
        "body": "sedan|hatchback|wagon|...",
        "plate": "string"
    }
    """
    data = request.get_json()

    required_fields = ['make', 'model', 'year', 'vin', 'body', 'plate']
    if not data or not all(field in data for field in required_fields):
        return jsonify({'error': f'Missing required fields: {", ".join(required_fields)}'}), 400

    controller = VehicleController(SessionLocal())

    # Check if VIN or plate already exists
    if controller.find_by_vin(data['vin']):
        return jsonify({'error': 'VIN already exists'}), 400

    if controller.find_by_plate(data['plate']):
        return jsonify({'error': 'License plate already exists'}), 400

    new_vehicle = Vehicle(
        make=data['make'],
        model=data['model'],
        year=data['year'],
        vin=data['vin'],
        body=data['body'],
        plate=data['plate']
    )

    created_vehicle = controller.create(new_vehicle)
    return jsonify(created_vehicle.to_dict()), 201


@vehicle_bp.route('/<int:vehicle_id>', methods=['PUT'])
def update_vehicle(vehicle_id):
    """
    PUT /api/vehicles/<id> - Update a vehicle
    """
    data = request.get_json()

    if not data:
        return jsonify({'error': 'No data provided'}), 400

    controller = VehicleController(SessionLocal())
    vehicle = controller.find_by_id(vehicle_id)

    if not vehicle:
        return jsonify({'error': 'Vehicle not found'}), 404

    # Check for duplicate VIN/plate if they're being changed
    if 'vin' in data and data['vin'] != vehicle.vin:
        existing_vehicle = controller.find_by_vin(data['vin'])
        if existing_vehicle:
            return jsonify({'error': 'VIN already exists'}), 400

    if 'plate' in data and data['plate'] != vehicle.plate:
        existing_vehicle = controller.find_by_plate(data['plate'])
        if existing_vehicle:
            return jsonify({'error': 'License plate already exists'}), 400

    controller.update(vehicle_id, data)
    updated_vehicle = controller.find_by_id(vehicle_id)
    return jsonify(updated_vehicle.to_dict()), 200


@vehicle_bp.route('/<int:vehicle_id>', methods=['DELETE'])
def delete_vehicle(vehicle_id):
    """
    DELETE /api/vehicles/<id> - Delete a vehicle
    """
    controller = VehicleController(SessionLocal())
    vehicle = controller.find_by_id(vehicle_id)

    if not vehicle:
        return jsonify({'error': 'Vehicle not found'}), 404

    controller.delete(vehicle_id)
    return jsonify({'message': 'Vehicle deleted successfully'}), 200


@vehicle_bp.route('/<int:vehicle_id>/rentings', methods=['GET'])
def get_vehicle_rentings(vehicle_id):
    controller = VehicleController(SessionLocal())
    vehicle = controller.find_by_id(vehicle_id)

    if not vehicle:
        return jsonify({'error': 'Vehicle not found'}), 404

    rentings = controller.find_rentings(vehicle_id)
    return jsonify([renting.to_dict() for renting in rentings]), 200


@vehicle_bp.route('/<int:vehicle_id>/parkings', methods=['GET'])
def get_vehicle_parkings(vehicle_id):
    controller = VehicleController(SessionLocal())
    vehicle = controller.find_by_id(vehicle_id)

    if not vehicle:
        return jsonify({'error': 'Vehicle not found'}), 404

    parkings = controller.find_parkings(vehicle_id)
    return jsonify([parking.to_dict() for parking in parkings]), 200
