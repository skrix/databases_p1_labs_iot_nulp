from dao.base_dao import BaseDAO
from domain.vehicle import Vehicle


class VehicleDAO(BaseDAO):
    """
    Data Access Object for Vehicle entity.
    """
    _model = Vehicle

    def __init__(self, session):
        self._session = session

    def find_by_id_with_nested(self, vehicle_id: int):
        """
        Finds a vehicle by ID with nested rentings and parkings.
        :param vehicle_id: vehicle ID
        :return: Vehicle object with nested data or None
        """
        vehicle = self._session.query(self._model).filter_by(id=vehicle_id).first()
        if vehicle:
            vehicle._rentings = self.find_rentings(vehicle_id)
            vehicle._parkings = self.find_parkings(vehicle_id)
        return vehicle

    def find_all_with_nested(self):
        """
        Finds all vehicles with nested rentings and parkings.
        :return: List of Vehicle objects with nested data
        """
        vehicles = self._session.query(self._model).all()
        for vehicle in vehicles:
            vehicle._rentings = self.find_rentings(vehicle.id)
            vehicle._parkings = self.find_parkings(vehicle.id)
        return vehicles

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
