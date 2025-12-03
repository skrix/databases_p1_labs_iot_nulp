from sqlalchemy import Column, Integer, Text, TIMESTAMP
from sqlalchemy.sql import func
from config.db import db


class UserNote(db.Model):
    """
    UserNote model representing a note associated with a user.
    This table uses triggers for referential integrity instead of foreign keys.
    """
    __tablename__ = 'user_notes'

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, nullable=False)  # No FK, enforced by trigger
    note = Column(Text, nullable=False)
    created_at = Column(TIMESTAMP, nullable=False, server_default=func.current_timestamp())

    def __repr__(self):
        return f"<UserNote(id={self.id}, user_id={self.user_id}, note='{self.note[:50]}...')>"

    def to_dict(self):
        """
        Converts the UserNote object to a dictionary.
        """
        return {
            'id': self.id,
            'user_id': self.user_id,
            'note': self.note,
            'created_at': self.created_at.isoformat() if self.created_at else None
        }
