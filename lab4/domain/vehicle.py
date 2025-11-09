from sqlalchemy import Column, Integer, String, Enum
from config.db import Base


class Vehicle(Base):
    """
    Vehicle model representing a vehicle in the database.
    """
    __tablename__ = 'vehicles'

    id = Column(Integer, primary_key=True, autoincrement=True)
    make = Column(String(100), nullable=False)
    model = Column(String(100), nullable=False)
    year = Column(Integer, nullable=False)
    vin = Column(String(17), unique=True, nullable=False)
    body = Column(Enum('sedan', 'hatchback', 'wagon', 'coupe', 'convertible', 'roadster',
                       'suv', 'crossover', 'pickup', 'van', 'minivan', 'truck', 'camper'),
                 nullable=False, default='sedan')
    plate = Column(String(15), unique=True, nullable=False)

    def __repr__(self):
        return f"<Vehicle(id={self.id}, make='{self.make}', model='{self.model}', plate='{self.plate}')>"

    def to_dict(self):
        """
        Converts the Vehicle object to a dictionary.
        """
        return {
            'id': self.id,
            'make': self.make,
            'model': self.model,
            'year': self.year,
            'vin': self.vin,
            'body': self.body,
            'plate': self.plate
        }
