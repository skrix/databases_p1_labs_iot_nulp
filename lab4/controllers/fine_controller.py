from controllers.base_controller import BaseController
from services.fine_service import FineService


class FineController(BaseController):
    """
    Controller for handling Fine-related requests.
    """

    def __init__(self, session):
        self._service = FineService(session)

    def find_payments(self, fine_id: int):
        return self._service.find_payments(fine_id)
