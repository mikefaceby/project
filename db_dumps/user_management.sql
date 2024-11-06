CREATE DATABASE `user_management`;

USE `user_management`;

-- Table structure for table `customer_info`

DROP TABLE IF EXISTS `customer_info`;

CREATE TABLE `customer_info` (
  `customer_id` int(11) NOT NULL AUTO_INCREMENT,
  `email` varchar(50) NOT NULL,
  `password` varchar(60) NOT NULL,
  `first_name` varchar(50) NOT NULL,
  `last_name` varchar(50) NOT NULL,
  `phone_number` double NOT NULL,
  `rewards` float DEFAULT NULL,
  `street_address` varchar(50) NOT NULL,
  `city` varchar(50) NOT NULL,
  `state` varchar(2) NOT NULL,
  `zip_code` int(11) NOT NULL,
  PRIMARY KEY (`customer_id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;


--
-- Dumping data for table `customer_info`
--

LOCK TABLES `customer_info` WRITE;

INSERT INTO `customer_info` VALUES (1,'johnnyfran20002@gmail.com','passwood','Johnny','Tejada',6463214487,33,'10005 Hawk Drive ','Queens','NY',12321),(2,'tylerherro23@gmail.com','password','Tyler','Herro',3475436578,90,'12th Street','New York','NY',9874),(3,'bronny45@hotmail.com','lebron','Bronny','James',2124567656,44,'21 Wood Street','Woodhaven','VT',7384),(4,'kyrieirving2@hotmail.com','kyrie','Kyrie','Irving',2123434567,14,'74 2nd Ave','New York','NY',12343),(6,'michaelj23@gmail.com','jordan','Michael','Jordan',2125468796,44,'14th Street','Chicago ','IL',76854),(7,'cp3@yahoo.com','phzsuns','Chris','Paul',8452341004,0,'346 Broad St','Los Angeles','CA',90212),(9,'bgates19@hotmail.com','apple','Bill','Gates',3479845093,0,'109 19th Street','Sacramento','CA',29343);

UNLOCK TABLES;

--
-- Table structure for table `employee_info`
--

DROP TABLE IF EXISTS `employee_info`;

CREATE TABLE `employee_info` (
  `employee_id` int(11) NOT NULL AUTO_INCREMENT,
  `email` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL,
  `pin_number` int(11) DEFAULT NULL,
  `first_name` varchar(50) NOT NULL,
  `last_name` varchar(50) NOT NULL,
  `user_id` double DEFAULT NULL,
  `phone_number` double NOT NULL,
  `SSN` double DEFAULT NULL,
  `street_address` varchar(50) NOT NULL,
  `city` varchar(50) NOT NULL,
  `state` varchar(2) NOT NULL,
  `zip_code` int(11) NOT NULL,
  `start_date` date DEFAULT NULL,
  `company_name` varchar(50) NOT NULL,
  `number_of_stores` varchar(11) DEFAULT NULL,
  `user_type` int(11) NOT NULL,
  `customer_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`employee_id`),
  UNIQUE KEY `customer_id` (`customer_id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;


--
-- Dumping data for table `employee_info`
--

LOCK TABLES `employee_info` WRITE;

INSERT INTO `employee_info` VALUES (1,'johnnyfran20002@gmail.com','passwood',231,'Johnny','Tejada',214564056,6463214487,756434736,'10005 Hawk Drive','Queens','NY',11105,'2020-11-02','Walmart','3',1,1),(2,'tylerherro23@gmail.com','herro',112,'Tyler','Herro',435678987,3475436897,123456789,'12th Street','New York','NY',9873,'2019-07-01','Shop Rite',NULL,2,2),(3,'bronny45@hotmail.com','lebron',113,'Bronny','James',112323454,2124568745,78234325,'21 Wood Street','Woodhaven','VT',12321,'2019-03-02','Walmart',NULL,2,3),(4,'usher54@aim.com','usher',555,'Usher','Man',345432345,8454342212,958674345,'76 Cross Street','Houston','NY',85743,'2020-12-05','Walmart',NULL,2,NULL),(5,'chrisbrown@gmail.com','pass',111,'Chris','Brown',111111111,7187654783,746378273,'19 West Street','Denver','CL',43454,'2019-07-03','Walmart',NULL,2,NULL),(6,'kyrieirving2@hotmail.com','kyrie',705,'Kyrie','Irving',123456789,2129857843,123456789,'71 2nd Ave','New York','NY',12343,'2017-07-03','Tops','4',1,4);

UNLOCK TABLES;

--
-- Table structure for table `stores`
--

DROP TABLE IF EXISTS `stores`;

CREATE TABLE `stores` (
  `SID` int(11) NOT NULL AUTO_INCREMENT,
  `company_name` varchar(50) NOT NULL,
  `employee_id` int(11) NOT NULL,
  PRIMARY KEY (`SID`),
  KEY `employee_id` (`employee_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;


--
-- Dumping data for table `stores`
--

LOCK TABLES `stores` WRITE;

INSERT INTO `stores` VALUES (1,'Company A',101),(2,'Company B',102),(3,'Company C',103);

UNLOCK TABLES;


