from controllers.base_controller import BaseController
from services.parking_service import ParkingService


class ParkingController(BaseController):
    """
    Controller for handling Parking-related requests.
    """

    def __init__(self, session):
        self._service = ParkingService(session)

    def find_by_city(self, city: str):
        """
        Finds all parkings in a city.
        :param city: city name
        :return: List of Parking objects
        """
        return self._service.find_by_city(city)

    def find_vehicles(self, parking_id: int):
        return self._service.find_vehicles(parking_id)
