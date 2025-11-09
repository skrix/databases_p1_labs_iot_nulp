from services.base_service import BaseService
from dao.fine_dao import FineDAO


class FineService(BaseService):
    """
    Business logic layer for Fine entity.
    """

    def __init__(self, session):
        self._dao = FineDAO(session)

    def find_by_status(self, status: str):
        """
        Finds all fines with a specific status.
        :param status: fine status
        :return: List of Fine objects
        """
        return self._dao.find_by_status(status)

    def find_unpaid_fines(self):
        """
        Finds all unpaid fines.
        :return: List of Fine objects
        """
        return self._dao.find_unpaid_fines()
