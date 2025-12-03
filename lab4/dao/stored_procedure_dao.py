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
        :return: Dict containing status, message, rows_affected, and table_name
        """
        sql = text("CALL generic_insert(:p_table, :p_columns, :p_values)")
        result = self._session.execute(sql, {
            'p_table': table,
            'p_columns': columns,
            'p_values': values
        })
        row = result.fetchone()
        self._session.commit()

        if row:
            return {
                'status': row[0],
                'message': row[1],
                'rows_affected': row[2],
                'table_name': row[3]
            }
        return None

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
        :return: Dict containing status, message, left_id, right_id, and join_table
        """
        sql = text("""CALL join_insert(
            :p_left_table, :p_left_lookup_col, :p_left_lookup_val,
            :p_right_table, :p_right_lookup_col, :p_right_lookup_val,
            :p_join_table, :p_left_fk, :p_right_fk
        )""")
        result = self._session.execute(sql, {
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
        row = result.fetchone()
        self._session.commit()

        if row:
            return {
                'status': row[0],
                'message': row[1],
                'left_id': row[2],
                'right_id': row[3],
                'join_table': row[4]
            }
        return None

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

    def split_table_random(self, table: str):
        """
        Calls the split_table_random stored procedure.
        Splits a table randomly into two new tables with timestamp suffixes.
        :param table: table name to split (must have 'id' column)
        :return: Dict containing status, message, original_table, table names and row counts
        """
        sql = text("CALL split_table_random(:p_table)")
        result = self._session.execute(sql, {'p_table': table})
        row = result.fetchone()
        self._session.commit()

        if row:
            return {
                'status': row[0],
                'message': row[1],
                'original_table': row[2],
                'table1_name': row[3],
                'table1_rows': row[4],
                'table2_name': row[5],
                'table2_rows': row[6]
            }
        return None
