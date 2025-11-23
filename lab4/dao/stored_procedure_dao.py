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

    def join_insert(self, left_table: str, left_lookup_col: str, left_lookup_val: str,
                        right_table: str, right_lookup_col: str, right_lookup_val: str,
                        join_table: str, left_fk: str, right_fk: str):
        """
        Calls the join_insert stored procedure.
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
        sql = text("""CALL join_insert(
            :p_left_table, :p_left_lookup_col, :p_left_lookup_val,
            :p_right_table, :p_right_lookup_col, :p_right_lookup_val,
            :p_join_table, :p_left_fk, :p_right_fk
        )""")
        self._session.execute(sql, {
            'p_left_table': left_table,
            'p_left_lookup_col': left_lookup_col,
            'p_left_lookup_val': left_lookup_val,
            'p_right_table': right_table,
            'p_right_lookup_col': right_lookup_col,
            'p_right_lookup_val': right_lookup_val,
            'p_join_table': join_table,
            'p_left_fk': left_fk,
            'p_right_fk': right_fk
        })
        self._session.commit()

    def noname_insert(self, table: str, column: str):
        """
        Calls the noname_insert stored procedure.
        Inserts 10 rows with values 'Noname1' through 'Noname10'.
        :param table: table name
        :param column: column name to insert into
        :return: None
        """
        sql = text("CALL noname_insert(:p_table, :p_column)")
        self._session.execute(sql, {
            'p_table': table,
            'p_column': column
        })
        self._session.commit()

    def get_stat(self, table: str, column: str, stat_type: str):
        """
        Calls the get_stat stored procedure to calculate statistics.
        :param table: table name
        :param column: column name to calculate stat on
        :param stat_type: type of statistic (SUM, AVG, COUNT, MIN, MAX)
        :return: Decimal value of the calculated statistic
        """
        sql = text("CALL get_stat(:p_table, :p_column, :p_stat)")
        result = self._session.execute(sql, {
            'p_table': table,
            'p_column': column,
            'p_stat': stat_type
        })
        row = result.fetchone()
        return float(row[0]) if row else None
