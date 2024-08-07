
-- CREATE USER 'cs6400'@'localhost' IDENTIFIED BY 'cs6400';
#CREATE USER IF NOT EXISTS cs6400@localhost IDENTIFIED BY 'cs6400';

DROP DATABASE IF EXISTS `cs6400_su24_team001`; 
SET default_storage_engine=InnoDB;
SET NAMES utf8mb4 COLLATE utf8mb4_unicode_ci;

CREATE DATABASE IF NOT EXISTS cs6400_su24_team001 
    DEFAULT CHARACTER SET utf8mb4 
    DEFAULT COLLATE utf8mb4_unicode_ci;
USE cs6400_su24_team001;

GRANT SELECT, INSERT, UPDATE, DELETE, FILE ON *.* TO 'cs6400'@'localhost';
GRANT ALL PRIVILEGES ON `cs6400`.* TO 'cs6400'@'localhost';
GRANT ALL PRIVILEGES ON `cs6400_su24_team001`.* TO 'cs6400'@'localhost';
FLUSH PRIVILEGES;

#Tables
CREATE TABLE `User` (
EmployeeID varchar(7) NOT NULL,
FirstName varchar(100) NOT NULL,
LastName varchar(100) NOT NULL,
SSN varchar(9) NOT NULL,
LogAccess boolean NOT NULL,
PRIMARY KEY (EmployeeID)
);

CREATE TABLE `Manufacturer` (
ManufacturerName varchar(100) NOT NULL,
PRIMARY KEY (ManufacturerName)
);

CREATE TABLE `Category` (
CategoryName varchar(100) NOT NULL,
PRIMARY KEY (CategoryName)
);

CREATE TABLE `District` (
DistrictNumber int NOT NULL,
PRIMARY KEY (DistrictNumber)
);

CREATE TABLE `City` (
CityName varchar(100) NOT NULL,
State varchar(100) NOT NULL,
Population INT NOT NULL,
PRIMARY KEY (CityName, State)
);

CREATE TABLE `Store` (
StoreNumber int NOT NULL,
PhoneNumber varchar(20) NOT NULL,
CityName varchar(100) NOT NULL,
State varchar(100) NOT NULL,
DistrictNumber int NOT NULL,
PRIMARY KEY (StoreNumber)
);

CREATE TABLE `User_Assigned_District` (
DistrictNumber int NOT NULL,
EmployeeID varchar(7) NOT NULL,
PRIMARY KEY (DistrictNumber,EmployeeID)
);

CREATE TABLE `Product` (
PID int NOT NULL,
ProductName varchar(100) NOT NULL,
RetailPrice FLOAT NOT NULL,
ManufacturerName varchar(100) NOT NULL,
PRIMARY KEY (PID)
);

CREATE TABLE `Product_Category` (
PID int NOT NULL,
CategoryName varchar(100) NOT NULL,
PRIMARY KEY (PID,CategoryName)
);

CREATE TABLE `Discount` (
DiscountDate datetime NOT NULL,
PID int NOT NULL,
DiscountPrice FLOAT NOT NULL,
PRIMARY KEY (DiscountDate,PID)
);

CREATE TABLE `Audit_Log`(
Date_Time datetime NOT NULL,
EmployeeID varchar(7) NOT NULL,
ReportName varchar(100) NOT NULL,
PRIMARY KEY (Date_Time, EmployeeID)
);

CREATE TABLE `Holiday` (
HolidayDate date NOT NULL,
HolidayName varchar(100) NOT NULL,
EmployeeID varchar(7) NOT NULL,
PRIMARY KEY (HolidayDate)
);

CREATE TABLE `Non_Holiday` (
NonHolidayDate date NOT NULL,
PRIMARY KEY (NonHolidayDate)
);

CREATE TABLE `Report`(
ReportName VARCHAR(100) NOT NULL,
PRIMARY KEY (ReportName)
);

CREATE TABLE `Product_Sold` (
StoreNumber int NOT NULL,
PID int NOT NULL,
SoldDate date NOT NULL,
Quantity int NOT NULL,
PRIMARY KEY (StoreNumber, PID, SoldDate)
);

#--Constraints Foreign Keys:

ALTER TABLE Store
	ADD CONSTRAINT fk_Store_DistrictNumber_District_DistrictNumber FOREIGN KEY (DistrictNumber) REFERENCES District (DistrictNumber),
        ADD CONSTRAINT fk_Store_CityName_City_CityName FOREIGN KEY (CityName) REFERENCES City (CityName);

ALTER TABLE User_Assigned_District
	ADD CONSTRAINT fk_User_Assigned_District_DistrictNumber_District_DistrictNumber FOREIGN KEY (DistrictNumber) REFERENCES District (DistrictNumber),
        ADD CONSTRAINT fk_User_Assigned_District_EmployeeID_User_EmployeeID FOREIGN KEY (EmployeeID) REFERENCES User (EmployeeID);

ALTER TABLE Product
	ADD CONSTRAINT fk_Product_ManufacturerName_Manufacturer_ManufacturerName FOREIGN KEY (ManufacturerName) REFERENCES Manufacturer(ManufacturerName);

ALTER TABLE Product_Category
	ADD CONSTRAINT fk_Product_Category_PID_Product_PID FOREIGN KEY (PID) REFERENCES Product(PID),
	ADD CONSTRAINT fk_Product_Category_CategoryName_Category_CategoryName FOREIGN KEY (CategoryName) References Category(CategoryName);

ALTER TABLE Discount
	ADD CONSTRAINT fk_Discount_PID_Product_PID FOREIGN KEY (PID) References Product(PID);

ALTER TABLE Audit_Log
	ADD CONSTRAINT fk_Audit_Log_EmployeeID_User_Employee_ID FOREIGN KEY (EmployeeID) References User(EmployeeID),
	ADD CONSTRAINT fk_Audit_Log_ReportName_Report_ReportName FOREIGN KEY (ReportName) References Report(ReportName);

ALTER TABLE Holiday
	ADD CONSTRAINT fk_Holiday_EmployeeID_User_Employee_ID FOREIGN KEY (EmployeeID) References User(EmployeeID);

ALTER TABLE Product_Sold
	ADD CONSTRAINT fk_Product_Sold_Store FOREIGN KEY (StoreNumber) References Store(StoreNumber),
	ADD CONSTRAINT fk_Product_Sold_Product FOREIGN KEY (PID) References Product(PID);
#	ADD CONSTRAINT fk_Product_Sold_SoldDate_Date FOREIGN KEY (SoldDate) References Non_Holiday(NonHolidayDate),
#	ADD CONSTRAINT fk_Product_Sold_SoldDate_HolidayDate FOREIGN KEY (SoldDate) References Holiday (HolidayDate);
	