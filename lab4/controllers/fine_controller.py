from controllers.base_controller import BaseController
from services.fine_service import FineService


class FineController(BaseController):
    """
    Controller for handling Fine-related requests.
    """

    def __init__(self, session):
        self._service = FineService(session)

    def find_by_status(self, status: str):
        """
        Finds all fines with a specific status.
        :param status: fine status
        :return: List of Fine objects
        """
        return self._service.find_by_status(status)

    def find_unpaid_fines(self):
        """
        Finds all unpaid fines.
        :return: List of Fine objects
        """
        return self._service.find_unpaid_fines()
