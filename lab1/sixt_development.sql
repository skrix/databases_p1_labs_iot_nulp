-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema sixt_development
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema sixt_development
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `sixt_development` DEFAULT CHARACTER SET utf8 ;
USE `sixt_development` ;

-- -----------------------------------------------------
-- Table `sixt_development`.`parkings`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `sixt_development`.`parkings` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `address` VARCHAR(45) NULL,
  `country` VARCHAR(45) NULL,
  `city` VARCHAR(45) NULL,
  `latitude` DECIMAL(11,8) NOT NULL,
  `longitude` DECIMAL(11,8) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `latitude_longitude_UNIQUE` (`longitude` ASC, `latitude` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `sixt_development`.`vehicles`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `sixt_development`.`vehicles` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `make` VARCHAR(45) NOT NULL,
  `model` VARCHAR(45) NOT NULL,
  `year` INT NOT NULL,
  `vin` VARCHAR(45) NOT NULL,
  `body` ENUM('sedan', 'hatchback', 'wagon', 'coupe', 'convertible', 'roadster', 'suv', 'crossover', 'pickup', 'van', 'minivan', 'truck', 'camper') NOT NULL DEFAULT 'sedan',
  PRIMARY KEY (`id`),
  UNIQUE INDEX `vin_UNIQUE` (`vin` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `sixt_development`.`users`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `sixt_development`.`users` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(45) NOT NULL,
  `middle_name` VARCHAR(45) NULL,
  `last_name` VARCHAR(45) NOT NULL,
  `dob` DATE NOT NULL,
  `email` VARCHAR(255) NOT NULL,
  `password` VARCHAR(32) NOT NULL,
  `created_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `driver_license` VARCHAR(255) NOT NULL,
  `gender` ENUM('male', 'female') NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `email_UNIQUE` (`email` ASC) VISIBLE,
  UNIQUE INDEX `driver_license_UNIQUE` (`driver_license` ASC) VISIBLE);


-- -----------------------------------------------------
-- Table `sixt_development`.`parkings_vehicles`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `sixt_development`.`parkings_vehicles` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `parking_id` INT NOT NULL,
  `vehicle_id` INT NOT NULL,
  `created_at` TIMESTAMP NOT NULL,
  `updated_at` TIMESTAMP NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `parking_id_idx` (`parking_id` ASC) VISIBLE,
  INDEX `vehicle_id_idx` (`vehicle_id` ASC) VISIBLE,
  UNIQUE INDEX `parking_vehicle_UNIQUE` (`parking_id` ASC, `vehicle_id` ASC) VISIBLE,
  CONSTRAINT `parking_vehicle_parking_id`
    FOREIGN KEY (`parking_id`)
    REFERENCES `sixt_development`.`parkings` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `parking_vehicle_vehicle_id`
    FOREIGN KEY (`vehicle_id`)
    REFERENCES `sixt_development`.`vehicles` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `sixt_development`.`rentings`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `sixt_development`.`rentings` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `user_id` INT NOT NULL,
  `vehicle_id` INT NOT NULL,
  `created_at` TIMESTAMP NOT NULL,
  `updated_at` TIMESTAMP NOT NULL,
  `start_at` DATETIME NOT NULL,
  `end_at` DATETIME NULL,
  PRIMARY KEY (`id`),
  INDEX `vehicle_id_idx` (`vehicle_id` ASC) VISIBLE,
  INDEX `user_id_idx` (`vehicle_id` ASC) VISIBLE,
  CONSTRAINT `renting_user_id`
    FOREIGN KEY (`user_id`)
    REFERENCES `sixt_development`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `renting_vehicle_id`
    FOREIGN KEY (`vehicle_id`)
    REFERENCES `sixt_development`.`vehicles` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `sixt_development`.`payments`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `sixt_development`.`payments` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `created_at` TIMESTAMP NOT NULL,
  `updated_at` TIMESTAMP NOT NULL,
  `status` ENUM('pending', 'paid', 'failed') NOT NULL,
  `amount` DECIMAL NOT NULL,
  `currency` ENUM('USD', 'EUR', 'UAH') NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `sixt_development`.`fines`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `sixt_development`.`fines` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `created_at` TIMESTAMP NOT NULL,
  `updated_at` TIMESTAMP NOT NULL,
  `status` ENUM('paid', 'unpaid') NOT NULL,
  `amount` DECIMAL NOT NULL,
  `currency` ENUM('USD', 'EUR', 'UAH') NOT NULL,
  `violation` VARCHAR(255) NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `sixt_development`.`rentings_fines`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `sixt_development`.`rentings_fines` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `renting_id` INT NOT NULL,
  `fine_id` INT NOT NULL,
  `created_at` TIMESTAMP NOT NULL,
  `updated_at` TIMESTAMP NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `renting_fine_UNIQUE` (`renting_id` ASC, `fine_id` ASC) VISIBLE,
  INDEX `fine_id_idx` (`fine_id` ASC) VISIBLE,
  INDEX `renting_id_idx` (`renting_id` ASC) VISIBLE,
  CONSTRAINT `renting_fine_renting_id`
    FOREIGN KEY (`renting_id`)
    REFERENCES `sixt_development`.`rentings` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `renting_fine_fine_id`
    FOREIGN KEY (`fine_id`)
    REFERENCES `sixt_development`.`fines` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `sixt_development`.`rentings_payments`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `sixt_development`.`rentings_payments` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `renting_id` INT NOT NULL,
  `payment_id` INT NOT NULL,
  `created_at` TIMESTAMP NOT NULL,
  `updated_at` TIMESTAMP NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `renting_payment_UNIQUE` (`renting_id` ASC, `payment_id` ASC) VISIBLE,
  INDEX `renting_id_idx` (`renting_id` ASC) VISIBLE,
  INDEX `payment_id_idx` (`payment_id` ASC) VISIBLE,
  CONSTRAINT `renting_payment_renting_id`
    FOREIGN KEY (`renting_id`)
    REFERENCES `sixt_development`.`rentings` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `renting_payment_payment_id`
    FOREIGN KEY (`payment_id`)
    REFERENCES `sixt_development`.`payments` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `sixt_development`.`fines_payments`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `sixt_development`.`fines_payments` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `fine_id` INT NOT NULL,
  `payment_id` INT NOT NULL,
  `created_at` TIMESTAMP NOT NULL,
  `updated_at` TIMESTAMP NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `fine_payment_UNIQUE` (`fine_id` ASC, `payment_id` ASC) VISIBLE,
  INDEX `fine_id_idx` (`fine_id` ASC) VISIBLE,
  INDEX `payment_id_idx` (`payment_id` ASC) VISIBLE,
  CONSTRAINT `fine_payment_fine_id`
    FOREIGN KEY (`fine_id`)
    REFERENCES `sixt_development`.`fines` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fine_payment_payment_id`
    FOREIGN KEY (`payment_id`)
    REFERENCES `sixt_development`.`payments` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
