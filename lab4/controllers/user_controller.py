from controllers.base_controller import BaseController
from services.user_service import UserService


class UserController(BaseController):
    """
    Controller for handling User-related requests.
    """

    def __init__(self, session):
        self._service = UserService(session)

    def find_by_email(self, email: str):
        """
        Finds a user by email.
        :param email: email to search
        :return: User object or None
        """
        return self._service.find_by_email(email)

    def find_by_driver_license(self, driver_license: str):
        """
        Finds a user by driver license.
        :param driver_license: driver license to search
        :return: User object or None
        """
        return self._service.find_by_driver_license(driver_license)

    def find_rentings(self, user_id: int):
        return self._service.find_rentings(user_id)

    def find_fines(self, user_id: int):
        return self._service.find_fines(user_id)
