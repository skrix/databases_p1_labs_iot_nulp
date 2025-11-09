from controllers.base_controller import BaseController
from services.renting_service import RentingService


class RentingController(BaseController):
    """
    Controller for handling Renting-related requests.
    """

    def __init__(self, session):
        self._service = RentingService(session)

    def find_by_user_id(self, user_id: int):
        """
        Finds all rentings for a user.
        :param user_id: user ID
        :return: List of Renting objects
        """
        return self._service.find_by_user_id(user_id)

    def find_active_rentings(self):
        """
        Finds all active rentings.
        :return: List of Renting objects
        """
        return self._service.find_active_rentings()
