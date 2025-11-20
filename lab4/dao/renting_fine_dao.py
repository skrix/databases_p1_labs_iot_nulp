from dao.base_dao import BaseDAO
from domain.renting_fine import RentingFine


class RentingFineDAO(BaseDAO):
    """
    Data Access Object for RentingFine entity.
    """
    _model = RentingFine

    def __init__(self, session):
        self._session = session

    def find_by_renting_id(self, renting_id: int):
        """
        Finds all fines for a renting.
        :param renting_id: renting ID
        :return: List of RentingFine objects
        """
        return self._session.query(self._model).filter_by(renting_id=renting_id).all()
