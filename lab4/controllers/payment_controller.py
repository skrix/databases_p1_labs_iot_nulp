from controllers.base_controller import BaseController
from services.payment_service import PaymentService


class PaymentController(BaseController):
    """
    Controller for handling Payment-related requests.
    """

    def __init__(self, session):
        self._service = PaymentService(session)

    def find_by_status(self, status: str):
        """
        Finds all payments with a specific status.
        :param status: payment status
        :return: List of Payment objects
        """
        return self._service.find_by_status(status)
