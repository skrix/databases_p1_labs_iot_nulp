from dao.base_dao import BaseDAO
from domain.payment import Payment


class PaymentDAO(BaseDAO):
    """
    Data Access Object for Payment entity.
    """
    _model = Payment

    def __init__(self, session):
        self._session = session
