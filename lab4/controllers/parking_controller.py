from controllers.base_controller import BaseController
from services.parking_service import ParkingService


class ParkingController(BaseController):
    """
    Controller for handling Parking-related requests.
    """

    def __init__(self, session):
        self._service = ParkingService(session)

    def find_vehicles(self, parking_id: int):
        return self._service.find_vehicles(parking_id)
