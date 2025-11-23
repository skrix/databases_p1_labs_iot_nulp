from services.stored_procedure_service import StoredProcedureService


class StoredProcedureController:
    """
    Controller for handling stored procedure requests.
    """

    def __init__(self, session):
        self._service = StoredProcedureService(session)

    def generic_insert(self, table: str, columns: str, values: str):
        """
        Performs a generic insert via stored procedure.
        :param table: table name
        :param columns: comma-separated column names
        :param values: comma-separated values (quoted as needed)
        :return: None
        """
        return self._service.generic_insert(table, columns, values)
