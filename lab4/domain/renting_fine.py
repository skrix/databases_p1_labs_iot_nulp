from sqlalchemy import Column, Integer, ForeignKey, TIMESTAMP
from sqlalchemy.sql import func
from config.db import Base


class RentingFine(Base):
    """
    RentingFine model representing the relationship between rentings and fines.
    """
    __tablename__ = 'rentings_fines'

    id = Column(Integer, primary_key=True, autoincrement=True)
    renting_id = Column(Integer, ForeignKey('rentings.id'), nullable=False)
    fine_id = Column(Integer, ForeignKey('fines.id'), nullable=False)
    created_at = Column(TIMESTAMP, nullable=False, server_default=func.current_timestamp())
    updated_at = Column(TIMESTAMP, nullable=False, server_default=func.current_timestamp(),
                       onupdate=func.current_timestamp())

    def __repr__(self):
        return f"<RentingFine(id={self.id}, renting_id={self.renting_id}, fine_id={self.fine_id})>"

    def to_dict(self):
        """
        Converts the RentingFine object to a dictionary.
        """
        return {
            'id': self.id,
            'renting_id': self.renting_id,
            'fine_id': self.fine_id,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None
        }
