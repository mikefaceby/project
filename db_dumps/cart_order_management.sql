CREATE DATABASE `cart_order_management`;

USE `cart_order_management`;


-- Table structure for table `cart`
--

DROP TABLE IF EXISTS `cart`;

CREATE TABLE `cart` (
  `cart_id` int(11) NOT NULL AUTO_INCREMENT,
  `CID` int(11) NOT NULL,
  `qty` int(11) NOT NULL,
  `product_id` int(11) NOT NULL,
  PRIMARY KEY (`cart_id`),
  KEY `product_id` (`product_id`),
  KEY `CID` (`CID`)
) ENGINE=InnoDB AUTO_INCREMENT=241 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;


--
-- Dumping data for table `cart`
--

LOCK TABLES `cart` WRITE;

UNLOCK TABLES;

--
-- Table structure for table `cart_inprogress`
--

DROP TABLE IF EXISTS `cart_inprogress`;

CREATE TABLE `cart_inprogress` (
  `CID` int(11) NOT NULL AUTO_INCREMENT,
  `customer_id` int(11) DEFAULT NULL,
  `ticket_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`CID`),
  KEY `customer_id` (`customer_id`),
  KEY `ticket_id` (`ticket_id`)
) ENGINE=InnoDB AUTO_INCREMENT=106 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;


--
-- Dumping data for table `cart_inprogress`
--

LOCK TABLES `cart_inprogress` WRITE;

UNLOCK TABLES;

--
-- Table structure for table `item_list`
--

DROP TABLE IF EXISTS `item_list`;

CREATE TABLE `item_list` (
  `ITID` int(11) NOT NULL AUTO_INCREMENT,
  `CID` int(11) NOT NULL,
  `qty` int(11) NOT NULL,
  `product_id` int(11) NOT NULL,
  PRIMARY KEY (`ITID`),
  KEY `CID` (`CID`),
  KEY `product_id` (`product_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;


--
-- Dumping data for table `item_list`
--

LOCK TABLES `item_list` WRITE;

UNLOCK TABLES;
