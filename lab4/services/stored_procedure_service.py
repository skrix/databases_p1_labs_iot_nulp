from dao.stored_procedure_dao import StoredProcedureDAO


class StoredProcedureService:
    """
    Business logic layer for stored procedures.
    """

    def __init__(self, session):
        self._dao = StoredProcedureDAO(session)

    def generic_insert(self, table: str, columns: str, values: str):
        """
        Performs a generic insert via stored procedure.
        :param table: table name
        :param columns: comma-separated column names
        :param values: comma-separated values (quoted as needed)
        :return: None
        """
        return self._dao.generic_insert(table, columns, values)

    def join_insert(self, left_table: str, left_lookup_col: str, left_lookup_val: str,
                        right_table: str, right_lookup_col: str, right_lookup_val: str,
                        join_table: str, left_fk: str, right_fk: str):
        """
        Performs a many-to-many insert via stored procedure.
        :param left_table: left entity table name
        :param left_lookup_col: column to look up left entity
        :param left_lookup_val: value to find left entity
        :param right_table: right entity table name
        :param right_lookup_col: column to look up right entity
        :param right_lookup_val: value to find right entity
        :param join_table: M2M join table name
        :param left_fk: foreign key column for left entity
        :param right_fk: foreign key column for right entity
        :return: None
        """
        return self._dao.join_insert(
            left_table, left_lookup_col, left_lookup_val,
            right_table, right_lookup_col, right_lookup_val,
            join_table, left_fk, right_fk
        )
