from sqlalchemy import Column, Integer, String, DECIMAL
from config.db import Base


class Parking(Base):
    """
    Parking model representing a parking location in the database.
    """
    __tablename__ = 'parkings'

    id = Column(Integer, primary_key=True, autoincrement=True)
    address = Column(String(255), nullable=True)
    country = Column(String(100), nullable=True)
    city = Column(String(100), nullable=True)
    latitude = Column(DECIMAL(11, 8), nullable=False)
    longitude = Column(DECIMAL(11, 8), nullable=False)

    def __repr__(self):
        return f"<Parking(id={self.id}, city='{self.city}', address='{self.address}')>"

    def to_dict(self):
        """
        Converts the Parking object to a dictionary.
        """
        return {
            'id': self.id,
            'address': self.address,
            'country': self.country,
            'city': self.city,
            'latitude': float(self.latitude) if self.latitude else None,
            'longitude': float(self.longitude) if self.longitude else None
        }
