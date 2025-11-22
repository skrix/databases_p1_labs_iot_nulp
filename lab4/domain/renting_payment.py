from sqlalchemy import Column, Integer, ForeignKey, TIMESTAMP
from sqlalchemy.sql import func
from config.db import db


class RentingPayment(db.Model):
    """
    RentingPayment model representing the relationship between rentings and payments.
    """
    __tablename__ = 'rentings_payments'

    id = Column(Integer, primary_key=True, autoincrement=True)
    renting_id = Column(Integer, ForeignKey('rentings.id'), nullable=False)
    payment_id = Column(Integer, ForeignKey('payments.id'), nullable=False)
    created_at = Column(TIMESTAMP, nullable=False, server_default=func.current_timestamp())
    updated_at = Column(TIMESTAMP, nullable=False, server_default=func.current_timestamp(),
                       onupdate=func.current_timestamp())

    def __repr__(self):
        return f"<RentingPayment(id={self.id}, renting_id={self.renting_id}, payment_id={self.payment_id})>"

    def to_dict(self):
        """
        Converts the RentingPayment object to a dictionary.
        """
        return {
            'id': self.id,
            'renting_id': self.renting_id,
            'payment_id': self.payment_id,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None
        }
