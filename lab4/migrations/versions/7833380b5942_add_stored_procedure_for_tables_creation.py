"""add stored procedure for tables creation

Revision ID: 7833380b5942
Revises: 40322e2767d1
Create Date: 2025-11-23 19:36:54.856166

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '7833380b5942'
down_revision = '40322e2767d1'
branch_labels = None
depends_on = None


def upgrade():
    op.execute("""
    CREATE PROCEDURE split_table_random(
        IN p_parent_table VARCHAR(64)
    )
    BEGIN
        DECLARE v_id INT;
        DECLARE done INT DEFAULT FALSE;
        DECLARE ts VARCHAR(20);
        DECLARE v_count_t1 INT DEFAULT 0;
        DECLARE v_count_t2 INT DEFAULT 0;

        -- Generate timestamp suffix
        SET ts = UNIX_TIMESTAMP();

        -- Build dynamic table names
        SET @t1 = CONCAT(p_parent_table, '_clone_', ts, '_1');
        SET @t2 = CONCAT(p_parent_table, '_clone_', ts, '_2');

        -- Create table 1 (clone structure from parent)
        SET @sql = CONCAT('CREATE TABLE ', @t1, ' LIKE ', p_parent_table);
        PREPARE stmt FROM @sql;
        EXECUTE stmt;
        DEALLOCATE PREPARE stmt;

        -- Create table 2 (clone structure from parent)
        SET @sql = CONCAT('CREATE TABLE ', @t2, ' LIKE ', p_parent_table);
        PREPARE stmt FROM @sql;
        EXECUTE stmt;
        DEALLOCATE PREPARE stmt;

        -- Create temporary table with IDs
        DROP TEMPORARY TABLE IF EXISTS tmp_ids;

        SET @tmp = CONCAT('CREATE TEMPORARY TABLE tmp_ids AS SELECT id FROM ', p_parent_table);
        PREPARE st2 FROM @tmp;
        EXECUTE st2;
        DEALLOCATE PREPARE st2;

        -- Declare cursor and handler
        BEGIN
            DECLARE cur2 CURSOR FOR SELECT id FROM tmp_ids;
            DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;

            OPEN cur2;

            read_loop: LOOP
                FETCH cur2 INTO v_id;
                IF done THEN
                    LEAVE read_loop;
                END IF;

                -- Randomly insert into one of the two tables
                IF RAND() < 0.5 THEN
                    SET @sql_ins = CONCAT(
                        'INSERT INTO ', @t1, ' SELECT * FROM ', p_parent_table, ' WHERE id = ', v_id
                    );
                ELSE
                    SET @sql_ins = CONCAT(
                        'INSERT INTO ', @t2, ' SELECT * FROM ', p_parent_table, ' WHERE id = ', v_id
                    );
                END IF;

                PREPARE stmt_ins FROM @sql_ins;
                EXECUTE stmt_ins;
                DEALLOCATE PREPARE stmt_ins;

            END LOOP;

            CLOSE cur2;
        END;

        DROP TEMPORARY TABLE IF EXISTS tmp_ids;

        -- Get counts from both tables
        SET @sql_count1 = CONCAT('SELECT COUNT(*) INTO @cnt1 FROM ', @t1);
        PREPARE stmt_count1 FROM @sql_count1;
        EXECUTE stmt_count1;
        DEALLOCATE PREPARE stmt_count1;

        SET @sql_count2 = CONCAT('SELECT COUNT(*) INTO @cnt2 FROM ', @t2);
        PREPARE stmt_count2 FROM @sql_count2;
        EXECUTE stmt_count2;
        DEALLOCATE PREPARE stmt_count2;

        SET v_count_t1 = @cnt1;
        SET v_count_t2 = @cnt2;

        SELECT
            'success' AS status,
            CONCAT('Successfully split table ', p_parent_table, ' into 2 tables') AS message,
            p_parent_table AS original_table,
            @t1 AS table1_name,
            v_count_t1 AS table1_rows,
            @t2 AS table2_name,
            v_count_t2 AS table2_rows;
    END
    """)


def downgrade():
    op.execute("""
    DROP PROCEDURE IF EXISTS split_table_random;
    """)
