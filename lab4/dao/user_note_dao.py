from dao.base_dao import BaseDAO
from domain.user_note import UserNote


class UserNoteDAO(BaseDAO):
    """
    Data Access Object for UserNote entity.
    """
    _model = UserNote

    def __init__(self, session):
        self._session = session

    def find_by_user_id(self, user_id: int):
        """
        Finds all notes for a specific user.
        :param user_id: user ID
        :return: List of UserNote objects
        """
        return self._session.query(self._model).filter_by(user_id=user_id).all()
