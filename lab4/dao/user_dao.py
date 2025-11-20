from dao.base_dao import BaseDAO
from domain.user import User


class UserDAO(BaseDAO):
    """
    Data Access Object for User entity.
    """
    _model = User

    def __init__(self, session):
        self._session = session

    def find_by_id_with_nested(self, user_id: int):
        """
        Finds a user by ID with nested rentings and fines.
        :param user_id: user ID
        :return: User object with nested data or None
        """
        user = self._session.query(self._model).filter_by(id=user_id).first()
        if user:
            user._rentings = self.find_rentings(user_id)
            # Load nested data for each renting
            for renting in user._rentings:
                renting._vehicle = self._session.query(self._model.__table__.metadata.tables['vehicles']).filter_by(id=renting.vehicle_id).first()
                from domain.vehicle import Vehicle
                renting._vehicle = self._session.query(Vehicle).filter_by(id=renting.vehicle_id).first()
                renting._fines = self.find_renting_fines(renting.id)
                renting._payments = self.find_renting_payments(renting.id)
            user._fines = self.find_fines(user_id)
        return user

    def find_all_with_nested(self):
        """
        Finds all users with nested rentings and fines.
        :return: List of User objects with nested data
        """
        users = self._session.query(self._model).all()
        for user in users:
            user._rentings = self.find_rentings(user.id)
            for renting in user._rentings:
                from domain.vehicle import Vehicle
                renting._vehicle = self._session.query(Vehicle).filter_by(id=renting.vehicle_id).first()
                renting._fines = self.find_renting_fines(renting.id)
                renting._payments = self.find_renting_payments(renting.id)
            user._fines = self.find_fines(user.id)
        return users

    def find_by_email(self, email: str) -> User:
        """
        Finds a user by email.
        :param email: email to search
        :return: User object or None
        """
        return self._session.query(self._model).filter_by(email=email).first()

    def find_by_driver_license(self, driver_license: str) -> User:
        """
        Finds a user by driver license.
        :param driver_license: driver license to search
        :return: User object or None
        """
        return self._session.query(self._model).filter_by(driver_license=driver_license).first()

    def find_rentings(self, user_id: int):
        from domain.renting import Renting
        return self._session.query(Renting).filter_by(user_id=user_id).all()

    def find_fines(self, user_id: int):
        from domain.renting import Renting
        from domain.renting_fine import RentingFine
        from domain.fine import Fine
        return self._session.query(Fine).join(
            RentingFine, Fine.id == RentingFine.fine_id
        ).join(
            Renting, RentingFine.renting_id == Renting.id
        ).filter(Renting.user_id == user_id).all()

    def find_renting_fines(self, renting_id: int):
        from domain.fine import Fine
        from domain.renting_fine import RentingFine
        return self._session.query(Fine).join(
            RentingFine, Fine.id == RentingFine.fine_id
        ).filter(RentingFine.renting_id == renting_id).all()

    def find_renting_payments(self, renting_id: int):
        from domain.payment import Payment
        from domain.renting_payment import RentingPayment
        return self._session.query(Payment).join(
            RentingPayment, Payment.id == RentingPayment.payment_id
        ).filter(RentingPayment.renting_id == renting_id).all()
