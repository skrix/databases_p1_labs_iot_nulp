from services.base_service import BaseService
from dao.vehicle_dao import VehicleDAO


class VehicleService(BaseService):
    """
    Business logic layer for Vehicle entity.
    """

    def __init__(self, session):
        self._dao = VehicleDAO(session)

    def find_by_id_with_nested(self, vehicle_id: int):
        """
        Finds a vehicle by ID with nested relationships.
        :param vehicle_id: vehicle ID
        :return: Vehicle object with nested data or None
        """
        return self._dao.find_by_id_with_nested(vehicle_id)

    def find_all_with_nested(self):
        """
        Finds all vehicles with nested relationships.
        :return: List of Vehicle objects with nested data
        """
        return self._dao.find_all_with_nested()

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

    def find_rentings(self, vehicle_id: int):
        return self._dao.find_rentings(vehicle_id)

    def find_parkings(self, vehicle_id: int):
        return self._dao.find_parkings(vehicle_id)
