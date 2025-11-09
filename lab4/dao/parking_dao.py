from dao.base_dao import BaseDAO
from domain.parking import Parking


class ParkingDAO(BaseDAO):
    """
    Data Access Object for Parking entity.
    """
    _model = Parking

    def __init__(self, session):
        self._session = session

    def find_by_city(self, city: str):
        """
        Finds all parkings in a city.
        :param city: city name
        :return: List of Parking objects
        """
        return self._session.query(self._model).filter_by(city=city).all()

    def find_vehicles(self, parking_id: int):
        from domain.vehicle import Vehicle
        from domain.parking_vehicle import ParkingVehicle
        return self._session.query(Vehicle).join(
            ParkingVehicle, Vehicle.id == ParkingVehicle.vehicle_id
        ).filter(ParkingVehicle.parking_id == parking_id).all()
