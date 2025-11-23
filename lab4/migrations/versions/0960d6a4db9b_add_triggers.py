"""add triggers

Revision ID: xxxx
Revises: yyyy
Create Date: 2025-11-22
"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '0960d6a4db9b'
down_revision = '7833380b5942'
branch_labels = None
depends_on = None


def upgrade():
    # '45000' - MySQL code for unhandled user-defined exception.
    op.execute("""
    CREATE TRIGGER trg_vehicle_plate_length_insert
    BEFORE INSERT ON vehicles
    FOR EACH ROW
    BEGIN
        IF CHAR_LENGTH(NEW.plate) < 2 OR CHAR_LENGTH(NEW.plate) > 10 THEN
            SIGNAL SQLSTATE '45000'
                SET MESSAGE_TEXT = 'Vehicle plate must be 2 to 10 characters long';
        END IF;
    END;
    """)

    op.execute("""
    CREATE TRIGGER trg_vehicle_plate_length_update
    BEFORE UPDATE ON vehicles
    FOR EACH ROW
    BEGIN
        IF CHAR_LENGTH(NEW.plate) < 2 OR CHAR_LENGTH(NEW.plate) > 10 THEN
            SIGNAL SQLSTATE '45000'
                SET MESSAGE_TEXT = 'Vehicle plate must be 2 to 10 characters long';
        END IF;
    END;
    """)

    # АВЕ-123-456
    # users.driver_license - format <3 letters (not M,R)> - <3 digits> - <3 digits>
    op.execute("""
    CREATE TRIGGER trg_driver_license_format_insert
    BEFORE INSERT ON users
    FOR EACH ROW
    BEGIN
        IF NEW.driver_license NOT REGEXP '^[A-LN-QS-Z]{3}-[0-9]{3}-[0-9]{3}$' THEN
            SIGNAL SQLSTATE '45000'
                SET MESSAGE_TEXT = 'Invalid driver_license format';
        END IF;
    END;
    """)

    op.execute("""
    CREATE TRIGGER trg_driver_license_format_update
    BEFORE UPDATE ON users
    FOR EACH ROW
    BEGIN
        IF NEW.driver_license NOT REGEXP '^[A-LN-QS-Z]{3}-[0-9]{3}-[0-9]{3}$' THEN
            SIGNAL SQLSTATE '45000'
                SET MESSAGE_TEXT = 'Invalid driver_license format';
        END IF;
    END;
    """)

    # payments delete log
    op.execute("""
    CREATE TABLE payments_delete_log (
        id INT AUTO_INCREMENT PRIMARY KEY,
        deleted_payment_id INT NOT NULL,
        deleted_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """)

    op.execute("""
    CREATE TRIGGER trg_payments_delete_log
    AFTER DELETE ON payments
    FOR EACH ROW
    BEGIN
        INSERT INTO payments_delete_log (deleted_payment_id)
        VALUES (OLD.id);
    END;
    """)


def downgrade():
    op.execute("DROP TRIGGER IF EXISTS trg_vehicle_plate_length_insert;")
    op.execute("DROP TRIGGER IF EXISTS trg_vehicle_plate_length_update;")
    op.execute("DROP TRIGGER IF EXISTS trg_driver_license_format_insert;")
    op.execute("DROP TRIGGER IF EXISTS trg_driver_license_format_update;")
    op.execute("DROP TRIGGER IF EXISTS trg_payments_delete_log;")
    op.execute("DROP TABLE IF EXISTS payments_delete_log;")
