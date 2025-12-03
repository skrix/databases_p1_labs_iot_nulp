from sqlalchemy import Column, Integer, String, Date, Enum, TIMESTAMP
from sqlalchemy.sql import func
from config.db import db


class User(db.Model):
    """
    User model representing a user in the database.
    """
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(100), nullable=False)
    middle_name = Column(String(100), nullable=True)
    last_name = Column(String(100), nullable=False)
    dob = Column(Date, nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    created_at = Column(TIMESTAMP, nullable=False, server_default=func.current_timestamp())
    driver_license = Column(String(255), unique=True, nullable=False)
    gender = Column(Enum('male', 'female', 'other', 'prefer_not_to_say'), nullable=False)

    def __repr__(self):
        return f"<User(id={self.id}, first_name='{self.first_name}', last_name='{self.last_name}', email='{self.email}')>"

    def to_dict(self, include_nested=False):
        """
        Converts the User object to a dictionary.
        :param include_nested: If True, includes nested rentings and fines
        """
        result = {
            'id': self.id,
            'first_name': self.first_name,
            'middle_name': self.middle_name,
            'last_name': self.last_name,
            'dob': self.dob.isoformat() if self.dob else None,
            'email': self.email,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'driver_license': self.driver_license,
            'gender': self.gender
        }

        if include_nested:
            # Include nested rentings if available
            if hasattr(self, '_rentings') and self._rentings is not None:
                result['rentings'] = [r.to_dict(include_nested=True) for r in self._rentings]
            # Include nested fines if available
            if hasattr(self, '_fines') and self._fines is not None:
                result['fines'] = [f.to_dict() for f in self._fines]

        return result
