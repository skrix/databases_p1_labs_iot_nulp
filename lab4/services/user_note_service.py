from services.base_service import BaseService
from dao.user_note_dao import UserNoteDAO


class UserNoteService(BaseService):
    """
    Business logic layer for UserNote entity.
    """

    def __init__(self, session):
        self._dao = UserNoteDAO(session)

    def find_by_user_id(self, user_id: int):
        """
        Finds all notes for a specific user.
        :param user_id: user ID
        :return: List of UserNote objects
        """
        return self._dao.find_by_user_id(user_id)
