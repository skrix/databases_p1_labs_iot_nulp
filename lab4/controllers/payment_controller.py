from controllers.base_controller import BaseController
from services.payment_service import PaymentService


class PaymentController(BaseController):
    """
    Controller for handling Payment-related requests.
    """

    def __init__(self, session):
        self._service = PaymentService(session)
