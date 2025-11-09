from dao.base_dao import BaseDAO
from domain.payment import Payment


class PaymentDAO(BaseDAO):
    """
    Data Access Object for Payment entity.
    """
    _model = Payment

    def __init__(self, session):
        self._session = session

    def find_by_status(self, status: str):
        """
        Finds all payments with a specific status.
        :param status: payment status
        :return: List of Payment objects
        """
        return self._session.query(self._model).filter_by(status=status).all()
