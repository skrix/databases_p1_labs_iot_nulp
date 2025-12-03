"""add custom function procedure

Revision ID: 40322e2767d1
Revises: b9c52d77ecbd
Create Date: 2025-11-23 17:55:35.330852

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '40322e2767d1'
down_revision = 'b9c52d77ecbd'
branch_labels = None
depends_on = None


def upgrade():
    op.execute("""
    CREATE PROCEDURE get_stat(
        IN p_table VARCHAR(64),
        IN p_column VARCHAR(64),
        IN p_stat VARCHAR(10)
    )
    BEGIN
        SET @sql_text = CONCAT(
            'SELECT ', p_stat, '(', p_column, ') AS result ',
            'FROM ', p_table
        );

        PREPARE stmt FROM @sql_text;
        EXECUTE stmt;
        DEALLOCATE PREPARE stmt;
    END
    """)


def downgrade():
    op.execute("DROP PROCEDURE IF EXISTS get_stat;")
