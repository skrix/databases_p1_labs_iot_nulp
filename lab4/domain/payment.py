from sqlalchemy import Column, Integer, Enum, DECIMAL, TIMESTAMP
from sqlalchemy.sql import func
from config.db import db


class Payment(db.Model):
    """
    Payment model representing a payment in the database.
    """
    __tablename__ = 'payments'

    id = Column(Integer, primary_key=True, autoincrement=True)
    created_at = Column(TIMESTAMP, nullable=False, server_default=func.current_timestamp())
    updated_at = Column(TIMESTAMP, nullable=False, server_default=func.current_timestamp(),
                       onupdate=func.current_timestamp())
    status = Column(Enum('pending', 'paid', 'failed', 'refunded'), nullable=False, default='pending')
    amount = Column(DECIMAL(10, 2), nullable=False)
    currency = Column(Enum('USD', 'EUR', 'UAH'), nullable=False, default='USD')

    def __repr__(self):
        return f"<Payment(id={self.id}, amount={self.amount}, currency='{self.currency}', status='{self.status}')>"

    def to_dict(self):
        """
        Converts the Payment object to a dictionary.
        """
        return {
            'id': self.id,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None,
            'status': self.status,
            'amount': float(self.amount) if self.amount else None,
            'currency': self.currency
        }
