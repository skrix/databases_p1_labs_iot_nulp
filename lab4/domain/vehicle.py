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

    def to_dict(self, include_nested=False):
        """
        Converts the Vehicle object to a dictionary.
        :param include_nested: If True, includes nested rentings and parkings
        """
        result = {
            'id': self.id,
            'make': self.make,
            'model': self.model,
            'year': self.year,
            'vin': self.vin,
            'body': self.body,
            'plate': self.plate
        }

        if include_nested:
            # Include nested rentings if available
            if hasattr(self, '_rentings') and self._rentings is not None:
                result['rentings'] = [r.to_dict() for r in self._rentings]
            # Include nested parkings if available
            if hasattr(self, '_parkings') and self._parkings is not None:
                result['parkings'] = [p.to_dict() for p in self._parkings]

        return result
