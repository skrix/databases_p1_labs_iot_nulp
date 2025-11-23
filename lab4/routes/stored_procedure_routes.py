from flask import Blueprint, request, jsonify
from config.db import db
from controllers.stored_procedure_controller import StoredProcedureController

stored_procedure_bp = Blueprint('stored_procedures', __name__, url_prefix='/api/stored-procedures')


@stored_procedure_bp.route('/generic-insert', methods=['POST'])
def generic_insert():
    """
    POST /api/stored-procedures/generic-insert - Execute generic_insert stored procedure
    Expected JSON body:
    {
        "table": "table_name",
        "columns": "col1, col2, col3",
        "values": "'val1', 'val2', 'val3'"
    }
    """
    data = request.get_json()

    required_fields = ['table', 'columns', 'values']
    if not data or not all(field in data for field in required_fields):
        return jsonify({'error': f'Missing required fields: {", ".join(required_fields)}'}), 400

    controller = StoredProcedureController(db.session)

    try:
        controller.generic_insert(
            table=data['table'],
            columns=data['columns'],
            values=data['values']
        )
        return jsonify({'message': 'Insert successful'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400
