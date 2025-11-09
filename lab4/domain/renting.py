from sqlalchemy import Column, Integer, ForeignKey, TIMESTAMP, DateTime
from sqlalchemy.sql import func
from config.db import Base


class Renting(Base):
    """
    Renting model representing a vehicle rental in the database.
    """
    __tablename__ = 'rentings'

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    vehicle_id = Column(Integer, ForeignKey('vehicles.id'), nullable=False)
    created_at = Column(TIMESTAMP, nullable=False, server_default=func.current_timestamp())
    updated_at = Column(TIMESTAMP, nullable=False, server_default=func.current_timestamp(),
                       onupdate=func.current_timestamp())
    start_at = Column(DateTime, nullable=False)
    end_at = Column(DateTime, nullable=True)

    def __repr__(self):
        return f"<Renting(id={self.id}, user_id={self.user_id}, vehicle_id={self.vehicle_id})>"

    def to_dict(self):
        """
        Converts the Renting object to a dictionary.
        """
        return {
            'id': self.id,
            'user_id': self.user_id,
            'vehicle_id': self.vehicle_id,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None,
            'start_at': self.start_at.isoformat() if self.start_at else None,
            'end_at': self.end_at.isoformat() if self.end_at else None
        }
