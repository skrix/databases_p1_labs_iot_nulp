from abc import ABC
from typing import List
from sqlalchemy import inspect
from sqlalchemy.orm import Mapper


class BaseDAO(ABC):
    """
    The common realization of Data Access class.
    """
    _model = None
    _session = None

    def find_all(self) -> List[object]:
        """
        Gets all objects from table.
        :return: list of all objects
        """
        return self._session.query(self._model).all()

    def find_by_id(self, key: int) -> object:
        """
        Gets object from database table by integer key.
        :param key: integer (PK)
        :return: object
        """
        return self._session.query(self._model).get(key)

    def create(self, obj: object) -> object:
        """
        Creates obj in database table.
        :param obj: object to create in database
        :return: created obj
        """
        self._session.add(obj)
        self._session.commit()
        return obj

    def create_all(self, obj_list: List[object]) -> List[object]:
        """
        Creates objects from object list.
        :param obj_list: object list to create in database
        :return: list of created object
        """
        self._session.add_all(obj_list)
        self._session.commit()
        return obj_list

    def update(self, key: int, attrs: object) -> None:
        """
        Updates object in database table.
        :param key: integer (PK)
        :param attrs: attrs of obj to update in database
        """
        obj = self._session.query(self._model).get(key)
        mapper: Mapper = inspect(type(attrs))
        columns = mapper.columns._collection
        for column_name, column_obj in columns:
            if not column_obj.primary_key:
                value = getattr(attrs, column_name)
                setattr(obj, column_name, value)
        self._session.commit()

    def patch(self, key: int, field: str, value: object) -> None:
        """
        Modifies defined field of object in database table.
        :param key: integer (PK)
        :param field: field name of object
        :param value: field value of object
        """
        obj = self._session.query(self._model).get(key)
        setattr(obj, field, value)
        self._session.commit()

    def delete(self, key: int) -> None:
        """
        Deletes object from database table by integer key.
        :param key: integer (PK)
        """
        obj = self._session.query(self._model).get(key)
        self._session.delete(obj)
        try:
            self._session.commit()
        except Exception:
            self._session.rollback()
            raise

    def delete_all(self) -> None:
        """
        Deletes all objects from database table.
        """
        self._session.query(self._model).delete()
        self._session.commit()
