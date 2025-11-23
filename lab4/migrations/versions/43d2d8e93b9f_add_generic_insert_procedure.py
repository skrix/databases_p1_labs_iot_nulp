"""add generic insert procedure

Revision ID: 43d2d8e93b9f
Revises: 3ab5eb690caf
Create Date: 2025-11-23 16:46:04.855138

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '43d2d8e93b9f'
down_revision = '3ab5eb690caf'
branch_labels = None
depends_on = None


def upgrade():
    op.execute("""
      CREATE PROCEDURE generic_insert(
          IN p_table VARCHAR(64),
          IN p_columns TEXT,
          IN p_values TEXT
      )
      BEGIN
          SET @sql = CONCAT(
              'INSERT INTO ', p_table, ' (', p_columns, ') ',
              'VALUES (', p_values, ');'
          );

          PREPARE stmt FROM @sql;
          EXECUTE stmt;
          DEALLOCATE PREPARE stmt;
      END
    """)


def downgrade():
    op.execute("""
      DROP PROCEDURE IF EXISTS generic_insert;
    """)
