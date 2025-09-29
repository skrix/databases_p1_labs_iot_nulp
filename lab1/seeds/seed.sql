-- Seed Data for sixt_development database (Ukraine localized)
USE `sixt_development`;

-- Disable foreign key checks for easier insertion
SET FOREIGN_KEY_CHECKS=0;

-- Clear existing data (optional - uncomment if you want to reset)
-- TRUNCATE TABLE `fines_payments`;
-- TRUNCATE TABLE `rentings_payments`;
-- TRUNCATE TABLE `rentings_fines`;
-- TRUNCATE TABLE `rentings`;
-- TRUNCATE TABLE `parkings_vehicles`;
-- TRUNCATE TABLE `fines`;
-- TRUNCATE TABLE `payments`;
-- TRUNCATE TABLE `users`;
-- TRUNCATE TABLE `vehicles`;
-- TRUNCATE TABLE `parkings`;

-- Insert Parkings (Ukrainian cities)
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

-- Insert Vehicles (popular in Ukraine with Ukrainian plates)
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

-- Insert Users (Ukrainian names)
INSERT INTO `users` (`first_name`, `middle_name`, `last_name`, `dob`, `email`, `password`, `driver_license`, `gender`) VALUES
('Олександр', 'Іванович', 'Шевченко', '1985-03-15', 'o.shevchenko@email.com', MD5('password123'), 'АВЕ123456', 'male'),
('Олена', 'Петрівна', 'Коваленко', '1990-07-22', 'o.kovalenko@email.com', MD5('password123'), 'АВЕ223456', 'female'),
('Дмитро', 'Сергійович', 'Мельник', '1982-11-08', 'd.melnyk@email.com', MD5('password123'), 'АВЕ323456', 'male'),
('Марія', 'Андріївна', 'Бондаренко', '1995-04-30', 'm.bondarenko@email.com', MD5('password123'), 'АВЕ423456', 'female'),
('Андрій', 'Миколайович', 'Ткаченко', '1988-09-12', 'a.tkachenko@email.com', MD5('password123'), 'АВЕ523456', 'male'),
('Юлія', 'Олександрівна', 'Кравченко', '1992-01-25', 'y.kravchenko@email.com', MD5('password123'), 'АВЕ623456', 'female'),
('Віктор', 'Васильович', 'Гончаренко', '1987-06-18', 'v.honcharenko@email.com', MD5('password123'), 'АВЕ723456', 'male'),
('Тетяна', 'Володимирівна', 'Павленко', '1993-12-05', 't.pavlenko@email.com', MD5('password123'), 'АВЕ823456', 'female'),
('Максим', 'Ігорович', 'Савченко', '1984-08-28', 'm.savchenko@email.com', MD5('password123'), 'АВЕ923456', 'male'),
('Наталія', 'Олегівна', 'Романенко', '1991-02-14', 'n.romanenko@email.com', MD5('password123'), 'АВЕ023456', 'female'),
('Сергій', 'Анатолійович', 'Лисенко', '1989-10-03', 's.lysenko@email.com', MD5('password123'), 'АВЕ033456', 'male'),
('Анна', 'Михайлівна', 'Поліщук', '1994-05-19', 'a.polischuk@email.com', MD5('password123'), 'АВЕ043456', 'female'),
('Ігор', 'Романович', 'Коваль', '1986-07-07', 'i.koval@email.com', MD5('password123'), 'АВЕ053456', 'male'),
('Катерина', 'Ярославівна', 'Захарченко', '1996-11-22', 'k.zakharchenko@email.com', MD5('password123'), 'АВЕ063456', 'female'),
('Володимир', 'Богданович', 'Білоус', '1983-03-11', 'v.bilous@email.com', MD5('password123'), 'АВЕ073456', 'male');

-- Insert Parkings_Vehicles (linking vehicles to parking locations)
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
(10, 20, '2024-01-01 19:30:00', '2024-01-01 19:30:00');

-- Insert Rentings (some completed, some ongoing)
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

-- Insert Payments (primarily in UAH with some EUR/USD)
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
('2024-09-28 13:00:00', '2024-09-28 13:00:00', 'pending', 17500.00, 'UAH');

-- Insert Fines (Ukrainian traffic violations)
INSERT INTO `fines` (`created_at`, `updated_at`, `status`, `amount`, `currency`, `violation`) VALUES
('2024-06-03 14:30:00', '2024-06-06 10:00:00', 'paid', 3400.00, 'UAH', 'Перевищення швидкості на 20 км/год'),
('2024-07-05 16:45:00', '2024-07-05 16:45:00', 'unpaid', 1700.00, 'UAH', 'Неправильна парковка'),
('2024-08-12 11:20:00', '2024-08-16 09:30:00', 'paid', 5100.00, 'UAH', 'Проїзд на червоне світло'),
('2024-09-05 10:15:00', '2024-09-05 10:15:00', 'unpaid', 2550.00, 'UAH', 'Порушення правил зупинки'),
('2024-09-22 15:30:00', '2024-09-22 15:30:00', 'unpaid', 6800.00, 'UAH', 'Перевищення швидкості на 50 км/год');

-- Insert Rentings_Payments (linking rentals to payments)
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

-- Insert Rentings_Fines (linking fines to rentals)
INSERT INTO `rentings_fines` (`renting_id`, `fine_id`, `created_at`, `updated_at`) VALUES
(1, 1, '2024-06-03 14:30:00', '2024-06-03 14:30:00'),
(3, 2, '2024-07-05 16:45:00', '2024-07-05 16:45:00'),
(6, 3, '2024-08-12 11:20:00', '2024-08-12 11:20:00'),
(7, 4, '2024-09-05 10:15:00', '2024-09-05 10:15:00'),
(9, 5, '2024-09-22 15:30:00', '2024-09-22 15:30:00');

-- Insert Fines_Payments (linking fine payments)
INSERT INTO `fines_payments` (`fine_id`, `payment_id`, `created_at`, `updated_at`) VALUES
(1, 1, '2024-06-06 10:00:00', '2024-06-06 10:00:00'),
(3, 6, '2024-08-16 09:30:00', '2024-08-16 09:30:00');

-- Re-enable foreign key checks
SET FOREIGN_KEY_CHECKS=1;

-- Verify data insertion
SELECT 'Parkings' AS TableName, COUNT(*) AS RecordCount FROM parkings
UNION ALL
SELECT 'Vehicles', COUNT(*) FROM vehicles
UNION ALL
SELECT 'Users', COUNT(*) FROM users
UNION ALL
SELECT 'Parkings_Vehicles', COUNT(*) FROM parkings_vehicles
UNION ALL
SELECT 'Rentings', COUNT(*) FROM rentings
UNION ALL
SELECT 'Payments', COUNT(*) FROM payments
UNION ALL
SELECT 'Fines', COUNT(*) FROM fines
UNION ALL
SELECT 'Rentings_Payments', COUNT(*) FROM rentings_payments
UNION ALL
SELECT 'Rentings_Fines', COUNT(*) FROM rentings_fines
UNION ALL
SELECT 'Fines_Payments', COUNT(*) FROM fines_payments;
