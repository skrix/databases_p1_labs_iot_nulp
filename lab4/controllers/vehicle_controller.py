from controllers.base_controller import BaseController
from services.vehicle_service import VehicleService


class VehicleController(BaseController):
    """
    Controller for handling Vehicle-related requests.
    """

    def __init__(self, session):
        self._service = VehicleService(session)

    def find_by_vin(self, vin: str):
        """
        Finds a vehicle by VIN.
        :param vin: VIN to search
        :return: Vehicle object or None
        """
        return self._service.find_by_vin(vin)

    def find_by_plate(self, plate: str):
        """
        Finds a vehicle by license plate.
        :param plate: plate to search
        :return: Vehicle object or None
        """
        return self._service.find_by_plate(plate)
