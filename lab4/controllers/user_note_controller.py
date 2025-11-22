from controllers.base_controller import BaseController
from services.user_note_service import UserNoteService


class UserNoteController(BaseController):
    """
    Controller for handling UserNote-related requests.
    """

    def __init__(self, session):
        self._service = UserNoteService(session)

    def find_by_user_id(self, user_id: int):
        """
        Finds all notes for a specific user.
        :param user_id: user ID
        :return: List of UserNote objects
        """
        return self._service.find_by_user_id(user_id)
