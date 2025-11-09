from sqlalchemy import Column, Integer, ForeignKey, TIMESTAMP
from sqlalchemy.sql import func
from config.db import Base


class ParkingVehicle(Base):
    """
    ParkingVehicle model representing the relationship between parkings and vehicles.
    """
    __tablename__ = 'parkings_vehicles'

    id = Column(Integer, primary_key=True, autoincrement=True)
    parking_id = Column(Integer, ForeignKey('parkings.id'), nullable=False)
    vehicle_id = Column(Integer, ForeignKey('vehicles.id'), nullable=False)
    created_at = Column(TIMESTAMP, nullable=False, server_default=func.current_timestamp())
    updated_at = Column(TIMESTAMP, nullable=False, server_default=func.current_timestamp(),
                       onupdate=func.current_timestamp())

    def __repr__(self):
        return f"<ParkingVehicle(id={self.id}, parking_id={self.parking_id}, vehicle_id={self.vehicle_id})>"

    def to_dict(self):
        """
        Converts the ParkingVehicle object to a dictionary.
        """
        return {
            'id': self.id,
            'parking_id': self.parking_id,
            'vehicle_id': self.vehicle_id,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None
        }
