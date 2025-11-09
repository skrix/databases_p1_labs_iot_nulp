from dao.base_dao import BaseDAO
from domain.vehicle import Vehicle


class VehicleDAO(BaseDAO):
    """
    Data Access Object for Vehicle entity.
    """
    _model = Vehicle

    def __init__(self, session):
        self._session = session

    def find_by_vin(self, vin: str) -> Vehicle:
        """
        Finds a vehicle by VIN.
        :param vin: VIN to search
        :return: Vehicle object or None
        """
        return self._session.query(self._model).filter_by(vin=vin).first()

    def find_by_plate(self, plate: str) -> Vehicle:
        """
        Finds a vehicle by license plate.
        :param plate: license plate to search
        :return: Vehicle object or None
        """
        return self._session.query(self._model).filter_by(plate=plate).first()
