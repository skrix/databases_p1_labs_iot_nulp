from flask import Blueprint, request, jsonify
from config.db import db
from controllers.user_note_controller import UserNoteController
from domain.user_note import UserNote

user_note_bp = Blueprint('user_notes', __name__, url_prefix='/api/user-notes')


@user_note_bp.route('/', methods=['GET'])
def get_all_user_notes():
    """
    GET /api/user-notes - Get all user notes
    """
    controller = UserNoteController(db.session)
    notes = controller.find_all()
    return jsonify([note.to_dict() for note in notes]), 200


@user_note_bp.route('/<int:note_id>', methods=['GET'])
def get_user_note(note_id):
    """
    GET /api/user-notes/<id> - Get a user note by ID
    """
    controller = UserNoteController(db.session)
    note = controller.find_by_id(note_id)
    if note:
        return jsonify(note.to_dict()), 200
    return jsonify({'error': 'User note not found'}), 404


@user_note_bp.route('/user/<int:user_id>', methods=['GET'])
def get_user_notes_by_user(user_id):
    """
    GET /api/user-notes/user/<user_id> - Get all notes for a user
    """
    controller = UserNoteController(db.session)
    notes = controller.find_by_user_id(user_id)
    return jsonify([note.to_dict() for note in notes]), 200


@user_note_bp.route('/', methods=['POST'])
def create_user_note():
    """
    POST /api/user-notes - Create a new user note
    Expected JSON body:
    {
        "user_id": int,
        "note": "string"
    }
    """
    data = request.get_json()

    required_fields = ['user_id', 'note']
    if not data or not all(field in data for field in required_fields):
        return jsonify({'error': f'Missing required fields: {", ".join(required_fields)}'}), 400

    controller = UserNoteController(db.session)

    new_note = UserNote(
        user_id=data['user_id'],
        note=data['note']
    )

    try:
        created_note = controller.create(new_note)
        return jsonify(created_note.to_dict()), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400


@user_note_bp.route('/<int:note_id>', methods=['PUT'])
def update_user_note(note_id):
    """
    PUT /api/user-notes/<id> - Update a user note
    """
    data = request.get_json()

    if not data:
        return jsonify({'error': 'No data provided'}), 400

    controller = UserNoteController(db.session)
    note = controller.find_by_id(note_id)

    if not note:
        return jsonify({'error': 'User note not found'}), 404

    try:
        controller.update(note_id, data)
        updated_note = controller.find_by_id(note_id)
        return jsonify(updated_note.to_dict()), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400


@user_note_bp.route('/<int:note_id>', methods=['DELETE'])
def delete_user_note(note_id):
    """
    DELETE /api/user-notes/<id> - Delete a user note
    """
    controller = UserNoteController(db.session)
    note = controller.find_by_id(note_id)

    if not note:
        return jsonify({'error': 'User note not found'}), 404

    controller.delete(note_id)
    return jsonify({'message': 'User note deleted successfully'}), 200
