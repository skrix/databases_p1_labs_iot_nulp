from dao.base_dao import BaseDAO
from domain.renting_payment import RentingPayment


class RentingPaymentDAO(BaseDAO):
    """
    Data Access Object for RentingPayment entity.
    """
    _model = RentingPayment

    def __init__(self, session):
        self._session = session

    def find_by_renting_id(self, renting_id: int):
        """
        Finds all payments for a renting.
        :param renting_id: renting ID
        :return: List of RentingPayment objects
        """
        return self._session.query(self._model).filter_by(renting_id=renting_id).all()
