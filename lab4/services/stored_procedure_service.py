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
