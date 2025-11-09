from dao.base_dao import BaseDAO
from domain.renting import Renting


class RentingDAO(BaseDAO):
    """
    Data Access Object for Renting entity.
    """
    _model = Renting

    def __init__(self, session):
        self._session = session

    def find_by_user_id(self, user_id: int):
        """
        Finds all rentings for a user.
        :param user_id: user ID
        :return: List of Renting objects
        """
        return self._session.query(self._model).filter_by(user_id=user_id).all()

    def find_active_rentings(self):
        """
        Finds all active rentings (end_at is NULL).
        :return: List of Renting objects
        """
        return self._session.query(self._model).filter(self._model.end_at.is_(None)).all()

    def find_fines(self, renting_id: int):
        from domain.fine import Fine
        from domain.renting_fine import RentingFine
        return self._session.query(Fine).join(
            RentingFine, Fine.id == RentingFine.fine_id
        ).filter(RentingFine.renting_id == renting_id).all()

    def find_payments(self, renting_id: int):
        from domain.payment import Payment
        from domain.renting_payment import RentingPayment
        return self._session.query(Payment).join(
            RentingPayment, Payment.id == RentingPayment.payment_id
        ).filter(RentingPayment.renting_id == renting_id).all()
