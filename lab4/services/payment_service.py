from services.base_service import BaseService
from dao.payment_dao import PaymentDAO


class PaymentService(BaseService):
    """
    Business logic layer for Payment entity.
    """

    def __init__(self, session):
        self._dao = PaymentDAO(session)

    def find_by_status(self, status: str):
        """
        Finds all payments with a specific status.
        :param status: payment status
        :return: List of Payment objects
        """
        return self._dao.find_by_status(status)
