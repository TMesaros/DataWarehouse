
INSERT INTO `user` VALUES('1', 'Jane', 'Test', '111111111', False);
INSERT INTO `user` VALUES('2', "John", "Test", '222222222', False);
INSERT INTO `user` VALUES('3', "Leonardo", "DaVinci", '333333333', True);
INSERT INTO `user` VALUES('4', "Joan", "dArc", '444444444', True);
INSERT INTO `user` VALUES('5', "Abraham", "Lincoln", '555555555', True);

INSERT INTO category VALUES ('Toasters');
INSERT INTO category VALUES ('Cars');
INSERT INTO category VALUES ('Air Conditioning');
INSERT INTO category VALUES ('GPS');
INSERT INTO category VALUES ('Snacks');
INSERT INTO category VALUES ('Education');
INSERT INTO category VALUES ('Livestock');
INSERT INTO category VALUES ('Dinosaurs');
INSERT INTO category VALUES ('Finance');
INSERT INTO category VALUES ('Poetry');


INSERT INTO city VALUES("Toronto", "Ontario", 4000000);
INSERT INTO city VALUES("San Francisco", "California", 500000);
INSERT INTO city VALUES("New York", "New York", 15000000);
INSERT INTO city VALUES("Tokyo", "Kanto", 14000000);
INSERT INTO city VALUES("Shanghai", "East China", 20000000);
INSERT INTO city VALUES("Chicago", "Illinois", 6000000);
INSERT INTO city VALUES("Buffalo", "New York", 300000);
INSERT INTO city VALUES("Dallas", "Texas", 2500000);
INSERT INTO city VALUES("Austin", "Texas", 5000000);
INSERT INTO city VALUES("Houston", "Texas", 10000000);
INSERT INTO city VALUES("San Diego", "California", 4000000);
INSERT INTO city VALUES("Berkeley", "California", 100000);
INSERT INTO city VALUES("San Antonio", "Texas", 7000000);

INSERT INTO manufacturer VALUES("GT");
INSERT INTO manufacturer VALUES("Yoyodyne");
INSERT INTO manufacturer VALUES("Uncle Enzos");
INSERT INTO manufacturer VALUES("Umbrella");
INSERT INTO manufacturer VALUES("Shinra");
INSERT INTO manufacturer VALUES("Microsoft");
INSERT INTO manufacturer VALUES("Google");
INSERT INTO manufacturer VALUES("Meta");
INSERT INTO manufacturer VALUES("Amazon");
INSERT INTO manufacturer VALUES("Apple");


INSERT INTO district VALUES(1);
INSERT INTO district VALUES(2);
INSERT INTO district VALUES(3);
INSERT INTO district VALUES(4);
INSERT INTO district VALUES(5);
INSERT INTO district VALUES(6);

INSERT INTO product VALUES(1, "Vitamins", 10.00, "GT");
INSERT INTO product VALUES(2, "Kayak", 10.00, "GT");
INSERT INTO product VALUES(3, "Degree", 10.00, "GT");
INSERT INTO product VALUES(4, "Enterprise", 10.00, "Yoyodyne");
INSERT INTO product VALUES(5, "Vitamix", 10.00, "Yoyodyne");
INSERT INTO product VALUES(6, "Death Star", 10.00, "Yoyodyne");
INSERT INTO product VALUES(7, "Muzak", 10.00, "Uncle Enzos");
INSERT INTO product VALUES(8, "Robot", 10.00, "Uncle Enzos");
INSERT INTO product VALUES(9, "Stuffie", 10.00, "Uncle Enzos");
INSERT INTO product VALUES(10, "Plate", 10.00, "Umbrella");
INSERT INTO product VALUES(11, "Mug", 10.00, "Umbrella");
INSERT INTO product VALUES(12, "Supervirus", 10.00, "Umbrella");
INSERT INTO product VALUES(13, "Tablet", 10.00, "Shinra");
INSERT INTO product VALUES(14, "House", 10.00, "Shinra");
INSERT INTO product VALUES(15, "Phone", 10.00, "Shinra");
INSERT INTO product VALUES(16, "Socks", 10.00, "Shinra");
INSERT INTO product VALUES(17, "Weights", 10.00, "Microsoft");
INSERT INTO product VALUES(18, "Pants", 10.00, "Microsoft");
INSERT INTO product VALUES(19, "Keyboard", 10.00, "Microsoft");
INSERT INTO product VALUES(20, "Can", 10.00, "Google");
INSERT INTO product VALUES(21, "Milk", 10.00, "Meta");
INSERT INTO product VALUES(22, "Tires", 10.00, "Meta");
INSERT INTO product VALUES(23, "Speakers", 10.00, "Amazon");
INSERT INTO product VALUES(24, "Towels", 10.00, "Amazon");
INSERT INTO product VALUES(25, "Boxes", 10.00, "Amazon");
INSERT INTO product VALUES(26, "Forks", 10.00, "Apple");
INSERT INTO product VALUES(27, "Lightbulbs", 10.00, "Apple");


INSERT INTO product_category VALUES(1, "Toasters");
INSERT INTO product_category VALUES(1, "Snacks");
INSERT INTO product_category VALUES(2, "Cars");
INSERT INTO product_category VALUES(2, "Finance");
INSERT INTO product_category VALUES(3, "Air conditioning");
INSERT INTO product_category VALUES(4, "GPS");
INSERT INTO product_category VALUES(4, "Finance");
INSERT INTO product_category VALUES(5, "Snacks");
INSERT INTO product_category VALUES(5, "Dinosaurs");
INSERT INTO product_category VALUES(6, "Education");
INSERT INTO product_category VALUES(6, "Livestock");
INSERT INTO product_category VALUES(6, "Dinosaurs");
INSERT INTO product_category VALUES(6, "Finance");
INSERT INTO product_category VALUES(6, "Poetry");
INSERT INTO product_category VALUES(7, "Livestock");
INSERT INTO product_category VALUES(7, "Poetry");
INSERT INTO product_category VALUES(8, "Livestock");
INSERT INTO product_category VALUES(8, "Education");
INSERT INTO product_category VALUES(9, "Livestock");
INSERT INTO product_category VALUES(9, "Cars");
INSERT INTO product_category VALUES(10, "Air conditioning");
INSERT INTO product_category VALUES(10, "Toasters");
INSERT INTO product_category VALUES(11, "GPS");
INSERT INTO product_category VALUES(12, "Air conditioning");
INSERT INTO product_category VALUES(13, "GPS");
INSERT INTO product_category VALUES(14, "Air conditioning");
INSERT INTO product_category VALUES(15, "GPS");
INSERT INTO product_category VALUES(15, "Toasters");
INSERT INTO product_category VALUES(16, "Air conditioning");
INSERT INTO product_category VALUES(16, "Poetry");
INSERT INTO product_category VALUES(17, "GPS");
INSERT INTO product_category VALUES(17, "Finance");
INSERT INTO product_category VALUES(18, "Air conditioning");
INSERT INTO product_category VALUES(19, "GPS");
INSERT INTO product_category VALUES(20, "Air conditioning");
INSERT INTO product_category VALUES(20, "Cars");
INSERT INTO product_category VALUES(21, "GPS");
INSERT INTO product_category VALUES(21, "Dinosaurs");
INSERT INTO product_category VALUES(22, "Air conditioning");
INSERT INTO product_category VALUES(22, "Education");
INSERT INTO product_category VALUES(23, "GPS");
INSERT INTO product_category VALUES(23, "Poetry");
INSERT INTO product_category VALUES(24, "Air conditioning");
INSERT INTO product_category VALUES(24, "Toasters");
INSERT INTO product_category VALUES(25, "GPS");
INSERT INTO product_category VALUES(25, "Toasters");
INSERT INTO product_category VALUES(26, "Air conditioning");
INSERT INTO product_category VALUES(26, "Livestock");
INSERT INTO product_category VALUES(27, "GPS");
INSERT INTO product_category VALUES(27, "Air conditioning");


INSERT INTO store VALUES(1, "555-555-5555", "Toronto", "Ontario", 1);
INSERT INTO store VALUES(2, "555-555-5566", "San Francisco", "California", 2);
INSERT INTO store VALUES(3, "555-555-5777", "New York", "New York", 3);
INSERT INTO store VALUES(4, "555-555-8888", "Tokyo", "Kanto", 4);
INSERT INTO store VALUES(5, "555-555-9999", "Shanghai", "East China", 5);
INSERT INTO store VALUES(6, "555-000-0000", "Chicago", "Illinois", 6);
INSERT INTO store VALUES(7, "555-000-0000", "Buffalo", "New York", 1);
INSERT INTO store VALUES(8, "555-000-0000", "Dallas", "Texas", 2);
INSERT INTO store VALUES(9, "555-000-0000", "Austin", "Texas", 3);
INSERT INTO store VALUES(10, "555-000-0000", "Houston", "Texas", 4);
INSERT INTO store VALUES(11, "555-000-0000", "San Diego", "California", 5);
INSERT INTO store VALUES(12, "555-000-0000", "Berkeley", "California", 6);
INSERT INTO store VALUES(13, "555-000-0000", "San Antonio", "Texas", 1);
INSERT INTO store VALUES(14, "555-555-5555", "Toronto", "Ontario", 2);
INSERT INTO store VALUES(15, "555-555-5566", "San Francisco", "California", 3);
INSERT INTO store VALUES(16, "555-555-5777", "New York", "New York", 4);
INSERT INTO store VALUES(17, "555-555-8888", "Tokyo", "Kanto", 5);
INSERT INTO store VALUES(18, "555-555-9999", "Shanghai", "East China", 6);
INSERT INTO store VALUES(19, "555-000-0000", "Chicago", "Illinois", 1);
INSERT INTO store VALUES(20, "555-000-0000", "Buffalo", "New York", 2);
INSERT INTO store VALUES(21, "555-000-0000", "Dallas", "Texas", 3);
INSERT INTO store VALUES(22, "555-000-0000", "Austin", "Texas", 4);
INSERT INTO store VALUES(23, "555-000-0000", "Houston", "Texas", 5);
INSERT INTO store VALUES(24, "555-000-0000", "San Diego", "California", 6);
INSERT INTO store VALUES(25, "555-000-0000", "Berkeley", "California", 1);
INSERT INTO store VALUES(26, "555-000-0000", "San Antonio", "Texas", 2);
INSERT INTO store VALUES(27, "555-555-5555", "Toronto", "Ontario", 3);
INSERT INTO store VALUES(28, "555-555-5566", "San Francisco", "California", 4);
INSERT INTO store VALUES(29, "555-555-5777", "New York", "New York", 5);
INSERT INTO store VALUES(30, "555-555-8888", "Tokyo", "Kanto", 6);
INSERT INTO store VALUES(31, "555-555-9999", "Shanghai", "East China", 1);
INSERT INTO store VALUES(32, "555-000-0000", "Chicago", "Illinois", 2);
INSERT INTO store VALUES(33, "555-000-0000", "Buffalo", "New York", 3);
INSERT INTO store VALUES(34, "555-000-0000", "Dallas", "Texas", 4);
INSERT INTO store VALUES(35, "555-000-0000", "Austin", "Texas", 5);
INSERT INTO store VALUES(36, "555-000-0000", "Houston", "Texas", 6);
INSERT INTO store VALUES(37, "555-000-0000", "San Diego", "California", 1);
INSERT INTO store VALUES(38, "555-000-0000", "Berkeley", "California", 2);
INSERT INTO store VALUES(39, "555-000-0000", "San Antonio", "Texas", 3);
INSERT INTO store VALUES(40, "555-555-5555", "Toronto", "Ontario", 4);
INSERT INTO store VALUES(41, "555-555-5566", "San Francisco", "California", 5);
INSERT INTO store VALUES(42, "555-555-5777", "New York", "New York", 6);
INSERT INTO store VALUES(43, "555-555-8888", "Tokyo", "Kanto", 1);
INSERT INTO store VALUES(44, "555-555-9999", "Shanghai", "East China", 2);
INSERT INTO store VALUES(45, "555-000-0000", "Chicago", "Illinois", 3);
INSERT INTO store VALUES(46, "555-000-0000", "Buffalo", "New York", 4);
INSERT INTO store VALUES(47, "555-000-0000", "Dallas", "Texas", 5);
INSERT INTO store VALUES(48, "555-000-0000", "Austin", "Texas", 6);
INSERT INTO store VALUES(49, "555-000-0000", "Houston", "Texas", 1);
INSERT INTO store VALUES(50, "555-000-0000", "San Diego", "California", 2);
INSERT INTO store VALUES(51, "555-000-0000", "Berkeley", "California", 3);
INSERT INTO store VALUES(52, "555-000-0000", "San Antonio", "Texas", 4);


INSERT INTO user_assigned_district VALUES(1, "1");
INSERT INTO user_assigned_district VALUES(2, "1");
INSERT INTO user_assigned_district VALUES(3, "1");
INSERT INTO user_assigned_district VALUES(4, "2");
INSERT INTO user_assigned_district VALUES(5, "2");
INSERT INTO user_assigned_district VALUES(6, "2");
INSERT INTO user_assigned_district VALUES(1, "3");
INSERT INTO user_assigned_district VALUES(1, "4");
INSERT INTO user_assigned_district VALUES(2, "4");
INSERT INTO user_assigned_district VALUES(3, "4");
INSERT INTO user_assigned_district VALUES(4, "4");
INSERT INTO user_assigned_district VALUES(5, "4");
INSERT INTO user_assigned_district VALUES(6, "4");
INSERT INTO user_assigned_district VALUES(1, "5");
INSERT INTO user_assigned_district VALUES(2, "5");
INSERT INTO user_assigned_district VALUES(3, "5");
INSERT INTO user_assigned_district VALUES(4, "5");
INSERT INTO user_assigned_district VALUES(5, "5");
INSERT INTO user_assigned_district VALUES(6, "5");


INSERT INTO holiday (HolidayDate, HolidayName, EmployeeID) VALUES('1983-01-01', 'New Years Day', '1');
INSERT INTO holiday (HolidayDate, HolidayName, EmployeeID) VALUES('1983-12-25', 'Christmas', '1');
INSERT INTO holiday (HolidayDate, HolidayName, EmployeeID) VALUES('1983-10-31', 'Halloween', '2');
INSERT INTO holiday (HolidayDate, HolidayName, EmployeeID) VALUES('1983-06-19', 'Juneteenth', '3');
INSERT INTO holiday (HolidayDate, HolidayName, EmployeeID) VALUES('1983-07-04', 'Independence Day', '1');
INSERT INTO holiday (HolidayDate, HolidayName, EmployeeID) VALUES('1983-02-14', 'Valentines Day', '4');


#BELOW are test cases without the SoldDate as foreign key linked to holiday cos of the problem i mentioned in the earlier post
INSERT product_sold (StoreNumber, PID, SoldDate, Quantity) VALUES ('3','26','2023-02-02','4');
INSERT product_sold (StoreNumber, PID, SoldDate, Quantity) VALUES ('2','25','2021-02-02','5');

INSERT product_sold (StoreNumber, PID, SoldDate, Quantity) VALUES ('4','2','2020-01-02','10');
INSERT product_sold (StoreNumber, PID, SoldDate, Quantity) VALUES ('5','4','2019-10-19','2');

INSERT product_sold (StoreNumber, PID, SoldDate, Quantity) VALUES ('6','10','2019-03-15','8');
INSERT product_sold (StoreNumber, PID, SoldDate, Quantity) VALUES ('7','11','2018-04-10','7');


INSERT product_sold (StoreNumber, PID, SoldDate, Quantity) VALUES ('6','10','2008-02-01','14');
INSERT product_sold (StoreNumber, PID, SoldDate, Quantity) VALUES ('11','21','2009-12-31','30');


INSERT discount (DiscountDate, PID, DiscountPrice) VALUES ('2021-02-02','25','20');


insert into audit_log values ('2019-10-19 10:19:00', '1','Category Report');
insert into audit_log values ('2019-12-19 10:19:00', '2','Store Revenue by Year by State');


INSERT INTO report VALUES("Manufacturer's Product Report");
INSERT INTO report VALUES('Category Report');
INSERT INTO report VALUES('Actual versus Predicted Revenue for GPS units');
INSERT INTO report VALUES('Air Conditioners on Groundhog Day?');
INSERT INTO report VALUES('Store Revenue by Year by State');
INSERT INTO report VALUES('State with Highest Volume for each Category');
INSERT INTO report VALUES('Revenue by Population');

