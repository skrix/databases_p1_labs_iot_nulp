from dao.base_dao import BaseDAO
from domain.user import User


class UserDAO(BaseDAO):
    """
    Data Access Object for User entity.
    """
    _model = User

    def __init__(self, session):
        self._session = session

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
