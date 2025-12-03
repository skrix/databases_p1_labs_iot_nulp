"""Initial migration

Revision ID: 2d7b5a031e2a
Revises:
Create Date: 2025-11-22 16:37:43.964801

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '2d7b5a031e2a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # Drop existing tables if they exist
    op.execute("DROP TABLE IF EXISTS `fines_payments`;")
    op.execute("DROP TABLE IF EXISTS `rentings_payments`;")
    op.execute("DROP TABLE IF EXISTS `rentings_fines`;")
    op.execute("DROP TABLE IF EXISTS `rentings`;")
    op.execute("DROP TABLE IF EXISTS `parkings_vehicles`;")
    op.execute("DROP TABLE IF EXISTS `payments`;")
    op.execute("DROP TABLE IF EXISTS `fines`;")
    op.execute("DROP TABLE IF EXISTS `vehicles`;")
    op.execute("DROP TABLE IF EXISTS `parkings`;")
    op.execute("DROP TABLE IF EXISTS `users`;")

    # Create tables - each table in separate execute to avoid MySQL multi-statement issues
    op.create_table(
        'parkings',
        sa.Column('id', sa.Integer(), nullable=False, autoincrement=True),
        sa.Column('address', sa.String(255), nullable=True),
        sa.Column('country', sa.String(100), nullable=True),
        sa.Column('city', sa.String(100), nullable=True),
        sa.Column('latitude', sa.DECIMAL(11, 8), nullable=False),
        sa.Column('longitude', sa.DECIMAL(11, 8), nullable=False),
        sa.PrimaryKeyConstraint('id'),
        mysql_engine='InnoDB'
    )

    op.create_table(
        'vehicles',
        sa.Column('id', sa.Integer(), nullable=False, autoincrement=True),
        sa.Column('make', sa.String(100), nullable=False),
        sa.Column('model', sa.String(100), nullable=False),
        sa.Column('year', sa.Integer(), nullable=False),
        sa.Column('vin', sa.String(17), nullable=False),
        sa.Column('body', mysql.ENUM('sedan', 'hatchback', 'wagon', 'coupe', 'convertible', 'roadster', 'suv', 'crossover', 'pickup', 'van', 'minivan', 'truck', 'camper'), nullable=False, server_default='sedan'),
        sa.Column('plate', sa.String(15), nullable=False),
        sa.PrimaryKeyConstraint('id'),
        mysql_engine='InnoDB'
    )

    op.create_table(
        'users',
        sa.Column('id', sa.Integer(), nullable=False, autoincrement=True),
        sa.Column('first_name', sa.String(100), nullable=False),
        sa.Column('middle_name', sa.String(100), nullable=True),
        sa.Column('last_name', sa.String(100), nullable=False),
        sa.Column('dob', sa.Date(), nullable=False),
        sa.Column('email', sa.String(255), nullable=False),
        sa.Column('password', sa.String(255), nullable=False),
        sa.Column('created_at', sa.TIMESTAMP(), nullable=False, server_default=sa.text('CURRENT_TIMESTAMP')),
        sa.Column('driver_license', sa.String(255), nullable=False),
        sa.Column('gender', mysql.ENUM('male', 'female', 'other', 'prefer_not_to_say'), nullable=False),
        sa.PrimaryKeyConstraint('id'),
        mysql_engine='InnoDB'
    )

    op.create_table(
        'parkings_vehicles',
        sa.Column('id', sa.Integer(), nullable=False, autoincrement=True),
        sa.Column('parking_id', sa.Integer(), nullable=False),
        sa.Column('vehicle_id', sa.Integer(), nullable=False),
        sa.Column('created_at', sa.TIMESTAMP(), nullable=False, server_default=sa.text('CURRENT_TIMESTAMP')),
        sa.Column('updated_at', sa.TIMESTAMP(), nullable=False, server_default=sa.text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP')),
        sa.PrimaryKeyConstraint('id'),
        mysql_engine='InnoDB'
    )

    op.create_table(
        'rentings',
        sa.Column('id', sa.Integer(), nullable=False, autoincrement=True),
        sa.Column('user_id', sa.Integer(), nullable=False),
        sa.Column('vehicle_id', sa.Integer(), nullable=False),
        sa.Column('created_at', sa.TIMESTAMP(), nullable=False, server_default=sa.text('CURRENT_TIMESTAMP')),
        sa.Column('updated_at', sa.TIMESTAMP(), nullable=False, server_default=sa.text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP')),
        sa.Column('start_at', sa.DateTime(), nullable=False),
        sa.Column('end_at', sa.DateTime(), nullable=True),
        sa.PrimaryKeyConstraint('id'),
        mysql_engine='InnoDB'
    )

    op.create_table(
        'payments',
        sa.Column('id', sa.Integer(), nullable=False, autoincrement=True),
        sa.Column('created_at', sa.TIMESTAMP(), nullable=False, server_default=sa.text('CURRENT_TIMESTAMP')),
        sa.Column('updated_at', sa.TIMESTAMP(), nullable=False, server_default=sa.text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP')),
        sa.Column('status', mysql.ENUM('pending', 'paid', 'failed', 'refunded'), nullable=False, server_default='pending'),
        sa.Column('amount', sa.DECIMAL(10, 2), nullable=False),
        sa.Column('currency', mysql.ENUM('USD', 'EUR', 'UAH'), nullable=False, server_default='USD'),
        sa.PrimaryKeyConstraint('id'),
        mysql_engine='InnoDB'
    )

    op.create_table(
        'fines',
        sa.Column('id', sa.Integer(), nullable=False, autoincrement=True),
        sa.Column('created_at', sa.TIMESTAMP(), nullable=False, server_default=sa.text('CURRENT_TIMESTAMP')),
        sa.Column('updated_at', sa.TIMESTAMP(), nullable=False, server_default=sa.text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP')),
        sa.Column('status', mysql.ENUM('paid', 'unpaid', 'disputed', 'waived'), nullable=False, server_default='unpaid'),
        sa.Column('amount', sa.DECIMAL(10, 2), nullable=False),
        sa.Column('currency', mysql.ENUM('USD', 'EUR', 'UAH'), nullable=False, server_default='USD'),
        sa.Column('violation', sa.String(255), nullable=False),
        sa.PrimaryKeyConstraint('id'),
        mysql_engine='InnoDB'
    )

    op.create_table(
        'rentings_fines',
        sa.Column('id', sa.Integer(), nullable=False, autoincrement=True),
        sa.Column('renting_id', sa.Integer(), nullable=False),
        sa.Column('fine_id', sa.Integer(), nullable=False),
        sa.Column('created_at', sa.TIMESTAMP(), nullable=False, server_default=sa.text('CURRENT_TIMESTAMP')),
        sa.Column('updated_at', sa.TIMESTAMP(), nullable=False, server_default=sa.text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP')),
        sa.PrimaryKeyConstraint('id'),
        mysql_engine='InnoDB'
    )

    op.create_table(
        'rentings_payments',
        sa.Column('id', sa.Integer(), nullable=False, autoincrement=True),
        sa.Column('renting_id', sa.Integer(), nullable=False),
        sa.Column('payment_id', sa.Integer(), nullable=False),
        sa.Column('created_at', sa.TIMESTAMP(), nullable=False, server_default=sa.text('CURRENT_TIMESTAMP')),
        sa.Column('updated_at', sa.TIMESTAMP(), nullable=False, server_default=sa.text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP')),
        sa.PrimaryKeyConstraint('id'),
        mysql_engine='InnoDB'
    )

    op.create_table(
        'fines_payments',
        sa.Column('id', sa.Integer(), nullable=False, autoincrement=True),
        sa.Column('fine_id', sa.Integer(), nullable=False),
        sa.Column('payment_id', sa.Integer(), nullable=False),
        sa.Column('created_at', sa.TIMESTAMP(), nullable=False, server_default=sa.text('CURRENT_TIMESTAMP')),
        sa.Column('updated_at', sa.TIMESTAMP(), nullable=False, server_default=sa.text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP')),
        sa.PrimaryKeyConstraint('id'),
        mysql_engine='InnoDB'
    )

    # Add indexes
    op.create_index('latitude_longitude_UNIQUE', 'parkings', ['latitude', 'longitude'], unique=True)
    op.create_index('address_idx', 'parkings', ['address'])
    op.create_index('country_idx', 'parkings', ['country'])
    op.create_index('city_idx', 'parkings', ['city'])

    op.create_index('vin_UNIQUE', 'vehicles', ['vin'], unique=True)
    op.create_index('plate_UNIQUE', 'vehicles', ['plate'], unique=True)
    op.create_index('make_idx', 'vehicles', ['make'])
    op.create_index('model_idx', 'vehicles', ['model'])
    op.create_index('year_idx', 'vehicles', ['year'])
    op.create_index('body_year_idx', 'vehicles', ['body', 'year'])

    op.create_index('email_UNIQUE', 'users', ['email'], unique=True)
    op.create_index('driver_license_UNIQUE', 'users', ['driver_license'], unique=True)
    op.create_index('first_name_idx', 'users', ['first_name'])
    op.create_index('last_name_idx', 'users', ['last_name'])
    op.create_index('dob_idx', 'users', ['dob'])

    op.create_index('parking_id_idx', 'parkings_vehicles', ['parking_id'])
    op.create_index('vehicle_id_idx', 'parkings_vehicles', ['vehicle_id'])
    op.create_index('parking_vehicle_UNIQUE', 'parkings_vehicles', ['parking_id', 'vehicle_id'], unique=True)

    op.create_index('vehicle_id_idx', 'rentings', ['vehicle_id'])
    op.create_index('user_id_idx', 'rentings', ['user_id'])
    op.create_index('start_at_idx', 'rentings', ['start_at'])
    op.create_index('end_at_idx', 'rentings', ['end_at'])
    op.create_index('user_start_idx', 'rentings', ['user_id', 'start_at'])

    op.create_index('status_idx', 'payments', ['status'])
    op.create_index('created_at_idx', 'payments', ['created_at'])

    op.create_index('status_idx', 'fines', ['status'])
    op.create_index('created_at_idx', 'fines', ['created_at'])

    op.create_index('renting_fine_UNIQUE', 'rentings_fines', ['renting_id', 'fine_id'], unique=True)
    op.create_index('fine_id_idx', 'rentings_fines', ['fine_id'])
    op.create_index('renting_id_idx', 'rentings_fines', ['renting_id'])

    op.create_index('renting_payment_UNIQUE', 'rentings_payments', ['renting_id', 'payment_id'], unique=True)
    op.create_index('renting_id_idx', 'rentings_payments', ['renting_id'])
    op.create_index('payment_id_idx', 'rentings_payments', ['payment_id'])

    op.create_index('fine_payment_UNIQUE', 'fines_payments', ['fine_id', 'payment_id'], unique=True)
    op.create_index('fine_id_idx', 'fines_payments', ['fine_id'])
    op.create_index('payment_id_idx', 'fines_payments', ['payment_id'])

    # Add foreign keys
    op.create_foreign_key('parking_vehicle_parking_id', 'parkings_vehicles', 'parkings', ['parking_id'], ['id'], ondelete='CASCADE', onupdate='CASCADE')
    op.create_foreign_key('parking_vehicle_vehicle_id', 'parkings_vehicles', 'vehicles', ['vehicle_id'], ['id'], ondelete='CASCADE', onupdate='CASCADE')

    op.create_foreign_key('renting_user_id', 'rentings', 'users', ['user_id'], ['id'], ondelete='RESTRICT', onupdate='CASCADE')
    op.create_foreign_key('renting_vehicle_id', 'rentings', 'vehicles', ['vehicle_id'], ['id'], ondelete='RESTRICT', onupdate='CASCADE')

    op.create_foreign_key('renting_fine_renting_id', 'rentings_fines', 'rentings', ['renting_id'], ['id'], ondelete='CASCADE', onupdate='CASCADE')
    op.create_foreign_key('renting_fine_fine_id', 'rentings_fines', 'fines', ['fine_id'], ['id'], ondelete='CASCADE', onupdate='CASCADE')

    op.create_foreign_key('renting_payment_renting_id', 'rentings_payments', 'rentings', ['renting_id'], ['id'], ondelete='CASCADE', onupdate='CASCADE')
    op.create_foreign_key('renting_payment_payment_id', 'rentings_payments', 'payments', ['payment_id'], ['id'], ondelete='CASCADE', onupdate='CASCADE')

    op.create_foreign_key('fine_payment_fine_id', 'fines_payments', 'fines', ['fine_id'], ['id'], ondelete='CASCADE', onupdate='CASCADE')
    op.create_foreign_key('fine_payment_payment_id', 'fines_payments', 'payments', ['payment_id'], ['id'], ondelete='CASCADE', onupdate='CASCADE')

    # Insert seed data
    op.execute("""
      INSERT INTO `parkings` (`address`, `country`, `city`, `latitude`, `longitude`) VALUES
      ('вул. Хрещатик 22', 'Ukraine', 'Kyiv', 50.45010000, 30.52340000),
      ('пр. Свободи 15', 'Ukraine', 'Lviv', 49.83826000, 24.02324000),
      ('вул. Дерибасівська 10', 'Ukraine', 'Odesa', 46.48572000, 30.74383000),
      ('пр. Соборний 45', 'Ukraine', 'Dnipro', 48.46477000, 35.04617000),
      ('вул. Сумська 30', 'Ukraine', 'Kharkiv', 49.98081000, 36.25272000),
      ('вул. Соборна 25', 'Ukraine', 'Vinnytsia', 49.23316000, 28.46798000),
      ('вул. Центральна 18', 'Ukraine', 'Lutsk', 50.74723000, 25.32538000),
      ('пр. Незалежності 50', 'Ukraine', 'Ivano-Frankivsk', 48.92264000, 24.71111000),
      ('вул. Театральна 12', 'Ukraine', 'Ternopil', 49.55351000, 25.59476000),
      ('вул. Шевченка 8', 'Ukraine', 'Poltava', 49.58826000, 34.55141000);
    """)

    op.execute("""
      INSERT INTO `vehicles` (`make`, `model`, `year`, `vin`, `body`, `plate`) VALUES
      ('Renault', 'Logan', 2023, '1HGBH41JXMN109186', 'sedan', 'AA1234KM'),
      ('Skoda', 'Octavia', 2023, '2HGBH41JXMN109187', 'sedan', 'AB5678BI'),
      ('Volkswagen', 'Passat', 2022, '3HGBH41JXMN109188', 'sedan', 'AC9012OD'),
      ('Toyota', 'Camry', 2023, '4HGBH41JXMN109189', 'sedan', 'AE3456DP'),
      ('Volkswagen', 'Golf', 2022, '5HGBH41JXMN109190', 'hatchback', 'AI7890KH'),
      ('Hyundai', 'Elantra', 2023, '6HGBH41JXMN109191', 'sedan', 'AK2345VN'),
      ('Kia', 'Sportage', 2022, '7HGBH41JXMN109192', 'suv', 'AM6789LT'),
      ('Toyota', 'RAV4', 2023, '8HGBH41JXMN109193', 'suv', 'AO0123IF'),
      ('Honda', 'CR-V', 2023, '9HGBH41JXMN109194', 'suv', 'AP4567TE'),
      ('Mazda', 'CX-5', 2022, 'AHGBH41JXMN109195', 'crossover', 'AT8901PT'),
      ('Nissan', 'Qashqai', 2023, 'BHGBH41JXMN109196', 'crossover', 'AX2345KM'),
      ('Renault', 'Duster', 2022, 'CHGBH41JXMN109197', 'suv', 'BC6789BI'),
      ('Skoda', 'Superb', 2023, 'DHGBH41JXMN109198', 'sedan', 'BH0123OD'),
      ('BMW', 'X5', 2023, 'EHGBH41JXMN109199', 'suv', 'BK4567DP'),
      ('Mercedes-Benz', 'E-Class', 2022, 'FHGBH41JXMN109200', 'sedan', 'BM8901KH'),
      ('Audi', 'A6', 2023, 'GHGBH41JXMN109201', 'sedan', 'BO2345VN'),
      ('Ford', 'Transit', 2023, 'HHGBH41JXMN109202', 'van', 'BT6789LT'),
      ('Volkswagen', 'Transporter', 2022, 'IHGBH41JXMN109203', 'van', 'BX0123IF'),
      ('Hyundai', 'Santa Fe', 2023, 'JHGBH41JXMN109204', 'suv', 'CA4567TE'),
      ('Kia', 'Sorento', 2022, 'KHGBH41JXMN109205', 'suv', 'CE8901PT');
    """)

    op.execute("""
      INSERT INTO `users` (`first_name`, `middle_name`, `last_name`, `dob`, `email`, `password`, `driver_license`, `gender`) VALUES
      ('Олександр', 'Іванович', 'Шевченко', '1985-03-15', 'o.shevchenko@email.com', SHA2('password123', 256), 'ABC-123-456', 'male'),
      ('Олена', 'Петрівна', 'Коваленко', '1990-07-22', 'o.kovalenko@email.com', SHA2('password123', 256), 'ABC-223-456', 'female'),
      ('Дмитро', 'Сергійович', 'Мельник', '1982-11-08', 'd.melnyk@email.com', SHA2('password123', 256), 'ABC-323-456', 'male'),
      ('Марія', 'Андріївна', 'Бондаренко', '1995-04-30', 'm.bondarenko@email.com', SHA2('password123', 256), 'ABC-423-456', 'female'),
      ('Андрій', 'Миколайович', 'Ткаченко', '1988-09-12', 'a.tkachenko@email.com', SHA2('password123', 256), 'ABC-523-456', 'male'),
      ('Юлія', 'Олександрівна', 'Кравченко', '1992-01-25', 'y.kravchenko@email.com', SHA2('password123', 256), 'ABC-623-456', 'female'),
      ('Віктор', 'Васильович', 'Гончаренко', '1987-06-18', 'v.honcharenko@email.com', SHA2('password123', 256), 'ABC-723-456', 'male'),
      ('Тетяна', 'Володимирівна', 'Павленко', '1993-12-05', 't.pavlenko@email.com', SHA2('password123', 256), 'ABC-823-456', 'female'),
      ('Максим', 'Ігорович', 'Савченко', '1984-08-28', 'm.savchenko@email.com', SHA2('password123', 256), 'ABC-923-456', 'male'),
      ('Наталія', 'Олегівна', 'Романенко', '1991-02-14', 'n.romanenko@email.com', SHA2('password123', 256), 'DEF-123-456', 'female'),
      ('Сергій', 'Анатолійович', 'Лисенко', '1989-10-03', 's.lysenko@email.com', SHA2('password123', 256), 'DEF-223-456', 'male'),
      ('Анна', 'Михайлівна', 'Поліщук', '1994-05-19', 'a.polischuk@email.com', SHA2('password123', 256), 'DEF-323-456', 'female'),
      ('Ігор', 'Романович', 'Коваль', '1986-07-07', 'i.koval@email.com', SHA2('password123', 256), 'DEF-423-456', 'male'),
      ('Катерина', 'Ярославівна', 'Захарченко', '1996-11-22', 'k.zakharchenko@email.com', SHA2('password123', 256), 'DEF-523-456', 'female'),
      ('Володимир', 'Богданович', 'Білоус', '1983-03-11', 'v.bilous@email.com', SHA2('password123', 256), 'DEF-623-456', 'male');
    """)

    op.execute("""
      INSERT INTO `parkings_vehicles` (`parking_id`, `vehicle_id`, `created_at`, `updated_at`) VALUES
      (1, 1, '2024-01-01 10:00:00', '2024-01-01 10:00:00'),
      (1, 2, '2024-01-01 10:15:00', '2024-01-01 10:15:00'),
      (2, 3, '2024-01-01 11:00:00', '2024-01-01 11:00:00'),
      (2, 4, '2024-01-01 11:30:00', '2024-01-01 11:30:00'),
      (3, 5, '2024-01-01 12:00:00', '2024-01-01 12:00:00'),
      (3, 6, '2024-01-01 12:30:00', '2024-01-01 12:30:00'),
      (4, 7, '2024-01-01 13:00:00', '2024-01-01 13:00:00'),
      (4, 8, '2024-01-01 13:30:00', '2024-01-01 13:30:00'),
      (5, 9, '2024-01-01 14:00:00', '2024-01-01 14:00:00'),
      (5, 10, '2024-01-01 14:30:00', '2024-01-01 14:30:00'),
      (6, 11, '2024-01-01 15:00:00', '2024-01-01 15:00:00'),
      (6, 12, '2024-01-01 15:30:00', '2024-01-01 15:30:00'),
      (7, 13, '2024-01-01 16:00:00', '2024-01-01 16:30:00'),
      (7, 14, '2024-01-01 16:30:00', '2024-01-01 16:30:00'),
      (8, 15, '2024-01-01 17:00:00', '2024-01-01 17:00:00'),
      (8, 16, '2024-01-01 17:30:00', '2024-01-01 17:30:00'),
      (9, 17, '2024-01-01 18:00:00', '2024-01-01 18:00:00'),
      (9, 18, '2024-01-01 18:30:00', '2024-01-01 18:30:00'),
      (10, 19, '2024-01-01 19:00:00', '2024-01-01 19:00:00'),
      (10, 20, '2024-01-01 19:30:00', '2024-01-01 19:30:00'),
      (1, 3, '2024-02-01 10:00:00', '2024-02-01 10:00:00'),
      (1, 5, '2024-02-15 11:00:00', '2024-02-15 11:00:00'),
      (1, 7, '2024-09-28 10:00:00', '2024-09-28 10:00:00'),
      (2, 1, '2024-03-01 09:00:00', '2024-03-01 09:00:00'),
      (2, 7, '2024-03-10 14:00:00', '2024-03-10 14:00:00'),
      (3, 2, '2024-03-20 10:30:00', '2024-03-20 10:30:00'),
      (3, 9, '2024-04-01 11:00:00', '2024-04-01 11:00:00'),
      (4, 4, '2024-04-15 13:00:00', '2024-04-15 13:00:00'),
      (4, 11, '2024-05-01 10:00:00', '2024-05-01 10:00:00'),
      (5, 6, '2024-05-10 12:00:00', '2024-05-10 12:00:00'),
      (5, 13, '2024-06-01 09:00:00', '2024-06-01 09:00:00'),
      (6, 8, '2024-06-15 14:00:00', '2024-06-15 14:00:00'),
      (6, 15, '2024-07-01 10:00:00', '2024-07-01 10:00:00'),
      (7, 10, '2024-07-15 11:00:00', '2024-07-15 11:00:00'),
      (7, 16, '2024-08-01 13:00:00', '2024-08-01 13:00:00'),
      (8, 12, '2024-08-15 10:00:00', '2024-08-15 10:00:00'),
      (8, 18, '2024-09-01 12:00:00', '2024-09-01 12:00:00'),
      (9, 14, '2024-09-10 14:00:00', '2024-09-10 14:00:00'),
      (9, 20, '2024-09-20 11:00:00', '2024-09-20 11:00:00'),
      (10, 1, '2024-09-25 15:00:00', '2024-09-25 15:00:00');
    """)

    op.execute("""
      INSERT INTO `rentings` (`user_id`, `vehicle_id`, `created_at`, `updated_at`, `start_at`, `end_at`) VALUES
      (1, 1, '2024-06-01 09:00:00', '2024-06-05 16:00:00', '2024-06-01 10:00:00', '2024-06-05 15:00:00'),
      (2, 3, '2024-06-10 08:00:00', '2024-06-15 18:00:00', '2024-06-10 09:00:00', '2024-06-15 17:00:00'),
      (3, 5, '2024-07-01 07:00:00', '2024-07-10 19:00:00', '2024-07-01 08:00:00', '2024-07-10 18:00:00'),
      (4, 7, '2024-07-15 10:00:00', '2024-07-20 15:00:00', '2024-07-15 11:00:00', '2024-07-20 14:00:00'),
      (5, 9, '2024-08-01 11:00:00', '2024-08-07 17:00:00', '2024-08-01 12:00:00', '2024-08-07 16:00:00'),
      (6, 11, '2024-08-10 09:00:00', '2024-08-20 18:00:00', '2024-08-10 10:00:00', '2024-08-20 17:00:00'),
      (7, 13, '2024-09-01 08:00:00', '2024-09-10 16:00:00', '2024-09-01 09:00:00', '2024-09-10 15:00:00'),
      (8, 15, '2024-09-15 10:00:00', '2024-09-15 10:00:00', '2024-09-15 11:00:00', NULL),
      (9, 17, '2024-09-20 12:00:00', '2024-09-20 12:00:00', '2024-09-20 13:00:00', NULL),
      (10, 19, '2024-09-25 14:00:00', '2024-09-25 14:00:00', '2024-09-25 15:00:00', NULL),
      (11, 2, '2024-05-15 09:00:00', '2024-05-20 16:00:00', '2024-05-15 10:00:00', '2024-05-20 15:00:00'),
      (12, 4, '2024-06-20 10:00:00', '2024-06-25 17:00:00', '2024-06-20 11:00:00', '2024-06-25 16:00:00'),
      (13, 6, '2024-07-25 11:00:00', '2024-07-30 18:00:00', '2024-07-25 12:00:00', '2024-07-30 17:00:00'),
      (14, 8, '2024-08-25 08:00:00', '2024-08-25 08:00:00', '2024-08-25 09:00:00', NULL),
      (15, 10, '2024-09-28 13:00:00', '2024-09-28 13:00:00', '2024-09-28 14:00:00', NULL);
    """)

    op.execute("""
      INSERT INTO `payments` (`created_at`, `updated_at`, `status`, `amount`, `currency`) VALUES
      ('2024-06-01 09:00:00', '2024-06-01 09:05:00', 'paid', 12500.00, 'UAH'),
      ('2024-06-10 08:00:00', '2024-06-10 08:05:00', 'paid', 15800.00, 'UAH'),
      ('2024-07-01 07:00:00', '2024-07-01 07:05:00', 'paid', 890.00, 'EUR'),
      ('2024-07-15 10:00:00', '2024-07-15 10:05:00', 'paid', 9200.00, 'UAH'),
      ('2024-08-01 11:00:00', '2024-08-01 11:05:00', 'paid', 18500.00, 'UAH'),
      ('2024-08-10 09:00:00', '2024-08-10 09:05:00', 'paid', 1200.00, 'EUR'),
      ('2024-09-01 08:00:00', '2024-09-01 08:05:00', 'paid', 22000.00, 'UAH'),
      ('2024-09-15 10:00:00', '2024-09-15 10:00:00', 'pending', 19500.00, 'UAH'),
      ('2024-09-20 12:00:00', '2024-09-20 12:00:00', 'pending', 750.00, 'USD'),
      ('2024-09-25 14:00:00', '2024-09-25 14:00:00', 'pending', 26000.00, 'UAH'),
      ('2024-05-15 09:00:00', '2024-05-15 09:05:00', 'paid', 11800.00, 'UAH'),
      ('2024-06-20 10:00:00', '2024-06-20 10:05:00', 'paid', 510.00, 'EUR'),
      ('2024-07-25 11:00:00', '2024-07-25 11:05:00', 'paid', 14200.00, 'UAH'),
      ('2024-08-25 08:00:00', '2024-08-25 08:00:00', 'pending', 23000.00, 'UAH'),
      ('2024-09-28 13:00:00', '2024-09-28 13:00:00', 'pending', 17500.00, 'UAH'),
      ('2024-06-17 10:00:00', '2024-06-17 10:05:00', 'paid', 2550.00, 'UAH'),
      ('2024-08-08 11:00:00', '2024-08-08 11:05:00', 'paid', 1700.00, 'UAH'),
      ('2024-09-06 10:30:00', '2024-09-06 10:35:00', 'paid', 5950.00, 'UAH'),
      ('2024-06-25 09:00:00', '2024-06-25 09:05:00', 'paid', 3740.00, 'UAH'),
      ('2024-08-26 14:20:00', '2024-08-26 14:25:00', 'paid', 1870.00, 'UAH');
    """)

    op.execute("""
      INSERT INTO `fines` (`created_at`, `updated_at`, `status`, `amount`, `currency`, `violation`) VALUES
      ('2024-06-03 14:30:00', '2024-06-06 10:00:00', 'paid', 3400.00, 'UAH', 'Перевищення швидкості на 20 км/год'),
      ('2024-07-05 16:45:00', '2024-07-05 16:45:00', 'unpaid', 1700.00, 'UAH', 'Неправильна парковка'),
      ('2024-08-12 11:20:00', '2024-08-16 09:30:00', 'paid', 5100.00, 'UAH', 'Проїзд на червоне світло'),
      ('2024-09-05 10:15:00', '2024-09-05 10:15:00', 'unpaid', 2550.00, 'UAH', 'Порушення правил зупинки'),
      ('2024-09-22 15:30:00', '2024-09-22 15:30:00', 'unpaid', 6800.00, 'UAH', 'Перевищення швидкості на 50 км/год'),
      ('2024-06-12 13:20:00', '2024-06-17 10:00:00', 'paid', 2550.00, 'UAH', 'Невикористання ременя безпеки'),
      ('2024-07-18 09:40:00', '2024-07-18 09:40:00', 'unpaid', 4250.00, 'UAH', 'Перевищення швидкості на 30 км/год'),
      ('2024-08-03 17:15:00', '2024-08-08 11:00:00', 'paid', 1700.00, 'UAH', 'Неправильний поворот'),
      ('2024-08-15 14:25:00', '2024-08-15 14:25:00', 'unpaid', 3400.00, 'UAH', 'Рух забороненою смугою'),
      ('2024-09-03 11:50:00', '2024-09-06 10:30:00', 'paid', 5950.00, 'UAH', 'Порушення правил обгону'),
      ('2024-05-18 10:30:00', '2024-05-18 10:30:00', 'unpaid', 2040.00, 'UAH', 'Паркування в забороненому місці'),
      ('2024-06-22 15:45:00', '2024-06-25 09:00:00', 'paid', 3740.00, 'UAH', 'Перевищення швидкості на 25 км/год'),
      ('2024-07-28 12:10:00', '2024-07-28 12:10:00', 'unpaid', 8500.00, 'UAH', "Керування в стані алкогольного сп'яніння"),
      ('2024-08-22 16:35:00', '2024-08-26 14:20:00', 'paid', 1870.00, 'UAH', 'Незупинка перед пішохідним переходом'),
      ('2024-09-26 09:20:00', '2024-09-26 09:20:00', 'unpaid', 4080.00, 'UAH', 'Використання телефону за кермом');
    """)

    op.execute("""
      INSERT INTO `rentings_payments` (`renting_id`, `payment_id`, `created_at`, `updated_at`) VALUES
      (1, 1, '2024-06-01 09:00:00', '2024-06-01 09:00:00'),
      (2, 2, '2024-06-10 08:00:00', '2024-06-10 08:00:00'),
      (3, 3, '2024-07-01 07:00:00', '2024-07-01 07:00:00'),
      (4, 4, '2024-07-15 10:00:00', '2024-07-15 10:00:00'),
      (5, 5, '2024-08-01 11:00:00', '2024-08-01 11:00:00'),
      (6, 6, '2024-08-10 09:00:00', '2024-08-10 09:00:00'),
      (7, 7, '2024-09-01 08:00:00', '2024-09-01 08:00:00'),
      (8, 8, '2024-09-15 10:00:00', '2024-09-15 10:00:00'),
      (9, 9, '2024-09-20 12:00:00', '2024-09-20 12:00:00'),
      (10, 10, '2024-09-25 14:00:00', '2024-09-25 14:00:00'),
      (11, 11, '2024-05-15 09:00:00', '2024-05-15 09:00:00'),
      (12, 12, '2024-06-20 10:00:00', '2024-06-20 10:00:00'),
      (13, 13, '2024-07-25 11:00:00', '2024-07-25 11:00:00'),
      (14, 14, '2024-08-25 08:00:00', '2024-08-25 08:00:00'),
      (15, 15, '2024-09-28 13:00:00', '2024-09-28 13:00:00');
    """)

    op.execute("""
      INSERT INTO `rentings_fines` (`renting_id`, `fine_id`, `created_at`, `updated_at`) VALUES
      (1, 1, '2024-06-03 14:30:00', '2024-06-03 14:30:00'),
      (3, 2, '2024-07-05 16:45:00', '2024-07-05 16:45:00'),
      (6, 3, '2024-08-12 11:20:00', '2024-08-12 11:20:00'),
      (7, 4, '2024-09-05 10:15:00', '2024-09-05 10:15:00'),
      (9, 5, '2024-09-22 15:30:00', '2024-09-22 15:30:00'),
      (2, 6, '2024-06-12 13:20:00', '2024-06-12 13:20:00'),
      (4, 7, '2024-07-18 09:40:00', '2024-07-18 09:40:00'),
      (5, 8, '2024-08-03 17:15:00', '2024-08-03 17:15:00'),
      (5, 9, '2024-08-15 14:25:00', '2024-08-15 14:25:00'),
      (7, 10, '2024-09-03 11:50:00', '2024-09-03 11:50:00'),
      (11, 11, '2024-05-18 10:30:00', '2024-05-18 10:30:00'),
      (12, 12, '2024-06-22 15:45:00', '2024-06-22 15:45:00'),
      (13, 13, '2024-07-28 12:10:00', '2024-07-28 12:10:00'),
      (14, 14, '2024-08-22 16:35:00', '2024-08-22 16:35:00'),
      (15, 15, '2024-09-26 09:20:00', '2024-09-26 09:20:00');
    """)

    op.execute("""
      INSERT INTO `fines_payments` (`fine_id`, `payment_id`, `created_at`, `updated_at`) VALUES
      (1, 1, '2024-06-06 10:00:00', '2024-06-06 10:00:00'),
      (3, 6, '2024-08-16 09:30:00', '2024-08-16 09:30:00'),
      (6, 16, '2024-06-17 10:00:00', '2024-06-17 10:00:00'),
      (8, 17, '2024-08-08 11:00:00', '2024-08-08 11:00:00'),
      (10, 18, '2024-09-06 10:30:00', '2024-09-06 10:30:00'),
      (12, 19, '2024-06-25 09:00:00', '2024-06-25 09:00:00'),
      (14, 20, '2024-08-26 14:20:00', '2024-08-26 14:20:00');
      """
    )

def downgrade():
    op.drop_table('fines_payments')
    op.drop_table('rentings_payments')
    op.drop_table('rentings_fines')
    op.drop_table('rentings')
    op.drop_table('parkings_vehicles')
    op.drop_table('payments')
    op.drop_table('fines')
    op.drop_table('vehicles')
    op.drop_table('parkings')
    op.drop_table('users')

