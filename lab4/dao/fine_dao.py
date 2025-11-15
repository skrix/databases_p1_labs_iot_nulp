from dao.base_dao import BaseDAO
from domain.fine import Fine


class FineDAO(BaseDAO):
    """
    Data Access Object for Fine entity.
    """
    _model = Fine

    def __init__(self, session):
        self._session = session

    def find_payments(self, fine_id: int):
        from domain.payment import Payment
        from domain.fine_payment import FinePayment
        return self._session.query(Payment).join(
            FinePayment, Payment.id == FinePayment.payment_id
        ).filter(FinePayment.fine_id == fine_id).all()
