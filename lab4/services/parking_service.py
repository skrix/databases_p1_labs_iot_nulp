from services.base_service import BaseService
from dao.parking_dao import ParkingDAO


class ParkingService(BaseService):
    """
    Business logic layer for Parking entity.
    """

    def __init__(self, session):
        self._dao = ParkingDAO(session)

    def find_vehicles(self, parking_id: int):
        return self._dao.find_vehicles(parking_id)
