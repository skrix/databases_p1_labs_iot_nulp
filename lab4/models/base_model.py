from abc import ABC
from typing import List
from sqlalchemy import inspect
from sqlalchemy.orm import Mapper


class BaseModel(ABC):
    """
    The common realization of Data Access class.
    """
    _model_table = None
    _session = None

    def find_all(self) -> List[object]:
        """
        Gets all objects from table.
        :return: list of all objects
        """
        return self._session.query(self._model_table).all()

    def find_by_id(self, key: int) -> object:
        """
        Gets object from database table by integer key.
        :param key: integer (PK)
        :return: object
        """
        return self._session.query(self._model_table).get(key)

    def create(self, record: object) -> object:
        """
        Creates record in database table.
        :param record: object to create in database
        :return: created record
        """
        self._session.add(record)
        self._session.commit()
        return record

    def create_all(self, records: List[object]) -> List[object]:
        """
        Creates objects from object list.
        :param records: object list to create in database
        :return: list of created object
        """
        self._session.add_all(records)
        self._session.commit()
        return records

    def update(self, key: int, attrs: object) -> None:
        """
        Updates object in database table.
        :param key: integer (PK)
        :param attrs: attrs of record to update in database
        """
        record = self._session.query(self._model_table).get(key)
        mapper: Mapper = inspect(type(attrs))
        columns = mapper.columns._collection
        for column_name, column_obj in columns:
            if not column_obj.primary_key:
                value = getattr(attrs, column_name)
                setattr(record, column_name, value)
        self._session.commit()

    def patch(self, key: int, field: str, value: object) -> None:
        """
        Modifies defined field of object in database table.
        :param key: integer (PK)
        :param field: field name of object
        :param value: field value of object
        """
        record = self._session.query(self._model_table).get(key)
        setattr(record, field, value)
        self._session.commit()

    def delete(self, key: int) -> None:
        """
        Deletes object from database table by integer key.
        :param key: integer (PK)
        """
        record = self._session.query(self._model_table).get(key)
        self._session.delete(record)
        try:
            self._session.commit()
        except Exception:
            self._session.rollback()
            raise

    def delete_all(self) -> None:
        """
        Deletes all objects from database table.
        """
        self._session.query(self._model_table).delete()
        self._session.commit()
