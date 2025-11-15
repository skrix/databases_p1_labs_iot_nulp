from services.base_service import BaseService
from dao.renting_dao import RentingDAO


class RentingService(BaseService):
    """
    Business logic layer for Renting entity.
    """

    def __init__(self, session):
        self._dao = RentingDAO(session)

    def find_by_id_with_nested(self, renting_id: int):
        """
        Finds a renting by ID with nested relationships.
        :param renting_id: renting ID
        :return: Renting object with nested data or None
        """
        return self._dao.find_by_id_with_nested(renting_id)

    def find_all_with_nested(self):
        """
        Finds all rentings with nested relationships.
        :return: List of Renting objects with nested data
        """
        return self._dao.find_all_with_nested()

    def find_fines(self, renting_id: int):
        return self._dao.find_fines(renting_id)

    def find_payments(self, renting_id: int):
        return self._dao.find_payments(renting_id)
