from dao.base_dao import BaseDAO
from domain.parking_vehicle import ParkingVehicle


class ParkingVehicleDAO(BaseDAO):
    """
    Data Access Object for ParkingVehicle entity.
    """
    _model = ParkingVehicle

    def __init__(self, session):
        self._session = session

    def find_by_parking_id(self, parking_id: int):
        """
        Finds all vehicles in a parking.
        :param parking_id: parking ID
        :return: List of ParkingVehicle objects
        """
        return self._session.query(self._model).filter_by(parking_id=parking_id).all()

    def find_by_vehicle_id(self, vehicle_id: int):
        """
        Finds all parkings for a vehicle.
        :param vehicle_id: vehicle ID
        :return: List of ParkingVehicle objects
        """
        return self._session.query(self._model).filter_by(vehicle_id=vehicle_id).all()
