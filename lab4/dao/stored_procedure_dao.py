from sqlalchemy import text


class StoredProcedureDAO:
    """
    Data Access Object for calling stored procedures.
    """

    def __init__(self, session):
        self._session = session

    def generic_insert(self, table: str, columns: str, values: str):
        """
        Calls the generic_insert stored procedure.
        :param table: table name
        :param columns: comma-separated column names
        :param values: comma-separated values (quoted as needed)
        :return: None
        """
        sql = text("CALL generic_insert(:p_table, :p_columns, :p_values)")
        self._session.execute(sql, {
            'p_table': table,
            'p_columns': columns,
            'p_values': values
        })
        self._session.commit()
