from sqlalchemy import Column, Integer, String, Date, Enum, TIMESTAMP
from sqlalchemy.sql import func
from config.db import Base


class User(Base):
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

    def to_dict(self):
        """
        Converts the User object to a dictionary.
        """
        return {
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
