"""
Setup script to initialize the database and create tables.
Run this script before starting the application.
"""
from app import create_app
from config.db import db

from domain.user import User
from domain.vehicle import Vehicle
from domain.parking import Parking
from domain.renting import Renting
from domain.payment import Payment
from domain.fine import Fine
from domain.parking_vehicle import ParkingVehicle
from domain.renting_payment import RentingPayment
from domain.renting_fine import RentingFine
from domain.fine_payment import FinePayment
from domain.user_note import UserNote


def setup_database():
    """
    Creates all database tables based on the defined models.
    """
    app = create_app()

    with app.app_context():
        print("Creating database tables...")
        db.create_all()
        print("Database tables created successfully!")

        # List all created tables
        print("\nCreated tables:")
        for table in db.metadata.sorted_tables:
            print(f"  - {table.name}")


if __name__ == '__main__':
    setup_database()
