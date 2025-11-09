from services.base_service import BaseService
from dao.parking_dao import ParkingDAO


class ParkingService(BaseService):
    """
    Business logic layer for Parking entity.
    """

    def __init__(self, session):
        self._dao = ParkingDAO(session)

    def find_by_city(self, city: str):
        """
        Finds all parkings in a city.
        :param city: city name
        :return: List of Parking objects
        """
        return self._dao.find_by_city(city)
