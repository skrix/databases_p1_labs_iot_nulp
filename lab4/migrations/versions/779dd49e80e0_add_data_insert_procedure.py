"""add data insert procedure

Revision ID: 779dd49e80e0
Revises: b9c52d77ecbd
Create Date: 2025-11-23 17:48:29.623927

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '779dd49e80e0'
down_revision = 'b9c52d77ecbd'
branch_labels = None
depends_on = None


def upgrade():
    op.execute("""
    CREATE PROCEDURE noname_insert(
        IN p_table VARCHAR(64),
        IN p_column VARCHAR(64)
    )
    BEGIN
        DECLARE idx INT DEFAULT 1;

        WHILE idx <= 10 DO
            SET @sql = CONCAT(
                'INSERT INTO ', p_table, ' (', p_column, ') ',
                'VALUES ("Noname', idx, '")'
            );

            PREPARE stmt FROM @sql;
            EXECUTE stmt;
            DEALLOCATE PREPARE stmt;

            SET idx = idx + 1;
        END WHILE;
    END
    """)


def downgrade():
    op.execute("""
    DROP PROCEDURE IF EXISTS noname_insert;
    """)
