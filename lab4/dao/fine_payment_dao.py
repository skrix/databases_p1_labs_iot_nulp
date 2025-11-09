from dao.base_dao import BaseDAO
from domain.fine_payment import FinePayment


class FinePaymentDAO(BaseDAO):
    """
    Data Access Object for FinePayment entity.
    """
    _model = FinePayment

    def __init__(self, session):
        self._session = session

    def find_by_fine_id(self, fine_id: int):
        """
        Finds all payments for a fine.
        :param fine_id: fine ID
        :return: List of FinePayment objects
        """
        return self._session.query(self._model).filter_by(fine_id=fine_id).all()
