CREATE DATABASE `sales_payment`;

USE `sales_payment`;
--
-- Table structure for table `gift_card`
--

DROP TABLE IF EXISTS `gift_card`;

CREATE TABLE `gift_card` (
  `gift_id` int(11) NOT NULL AUTO_INCREMENT,
  `promo_number` double NOT NULL,
  `card_balance` float NOT NULL,
  `ticket_id` int(11) DEFAULT NULL,
  `customer_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`gift_id`),
  KEY `ticket_id` (`ticket_id`),
  KEY `customer_id` (`customer_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;


--
-- Dumping data for table `gift_card`
--

LOCK TABLES `gift_card` WRITE;

INSERT INTO `gift_card` VALUES (1,26576,10,NULL,NULL);

UNLOCK TABLES;

--
-- Table structure for table `registers_table`
--

DROP TABLE IF EXISTS `registers_table`;

CREATE TABLE `registers_table` (
  `register_id` int(11) NOT NULL AUTO_INCREMENT,
  `open_total` float NOT NULL,
  `close_total` float DEFAULT NULL,
  `register_num` int(11) NOT NULL,
  `open_emp_id` int(11) NOT NULL,
  `close_emp_id` int(11) DEFAULT NULL,
  `open_time` datetime NOT NULL,
  `close_time` datetime DEFAULT NULL,
  `drop_time` datetime DEFAULT NULL,
  `drop_emp_id` int(11) DEFAULT NULL,
  `drop_total` float DEFAULT NULL,
  `note` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`register_id`),
  KEY `fk_open_emp_id` (`open_emp_id`),
  KEY `fk_close_emp_id` (`close_emp_id`),
  KEY `fk_drop_emp_id` (`drop_emp_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;


--
-- Dumping data for table `registers_table`
--

LOCK TABLES `registers_table` WRITE;

INSERT INTO `registers_table` VALUES (1,100,NULL,1,101,NULL,'2024-10-25 15:50:56',NULL,NULL,NULL,NULL,'Initial register');

UNLOCK TABLES;

--
-- Table structure for table `tax_table`
--

DROP TABLE IF EXISTS `tax_table`;

CREATE TABLE `tax_table` (
  `TTID` int(11) NOT NULL AUTO_INCREMENT,
  `tax_year` year(4) NOT NULL,
  `state_tax` float NOT NULL,
  `county_tax` float NOT NULL,
  `city_rate` float NOT NULL,
  `tax_rate` float NOT NULL,
  PRIMARY KEY (`TTID`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;


--
-- Dumping data for table `tax_table`
--

LOCK TABLES `tax_table` WRITE;
;
INSERT INTO `tax_table` VALUES (1,2020,0.04,0.04,0.08,0.08);
;
UNLOCK TABLES;

--
-- Table structure for table `ticket_system`
--

DROP TABLE IF EXISTS `ticket_system`;

CREATE TABLE `ticket_system` (
  `ticket_id` int(11) NOT NULL AUTO_INCREMENT,
  `date` date NOT NULL,
  `company_name` varchar(50) DEFAULT NULL,
  `time` time NOT NULL,
  `quantity` int(11) NOT NULL,
  `subtotal` float NOT NULL,
  `total` float NOT NULL,
  `cost` float NOT NULL,
  `discount` float DEFAULT NULL,
  `tax` float NOT NULL,
  `tax_rate` float NOT NULL,
  `cash` float NOT NULL,
  `credit` float NOT NULL,
  `cart_purchase` tinyint(1) NOT NULL,
  `customer_id` int(11) DEFAULT NULL,
  `employee_id` int(11) NOT NULL,
  PRIMARY KEY (`ticket_id`),
  KEY `customer_id` (`customer_id`),
  KEY `employee_id` (`employee_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;
;

--
-- Dumping data for table `ticket_system`
--

LOCK TABLES `ticket_system` WRITE;
;
INSERT INTO `ticket_system` VALUES (1,'2024-10-25','Company A','15:49:26',2,50,55,50,5,5,0.1,30,25,1,NULL,101);
;
UNLOCK TABLES;
