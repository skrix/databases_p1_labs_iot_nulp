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


@stored_procedure_bp.route('/m2m-insert', methods=['POST'])
def m2m_insert():
    """
    POST /api/stored-procedures/m2m-insert - Execute join_insert stored procedure
    Expected JSON body:
    {
        "left_table": "table_name",
        "left_lookup_col": "column_name",
        "left_lookup_val": "value",
        "right_table": "table_name",
        "right_lookup_col": "column_name",
        "right_lookup_val": "value",
        "join_table": "join_table_name",
        "left_fk": "left_fk_column",
        "right_fk": "right_fk_column"
    }
    """
    data = request.get_json()

    required_fields = [
        'left_table', 'left_lookup_col', 'left_lookup_val',
        'right_table', 'right_lookup_col', 'right_lookup_val',
        'join_table', 'left_fk', 'right_fk'
    ]
    if not data or not all(field in data for field in required_fields):
        return jsonify({'error': f'Missing required fields: {", ".join(required_fields)}'}), 400

    controller = StoredProcedureController(db.session)

    try:
        controller.join_insert(
            left_table=data['left_table'],
            left_lookup_col=data['left_lookup_col'],
            left_lookup_val=data['left_lookup_val'],
            right_table=data['right_table'],
            right_lookup_col=data['right_lookup_col'],
            right_lookup_val=data['right_lookup_val'],
            join_table=data['join_table'],
            left_fk=data['left_fk'],
            right_fk=data['right_fk']
        )
        return jsonify({'message': 'M2M relation created successfully'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400


@stored_procedure_bp.route('/noname-insert', methods=['POST'])
def noname_insert():
    """
    POST /api/stored-procedures/noname-insert - Execute noname_insert stored procedure
    Inserts 10 rows with values 'Noname1' through 'Noname10'
    Expected JSON body:
    {
        "table": "table_name",
        "column": "column_name"
    }
    """
    data = request.get_json()

    required_fields = ['table', 'column']
    if not data or not all(field in data for field in required_fields):
        return jsonify({'error': f'Missing required fields: {", ".join(required_fields)}'}), 400

    controller = StoredProcedureController(db.session)

    try:
        controller.noname_insert(
            table=data['table'],
            column=data['column']
        )
        return jsonify({'message': '10 Noname rows inserted successfully'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400


@stored_procedure_bp.route('/get-stat', methods=['POST'])
def get_stat():
    """
    POST /api/stored-procedures/get-stat - Execute get_stat stored procedure
    Calculates statistics (SUM, AVG, COUNT, MIN, MAX) on a column
    Expected JSON body:
    {
        "table": "table_name",
        "column": "column_name",
        "stat_type": "SUM|AVG|COUNT|MIN|MAX"
    }
    """
    data = request.get_json()

    required_fields = ['table', 'column', 'stat_type']
    if not data or not all(field in data for field in required_fields):
        return jsonify({'error': f'Missing required fields: {", ".join(required_fields)}'}), 400

    # Validate stat_type
    valid_stats = ['SUM', 'AVG', 'COUNT', 'MIN', 'MAX']
    if data['stat_type'].upper() not in valid_stats:
        return jsonify({'error': f'Invalid stat_type. Must be one of: {", ".join(valid_stats)}'}), 400

    controller = StoredProcedureController(db.session)

    try:
        result = controller.get_stat(
            table=data['table'],
            column=data['column'],
            stat_type=data['stat_type'].upper()
        )
        return jsonify({
            'table': data['table'],
            'column': data['column'],
            'stat_type': data['stat_type'].upper(),
            'result': result
        }), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400


@stored_procedure_bp.route('/split-table', methods=['POST'])
def split_table():
    """
    POST /api/stored-procedures/split-table - Execute split_table_random stored procedure
    Splits a table randomly into two new tables with timestamp suffixes
    Expected JSON body:
    {
        "table": "table_name"
    }
    """
    data = request.get_json()

    required_fields = ['table']
    if not data or not all(field in data for field in required_fields):
        return jsonify({'error': f'Missing required fields: {", ".join(required_fields)}'}), 400

    controller = StoredProcedureController(db.session)

    try:
        controller.split_table_random(table=data['table'])

        # Get timestamp for new table names
        import time
        ts = int(time.time())

        return jsonify({
            'message': 'Table split successfully',
            'original_table': data['table'],
            'new_tables': [
                f"{data['table']}_clone_{ts}_1",
                f"{data['table']}_clone_{ts}_2"
            ]
        }), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400
