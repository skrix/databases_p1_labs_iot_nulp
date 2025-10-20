CREATE SCHEMA IF NOT EXISTS `sixt_development` DEFAULT CHARACTER SET utf8mb4;
USE `sixt_development`;

DROP TABLE IF EXISTS `fines_payments`;
DROP TABLE IF EXISTS `rentings_payments`;
DROP TABLE IF EXISTS `rentings_fines`;
DROP TABLE IF EXISTS `rentings`;
DROP TABLE IF EXISTS `parkings_vehicles`;
DROP TABLE IF EXISTS `payments`;
DROP TABLE IF EXISTS `fines`;
DROP TABLE IF EXISTS `vehicles`;
DROP TABLE IF EXISTS `parkings`;
DROP TABLE IF EXISTS `users`;

CREATE TABLE `sixt_development`.`parkings` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `address` VARCHAR(255) NULL,
  `country` VARCHAR(100) NULL,
  `city` VARCHAR(100) NULL,
  `latitude` DECIMAL(11,8) NOT NULL,
  `longitude` DECIMAL(11,8) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE = InnoDB;

CREATE TABLE `sixt_development`.`vehicles` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `make` VARCHAR(100) NOT NULL,
  `model` VARCHAR(100) NOT NULL,
  `year` INT NOT NULL,
  `vin` VARCHAR(17) NOT NULL,
  `body` ENUM('sedan', 'hatchback', 'wagon', 'coupe', 'convertible', 'roadster', 'suv', 'crossover', 'pickup', 'van', 'minivan', 'truck', 'camper') NOT NULL DEFAULT 'sedan',
  `plate` VARCHAR(15) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE = InnoDB;

CREATE TABLE `sixt_development`.`users` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(100) NOT NULL,
  `middle_name` VARCHAR(100) NULL,
  `last_name` VARCHAR(100) NOT NULL,
  `dob` DATE NOT NULL,
  `email` VARCHAR(255) NOT NULL,
  `password` VARCHAR(255) NOT NULL,
  `created_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `driver_license` VARCHAR(255) NOT NULL,
  `gender` ENUM('male', 'female', 'other', 'prefer_not_to_say') NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE = InnoDB;

CREATE TABLE `sixt_development`.`parkings_vehicles` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `parking_id` INT NOT NULL,
  `vehicle_id` INT NOT NULL,
  `created_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE = InnoDB;

CREATE TABLE `sixt_development`.`rentings` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `user_id` INT NOT NULL,
  `vehicle_id` INT NOT NULL,
  `created_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `start_at` DATETIME NOT NULL,
  `end_at` DATETIME NULL,
  PRIMARY KEY (`id`)
) ENGINE = InnoDB;

CREATE TABLE `sixt_development`.`payments` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `created_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `status` ENUM('pending', 'paid', 'failed', 'refunded') NOT NULL DEFAULT 'pending',
  `amount` DECIMAL(10,2) NOT NULL,
  `currency` ENUM('USD', 'EUR', 'UAH') NOT NULL DEFAULT 'USD',
  PRIMARY KEY (`id`)
) ENGINE = InnoDB;

CREATE TABLE `sixt_development`.`fines` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `created_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `status` ENUM('paid', 'unpaid', 'disputed', 'waived') NOT NULL DEFAULT 'unpaid',
  `amount` DECIMAL(10,2) NOT NULL,
  `currency` ENUM('USD', 'EUR', 'UAH') NOT NULL DEFAULT 'USD',
  `violation` VARCHAR(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE = InnoDB;

CREATE TABLE `sixt_development`.`rentings_fines` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `renting_id` INT NOT NULL,
  `fine_id` INT NOT NULL,
  `created_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE = InnoDB;

CREATE TABLE `sixt_development`.`rentings_payments` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `renting_id` INT NOT NULL,
  `payment_id` INT NOT NULL,
  `created_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE = InnoDB;

CREATE TABLE `sixt_development`.`fines_payments` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `fine_id` INT NOT NULL,
  `payment_id` INT NOT NULL,
  `created_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE = InnoDB;

-- Add indexes to parkings
ALTER TABLE `sixt_development`.`parkings`
  ADD UNIQUE INDEX `latitude_longitude_UNIQUE` (`latitude` ASC, `longitude` ASC),
  ADD INDEX `address_idx` (`address` ASC),
  ADD INDEX `country_idx` (`country` ASC),
  ADD INDEX `city_idx` (`city` ASC);

-- Add indexes to vehicles
ALTER TABLE `sixt_development`.`vehicles`
  ADD UNIQUE INDEX `vin_UNIQUE` (`vin` ASC),
  ADD UNIQUE INDEX `plate_UNIQUE` (`plate` ASC),
  ADD INDEX `make_idx` (`make` ASC),
  ADD INDEX `model_idx` (`model` ASC),
  ADD INDEX `year_idx` (`year` ASC),
  ADD INDEX `body_year_idx` (`body` ASC, `year` ASC);

-- Add indexes to users
ALTER TABLE `sixt_development`.`users`
  ADD UNIQUE INDEX `email_UNIQUE` (`email` ASC),
  ADD UNIQUE INDEX `driver_license_UNIQUE` (`driver_license` ASC),
  ADD INDEX `first_name_idx` (`first_name` ASC),
  ADD INDEX `last_name_idx` (`last_name` ASC),
  ADD INDEX `dob_idx` (`dob` ASC);

-- Add indexes to parkings_vehicles
ALTER TABLE `sixt_development`.`parkings_vehicles`
  ADD INDEX `parking_id_idx` (`parking_id` ASC),
  ADD INDEX `vehicle_id_idx` (`vehicle_id` ASC),
  ADD UNIQUE INDEX `parking_vehicle_UNIQUE` (`parking_id` ASC, `vehicle_id` ASC);

-- Add indexes to rentings
ALTER TABLE `sixt_development`.`rentings`
  ADD INDEX `vehicle_id_idx` (`vehicle_id` ASC),
  ADD INDEX `user_id_idx` (`user_id` ASC),
  ADD INDEX `start_at_idx` (`start_at` ASC),
  ADD INDEX `end_at_idx` (`end_at` ASC),
  ADD INDEX `user_start_idx` (`user_id` ASC, `start_at` ASC);

-- Add indexes to payments
ALTER TABLE `sixt_development`.`payments`
  ADD INDEX `status_idx` (`status` ASC),
  ADD INDEX `created_at_idx` (`created_at` ASC);

-- Add indexes to fines
ALTER TABLE `sixt_development`.`fines`
  ADD INDEX `status_idx` (`status` ASC),
  ADD INDEX `created_at_idx` (`created_at` ASC);

-- Add indexes to rentings_fines
ALTER TABLE `sixt_development`.`rentings_fines`
  ADD UNIQUE INDEX `renting_fine_UNIQUE` (`renting_id` ASC, `fine_id` ASC),
  ADD INDEX `fine_id_idx` (`fine_id` ASC),
  ADD INDEX `renting_id_idx` (`renting_id` ASC);

-- Add indexes to rentings_payments
ALTER TABLE `sixt_development`.`rentings_payments`
  ADD UNIQUE INDEX `renting_payment_UNIQUE` (`renting_id` ASC, `payment_id` ASC),
  ADD INDEX `renting_id_idx` (`renting_id` ASC),
  ADD INDEX `payment_id_idx` (`payment_id` ASC);

-- Add indexes to fines_payments
ALTER TABLE `sixt_development`.`fines_payments`
  ADD UNIQUE INDEX `fine_payment_UNIQUE` (`fine_id` ASC, `payment_id` ASC),
  ADD INDEX `fine_id_idx` (`fine_id` ASC),
  ADD INDEX `payment_id_idx` (`payment_id` ASC);

-- Add foreign keys to parkings_vehicles
ALTER TABLE `sixt_development`.`parkings_vehicles`
  ADD CONSTRAINT `parking_vehicle_parking_id`
    FOREIGN KEY (`parking_id`)
    REFERENCES `sixt_development`.`parkings` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  ADD CONSTRAINT `parking_vehicle_vehicle_id`
    FOREIGN KEY (`vehicle_id`)
    REFERENCES `sixt_development`.`vehicles` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE;

-- Add foreign keys to rentings
ALTER TABLE `sixt_development`.`rentings`
  ADD CONSTRAINT `renting_user_id`
    FOREIGN KEY (`user_id`)
    REFERENCES `sixt_development`.`users` (`id`)
    ON DELETE RESTRICT
    ON UPDATE CASCADE,
  ADD CONSTRAINT `renting_vehicle_id`
    FOREIGN KEY (`vehicle_id`)
    REFERENCES `sixt_development`.`vehicles` (`id`)
    ON DELETE RESTRICT
    ON UPDATE CASCADE;

-- Add foreign keys to rentings_fines
ALTER TABLE `sixt_development`.`rentings_fines`
  ADD CONSTRAINT `renting_fine_renting_id`
    FOREIGN KEY (`renting_id`)
    REFERENCES `sixt_development`.`rentings` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  ADD CONSTRAINT `renting_fine_fine_id`
    FOREIGN KEY (`fine_id`)
    REFERENCES `sixt_development`.`fines` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE;

-- Add foreign keys to rentings_payments
ALTER TABLE `sixt_development`.`rentings_payments`
  ADD CONSTRAINT `renting_payment_renting_id`
    FOREIGN KEY (`renting_id`)
    REFERENCES `sixt_development`.`rentings` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  ADD CONSTRAINT `renting_payment_payment_id`
    FOREIGN KEY (`payment_id`)
    REFERENCES `sixt_development`.`payments` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE;

-- Add foreign keys to fines_payments
ALTER TABLE `sixt_development`.`fines_payments`
  ADD CONSTRAINT `fine_payment_fine_id`
    FOREIGN KEY (`fine_id`)
    REFERENCES `sixt_development`.`fines` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  ADD CONSTRAINT `fine_payment_payment_id`
    FOREIGN KEY (`payment_id`)
    REFERENCES `sixt_development`.`payments` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE;

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

INSERT INTO `users` (`first_name`, `middle_name`, `last_name`, `dob`, `email`, `password`, `driver_license`, `gender`) VALUES
('Олександр', 'Іванович', 'Шевченко', '1985-03-15', 'o.shevchenko@email.com', SHA2('password123', 256), 'АВЕ123456', 'male'),
('Олена', 'Петрівна', 'Коваленко', '1990-07-22', 'o.kovalenko@email.com', SHA2('password123', 256), 'АВЕ223456', 'female'),
('Дмитро', 'Сергійович', 'Мельник', '1982-11-08', 'd.melnyk@email.com', SHA2('password123', 256), 'АВЕ323456', 'male'),
('Марія', 'Андріївна', 'Бондаренко', '1995-04-30', 'm.bondarenko@email.com', SHA2('password123', 256), 'АВЕ423456', 'female'),
('Андрій', 'Миколайович', 'Ткаченко', '1988-09-12', 'a.tkachenko@email.com', SHA2('password123', 256), 'АВЕ523456', 'male'),
('Юлія', 'Олександрівна', 'Кравченко', '1992-01-25', 'y.kravchenko@email.com', SHA2('password123', 256), 'АВЕ623456', 'female'),
('Віктор', 'Васильович', 'Гончаренко', '1987-06-18', 'v.honcharenko@email.com', SHA2('password123', 256), 'АВЕ723456', 'male'),
('Тетяна', 'Володимирівна', 'Павленко', '1993-12-05', 't.pavlenko@email.com', SHA2('password123', 256), 'АВЕ823456', 'female'),
('Максим', 'Ігорович', 'Савченко', '1984-08-28', 'm.savchenko@email.com', SHA2('password123', 256), 'АВЕ923456', 'male'),
('Наталія', 'Олегівна', 'Романенко', '1991-02-14', 'n.romanenko@email.com', SHA2('password123', 256), 'АВЕ023456', 'female'),
('Сергій', 'Анатолійович', 'Лисенко', '1989-10-03', 's.lysenko@email.com', SHA2('password123', 256), 'АВЕ033456', 'male'),
('Анна', 'Михайлівна', 'Поліщук', '1994-05-19', 'a.polischuk@email.com', SHA2('password123', 256), 'АВЕ043456', 'female'),
('Ігор', 'Романович', 'Коваль', '1986-07-07', 'i.koval@email.com', SHA2('password123', 256), 'АВЕ053456', 'male'),
('Катерина', 'Ярославівна', 'Захарченко', '1996-11-22', 'k.zakharchenko@email.com', SHA2('password123', 256), 'АВЕ063456', 'female'),
('Володимир', 'Богданович', 'Білоус', '1983-03-11', 'v.bilous@email.com', SHA2('password123', 256), 'АВЕ073456', 'male');

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

INSERT INTO `fines_payments` (`fine_id`, `payment_id`, `created_at`, `updated_at`) VALUES
(1, 1, '2024-06-06 10:00:00', '2024-06-06 10:00:00'),
(3, 6, '2024-08-16 09:30:00', '2024-08-16 09:30:00'),
(6, 16, '2024-06-17 10:00:00', '2024-06-17 10:00:00'),
(8, 17, '2024-08-08 11:00:00', '2024-08-08 11:00:00'),
(10, 18, '2024-09-06 10:30:00', '2024-09-06 10:30:00'),
(12, 19, '2024-06-25 09:00:00', '2024-06-25 09:00:00'),
(14, 20, '2024-08-26 14:20:00', '2024-08-26 14:20:00');
