from services.base_service import BaseService
from dao.fine_dao import FineDAO


class FineService(BaseService):
    """
    Business logic layer for Fine entity.
    """

    def __init__(self, session):
        self._dao = FineDAO(session)

    def find_payments(self, fine_id: int):
        return self._dao.find_payments(fine_id)
