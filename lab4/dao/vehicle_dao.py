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

    def find_rentings(self, vehicle_id: int):
        from domain.renting import Renting
        return self._session.query(Renting).filter_by(vehicle_id=vehicle_id).all()

    def find_parkings(self, vehicle_id: int):
        from domain.parking import Parking
        from domain.parking_vehicle import ParkingVehicle
        return self._session.query(Parking).join(
            ParkingVehicle, Parking.id == ParkingVehicle.parking_id
        ).filter(ParkingVehicle.vehicle_id == vehicle_id).all()
