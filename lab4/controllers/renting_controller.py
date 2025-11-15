from controllers.base_controller import BaseController
from services.renting_service import RentingService


class RentingController(BaseController):
    """
    Controller for handling Renting-related requests.
    """

    def __init__(self, session):
        self._service = RentingService(session)

    def find_by_id_with_nested(self, renting_id: int):
        """
        Finds a renting by ID with nested relationships.
        :param renting_id: renting ID
        :return: Renting object with nested data or None
        """
        return self._service.find_by_id_with_nested(renting_id)

    def find_all_with_nested(self):
        """
        Finds all rentings with nested relationships.
        :return: List of Renting objects with nested data
        """
        return self._service.find_all_with_nested()

    def find_fines(self, renting_id: int):
        return self._service.find_fines(renting_id)

    def find_payments(self, renting_id: int):
        return self._service.find_payments(renting_id)
