from services.base_service import BaseService
from dao.vehicle_dao import VehicleDAO


class VehicleService(BaseService):
    """
    Business logic layer for Vehicle entity.
    """

    def __init__(self, session):
        self._dao = VehicleDAO(session)

    def find_by_vin(self, vin: str):
        """
        Finds a vehicle by VIN.
        :param vin: VIN to search
        :return: Vehicle object or None
        """
        return self._dao.find_by_vin(vin)

    def find_by_plate(self, plate: str):
        """
        Finds a vehicle by license plate.
        :param plate: plate to search
        :return: Vehicle object or None
        """
        return self._dao.find_by_plate(plate)
