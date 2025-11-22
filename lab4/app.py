import os
import logging
from flask import Flask, jsonify
from flask_migrate import Migrate
from dotenv import load_dotenv
from config.db import db, DATABASE_URL, ECHO_SQL
from routes.user_routes import user_bp
from routes.vehicle_routes import vehicle_bp
from routes.parking_routes import parking_bp
from routes.renting_routes import renting_bp
from routes.payment_routes import payment_bp
from routes.fine_routes import fine_bp
from routes.user_note_routes import user_note_bp

load_dotenv()

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[logging.StreamHandler()]
)
logger = logging.getLogger(__name__)


def create_app():
    app = Flask(__name__)
    app.config['JSON_SORT_KEYS'] = False
    app.config['DEBUG'] = os.getenv('FLASK_DEBUG', 'True').lower() == 'true'
    app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
    app.config['SQLALCHEMY_ECHO'] = ECHO_SQL
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    migrate = Migrate(app, db)

    app.register_blueprint(user_bp)
    app.register_blueprint(vehicle_bp)
    app.register_blueprint(parking_bp)
    app.register_blueprint(renting_bp)
    app.register_blueprint(payment_bp)
    app.register_blueprint(fine_bp)

    @app.teardown_appcontext
    def remove_session(exception=None):
        db.session.remove()

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({'error': 'Resource not found'}), 404

    @app.errorhandler(500)
    def internal_error(error):
        db.session.remove()
        return jsonify({'error': 'Internal server error'}), 500

    @app.errorhandler(Exception)
    def handle_exception(error):
        logger.error(f"Unhandled exception: {str(error)}", exc_info=True)
        db.session.remove()
        return jsonify({'error': str(error)}), 500

    @app.route('/')
    def index():
        return jsonify({
            'message': 'Welcome to Sixt Car Rental API',
            'version': '1.0',
            'endpoints': {
                'users': {
                    'GET /api/users': 'Get all users',
                    'GET /api/users/<id>': 'Get user by ID',
                    'POST /api/users': 'Create a new user',
                    'PUT /api/users/<id>': 'Update a user',
                    'DELETE /api/users/<id>': 'Delete a user'
                },
                'vehicles': {
                    'GET /api/vehicles': 'Get all vehicles',
                    'GET /api/vehicles/<id>': 'Get vehicle by ID',
                    'POST /api/vehicles': 'Create a new vehicle',
                    'PUT /api/vehicles/<id>': 'Update a vehicle',
                    'DELETE /api/vehicles/<id>': 'Delete a vehicle'
                },
                'parkings': {
                    'GET /api/parkings': 'Get all parkings',
                    'GET /api/parkings/<id>': 'Get parking by ID',
                    'POST /api/parkings': 'Create a new parking',
                    'PUT /api/parkings/<id>': 'Update a parking',
                    'DELETE /api/parkings/<id>': 'Delete a parking'
                },
                'rentings': {
                    'GET /api/rentings': 'Get all rentings',
                    'GET /api/rentings/active': 'Get active rentings',
                    'GET /api/rentings/<id>': 'Get renting by ID',
                    'POST /api/rentings': 'Create a new renting',
                    'PUT /api/rentings/<id>': 'Update a renting',
                    'DELETE /api/rentings/<id>': 'Delete a renting'
                },
                'payments': {
                    'GET /api/payments': 'Get all payments',
                    'GET /api/payments/<id>': 'Get payment by ID',
                    'POST /api/payments': 'Create a new payment',
                    'PUT /api/payments/<id>': 'Update a payment',
                    'DELETE /api/payments/<id>': 'Delete a payment'
                },
                'fines': {
                    'GET /api/fines': 'Get all fines',
                    'GET /api/fines/unpaid': 'Get unpaid fines',
                    'GET /api/fines/<id>': 'Get fine by ID',
                    'POST /api/fines': 'Create a new fine',
                    'PUT /api/fines/<id>': 'Update a fine',
                    'DELETE /api/fines/<id>': 'Delete a fine'
                }
            }
        }), 200

    @app.route('/health')
    def health():
        return jsonify({'status': 'healthy'}), 200

    return app


if __name__ == '__main__':
    app = create_app()
    host = os.getenv('FLASK_HOST', '0.0.0.0')
    port = int(os.getenv('FLASK_PORT', '5000'))
    debug = os.getenv('FLASK_DEBUG', 'True').lower() == 'true'

    logger.info(f"Starting Flask application on http://{host}:{port}")
    app.run(debug=debug, host=host, port=port)
