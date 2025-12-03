"""add join insert procedure

Revision ID: b9c52d77ecbd
Revises: 43d2d8e93b9f
Create Date: 2025-11-23 17:23:18.843832

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'b9c52d77ecbd'
down_revision = '43d2d8e93b9f'
branch_labels = None
depends_on = None


def upgrade():
    op.execute("""
    CREATE PROCEDURE join_insert(
        IN p_left_table VARCHAR(64),
        IN p_left_lookup_col VARCHAR(64),
        IN p_left_lookup_val VARCHAR(255),

        IN p_right_table VARCHAR(64),
        IN p_right_lookup_col VARCHAR(64),
        IN p_right_lookup_val VARCHAR(255),

        IN p_join_table VARCHAR(64),
        IN p_left_fk VARCHAR(64),
        IN p_right_fk VARCHAR(64)
    )
    BEGIN
        DECLARE v_left_id INT;
        DECLARE v_right_id INT;

        -- Find left ID dynamically
        SET @sql_left = CONCAT(
            'SELECT id INTO @lid FROM ', p_left_table,
            ' WHERE ', p_left_lookup_col, ' = ''', p_left_lookup_val, ''' LIMIT 1'
        );
        PREPARE stmt_left FROM @sql_left;
        EXECUTE stmt_left;
        DEALLOCATE PREPARE stmt_left;

        SET v_left_id = @lid;

        IF v_left_id IS NULL THEN
            SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Left-side entity does not exist';
        END IF;

        -- Find right ID dynamically
        SET @sql_right = CONCAT(
            'SELECT id INTO @rid FROM ', p_right_table,
            ' WHERE ', p_right_lookup_col, ' = ''', p_right_lookup_val, ''' LIMIT 1'
        );
        PREPARE stmt_right FROM @sql_right;
        EXECUTE stmt_right;
        DEALLOCATE PREPARE stmt_right;

        SET v_right_id = @rid;

        IF v_right_id IS NULL THEN
            SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Right-side entity does not exist';
        END IF;

        -- Check if relation already exists
        SET @sql_exists = CONCAT(
            'SELECT COUNT(*) INTO @exists FROM ', p_join_table,
            ' WHERE ', p_left_fk, ' = ', v_left_id,
            ' AND ', p_right_fk, ' = ', v_right_id
        );
        PREPARE stmt_exists FROM @sql_exists;
        EXECUTE stmt_exists;
        DEALLOCATE PREPARE stmt_exists;

        IF @exists > 0 THEN
            SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Relation already exists';
        END IF;

        -- Insert into M2M table
        SET @sql_insert = CONCAT(
            'INSERT INTO ', p_join_table,
            ' (', p_left_fk, ', ', p_right_fk, ') VALUES (',
            v_left_id, ', ', v_right_id, ')'
        );
        PREPARE stmt_insert FROM @sql_insert;
        EXECUTE stmt_insert;
        DEALLOCATE PREPARE stmt_insert;

        SELECT
            'success' AS status,
            CONCAT('Successfully created relation between ', p_left_table, ' (id=', v_left_id, ') and ', p_right_table, ' (id=', v_right_id, ')') AS message,
            v_left_id AS left_id,
            v_right_id AS right_id,
            p_join_table AS join_table;

    END
    """)


def downgrade():
    op.execute("""
    DROP PROCEDURE IF EXISTS join_insert;
    """)
