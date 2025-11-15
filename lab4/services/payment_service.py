from services.base_service import BaseService
from dao.payment_dao import PaymentDAO


class PaymentService(BaseService):
    """
    Business logic layer for Payment entity.
    """

    def __init__(self, session):
        self._dao = PaymentDAO(session)
