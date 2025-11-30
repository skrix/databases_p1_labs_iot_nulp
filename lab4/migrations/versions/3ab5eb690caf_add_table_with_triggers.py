"""add user_notes table with triggers (no FK)

Revision ID: 3ab5eb690caf
Revises: 2d7b5a031e2a
Create Date: 2025-11-22 17:02:35.420172

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers
revision = '3ab5eb690caf'
down_revision = '2d7b5a031e2a'
branch_labels = None
depends_on = None


def upgrade():
    # 1. Create table without foreign keys
    op.execute("""
        CREATE TABLE user_notes (
            id INT AUTO_INCREMENT PRIMARY KEY,
            user_id INT NOT NULL,
            note TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
    """)

    # 2. Trigger: Validate user exists on INSERT
    op.execute("""
        CREATE TRIGGER trg_user_notes_before_insert
        BEFORE INSERT ON user_notes
        FOR EACH ROW
        BEGIN
            IF (SELECT COUNT(*) FROM users WHERE id = NEW.user_id) = 0 THEN
                SIGNAL SQLSTATE '45000'
                    SET MESSAGE_TEXT = 'Invalid user_id: user does not exist.';
            END IF;
        END;
    """)

    # 3. Trigger: Validate user exists on UPDATE
    op.execute("""
        CREATE TRIGGER trg_user_notes_before_update
        BEFORE UPDATE ON user_notes
        FOR EACH ROW
        BEGIN
            IF NEW.user_id IS NULL THEN
                SIGNAL SQLSTATE '45000'
                    SET MESSAGE_TEXT = 'user_id cannot be NULL.';
            END IF;

            IF (SELECT COUNT(*) FROM users WHERE id = NEW.user_id) = 0 THEN
                SIGNAL SQLSTATE '45000'
                    SET MESSAGE_TEXT = 'Invalid user_id on UPDATE: user does not exist.';
            END IF;
        END;
    """)

    # 4. Trigger: Prevent deletion of user with notes
    op.execute("""
        CREATE TRIGGER trg_users_before_delete
        BEFORE DELETE ON users
        FOR EACH ROW
        BEGIN
            IF (SELECT COUNT(*) FROM user_notes WHERE user_id = OLD.id) > 0 THEN
                SIGNAL SQLSTATE '45000'
                    SET MESSAGE_TEXT = 'Cannot delete user: user_notes exist.';
            END IF;
        END;
    """)


def downgrade():
    # Drop triggers
    op.execute("DROP TRIGGER IF EXISTS trg_user_notes_before_insert;")
    op.execute("DROP TRIGGER IF EXISTS trg_user_notes_before_update;")
    op.execute("DROP TRIGGER IF EXISTS trg_users_before_delete;")

    # Drop table
    op.execute("DROP TABLE IF EXISTS user_notes;")
