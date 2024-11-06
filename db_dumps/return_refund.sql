CREATE DATABASE `return_refund`;

USE `return_refund`;

--
-- Table structure for table `return_table`
--

DROP TABLE IF EXISTS `return_table`;

CREATE TABLE `return_table` (
  `RTID` int(11) NOT NULL AUTO_INCREMENT,
  `ticket_id` int(11) NOT NULL,
  `date` date NOT NULL,
  `time` time NOT NULL,
  `refunds` float NOT NULL,
  `exchanges` float DEFAULT NULL,
  PRIMARY KEY (`RTID`),
  KEY `ticket_id` (`ticket_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;


--
-- Dumping data for table `return_table`
--

LOCK TABLES `return_table` WRITE;

UNLOCK TABLES;


