from services.base_service import BaseService
from dao.user_dao import UserDAO


class UserService(BaseService):
    """
    Business logic layer for User entity.
    """

    def __init__(self, session):
        self._dao = UserDAO(session)

    def find_by_id_with_nested(self, user_id: int):
        """
        Finds a user by ID with nested relationships.
        :param user_id: user ID
        :return: User object with nested data or None
        """
        return self._dao.find_by_id_with_nested(user_id)

    def find_all_with_nested(self):
        """
        Finds all users with nested relationships.
        :return: List of User objects with nested data
        """
        return self._dao.find_all_with_nested()

    def find_by_email(self, email: str):
        """
        Finds a user by email.
        :param email: email to search
        :return: User object or None
        """
        return self._dao.find_by_email(email)

    def find_by_driver_license(self, driver_license: str):
        """
        Finds a user by driver license.
        :param driver_license: driver license to search
        :return: User object or None
        """
        return self._dao.find_by_driver_license(driver_license)

    def find_rentings(self, user_id: int):
        return self._dao.find_rentings(user_id)

    def find_fines(self, user_id: int):
        return self._dao.find_fines(user_id)
