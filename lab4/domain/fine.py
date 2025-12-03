from sqlalchemy import Column, Integer, String, Enum, DECIMAL, TIMESTAMP
from sqlalchemy.sql import func
from config.db import db


class Fine(db.Model):
    """
    Fine model representing a traffic fine in the database.
    """
    __tablename__ = 'fines'

    id = Column(Integer, primary_key=True, autoincrement=True)
    created_at = Column(TIMESTAMP, nullable=False, server_default=func.current_timestamp())
    updated_at = Column(TIMESTAMP, nullable=False, server_default=func.current_timestamp(),
                       onupdate=func.current_timestamp())
    status = Column(Enum('paid', 'unpaid', 'disputed', 'waived'), nullable=False, default='unpaid')
    amount = Column(DECIMAL(10, 2), nullable=False)
    currency = Column(Enum('USD', 'EUR', 'UAH'), nullable=False, default='USD')
    violation = Column(String(255), nullable=False)

    def __repr__(self):
        return f"<Fine(id={self.id}, violation='{self.violation}', amount={self.amount}, status='{self.status}')>"

    def to_dict(self):
        """
        Converts the Fine object to a dictionary.
        """
        return {
            'id': self.id,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None,
            'status': self.status,
            'amount': float(self.amount) if self.amount else None,
            'currency': self.currency,
            'violation': self.violation
        }
