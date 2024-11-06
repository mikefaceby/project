CREATE DATABASE `product_management`;

USE `product_management`;

--
-- Table structure for table `orders`
--

DROP TABLE IF EXISTS `orders`;

CREATE TABLE `orders` (
  `OID` int(11) NOT NULL AUTO_INCREMENT,
  `OTID` int(11) NOT NULL,
  `stock_amount` int(11) NOT NULL,
  `product_id` int(11) NOT NULL,
  PRIMARY KEY (`OID`),
  KEY `OTID` (`OTID`),
  KEY `product_id` (`product_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;


--
-- Dumping data for table `orders`
--

LOCK TABLES `orders` WRITE;

UNLOCK TABLES;

--
-- Table structure for table `orders_ticket`
--

DROP TABLE IF EXISTS `orders_ticket`;

CREATE TABLE `orders_ticket` (
  `OTID` int(11) NOT NULL AUTO_INCREMENT,
  `date` date DEFAULT NULL,
  `time` time DEFAULT NULL,
  `quantity` int(11) DEFAULT NULL,
  `subtotal` float DEFAULT NULL,
  `total` float DEFAULT NULL,
  `discount` float DEFAULT NULL,
  `tax` float DEFAULT NULL,
  `tax_rate` float DEFAULT NULL,
  `cash` float DEFAULT NULL,
  `credit` float DEFAULT NULL,
  `status` int(11) DEFAULT NULL,
  `employee_id` int(11) DEFAULT NULL,
  `vendor_id` int(11) NOT NULL,
  PRIMARY KEY (`OTID`),
  KEY `employee_id` (`employee_id`),
  KEY `vendor_id` (`vendor_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;


--
-- Dumping data for table `orders_ticket`
--

LOCK TABLES `orders_ticket` WRITE;

UNLOCK TABLES;

--
-- Table structure for table `product_inventory`
--

DROP TABLE IF EXISTS `product_inventory`;

CREATE TABLE `product_inventory` (
  `product_id` int(11) NOT NULL AUTO_INCREMENT,
  `brand` varchar(50) NOT NULL,
  `description` varchar(50) NOT NULL,
  `productName` varchar(50) NOT NULL,
  `productType` varchar(50) NOT NULL,
  `productSubType` varchar(50) NOT NULL,
  `unit_price` float NOT NULL,
  `cost` float NOT NULL,
  `in_stock` int(11) NOT NULL,
  `vendor_id` int(11) NOT NULL,
  PRIMARY KEY (`product_id`),
  KEY `vendor_id` (`vendor_id`)
) ENGINE=InnoDB AUTO_INCREMENT=63 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;


--
-- Dumping data for table `product_inventory`
--

LOCK TABLES `product_inventory` WRITE;

INSERT INTO `product_inventory` VALUES (1,'Fat Free','Half and Half','Dairy Pure','Dairy','Milk',8.99,6.99,10,1),(2,'Organic Whole Milk','Organic Vitamin D Milk','Horizon','Dairy','Milk',10.45,8.99,3,1),(3,'Cheddar Sliced Cheese','Natural Medium','Sargento','Dairy','Cheese',7.89,5.15,5,1),(4,'Irish Cheddar','Reverse Cheddar Cheese','Kerrygold Cheddar','Dairy','Cheese',9.99,6.99,65,1),(5,'Organic Banana','2lbs','Dole','Produce','Banana',4.99,3.45,56,1),(6,'Strawberries','1lb package','Driscolls','Produce','Strawberries',8.95,6.99,45,1),(7,'Red Cherry Tomato','10.5oz package','Cherry','Produce','Tomato',5.59,3.99,21,1),(8,'Organic Red Grape Tomatoes','10 oz package','Brandywine','Produce','Tomato',8.99,5.75,2,1),(9,'Sht Cuts Grlld Ital Chic Strip','22oz','Perdue chicken breast','Poultry','ChickenBreast',7.49,6.99,7,2),(10,'Sht Cuts Grlld Ital Chic Legs','22oz','Perdue chicken legs','Poultry','ChickenLeg',7.49,6.99,12,2),(12,'Five Star Beef','16oz','Tyson steaks','Beef','Steak',10.49,9.99,19,2),(13,'Five Star Flanks','30oz','Tyson flanks','Beef','Flank',14.49,12.99,60,2),(14,'Bush','2oz','Bushs Black Beans','DryGoods','Beans',4.49,2.99,20,2),(15,'Heinz','5oz','Heinz Baked Beans','DryGoods','Beans',5.49,4.99,60,2),(16,'Goya','4oz','Goya Black Beans','DryGoods','Beans',6.99,5.99,6,2),(17,'Hormel Foods','3oz','Canned Spam','DryGoods','Cans',3.49,2.99,50,2),(18,'Dole','3oz','Doles Canned Tropical Fruit','DryGoods','Cans',4.49,2.99,60,2),(19,'Campbells','3oz','Campbells Canned Soup','DryGoods','Cans',3.49,2.99,50,2),(20,'Healthy Choice','4oz','Healthy Choice Canned Peas','DryGoods','Cans',3.65,2.89,50,2),(21,'Heckers','4lb','Heckers All Purpose Flour','DryGoods','Flour',10.99,9.99,68,2),(22,'Bobs Red Mill','4lb','Bobs Red Mill All Purpose Flour','DryGoods','Flour',12.99,10.99,32,2),(23,'King Arthur','4lb','King Arthur All Purpose Flour','DryGoods','Flour',13.99,12.99,54,2),(24,'Pillsbury','4oz','Pillsburrys Best All Purpose Flour','DryGoods','Flour',12.99,11.99,61,2),(25,'Domino','5oz','Domino Sugar','DryGoods','Sugar',6.99,5.99,6,2),(26,'NJOY','5oz','NJOY Pure Cane Sugar','DryGoods','Sugar',7.99,6.99,62,2),(27,'Anthonys','5oz','Organic Cane Sugar by Anthonys','DryGoods','Sugar',7.99,6.99,62,2),(28,'Pedigree','7lb','Pedigrees Roasted Chicken','PetFood','Dog',10.99,9.99,64,2),(29,'Blue Wilderness','7lb','Blue Wilderness Salmon','PetFood','Dog',6.99,5.99,6,2),(30,'Cesars','5oz','Cesars Filet','PetFood','Dog',4.99,3.99,63,2),(31,'Meow Mix','7lb','Meow Mix Dry Chicken','PetFood','Cat',6.99,5.99,7,2),(32,'Purina','7lb','Purina Salmon Flavor','PetFood','Cat',6.99,5.99,73,2),(33,'American Journey','7lb','American Journey turkey and Chicken','PetFood','Cat',8.99,7.99,45,2),(34,'Nine Lives','7lb','Nine Lives Daily Essentials','PetFood','Cat',6.99,5.99,73,2),(35,'Barilla','5oz','Barilla Spaghetti','Pasta','Spaghetti',6.99,5.99,62,2),(36,'De Cecco','5oz','De Cecco Spaghetti','Pasta','Spaghetti',8.99,6.99,64,2),(37,'Whole Foods','5oz','Whole Foods 365 Spaghetti','Pasta','Spaghetti',7.99,6.99,63,2),(38,'Palmini','5oz','Palmini Low Carb Lasagna','Pasta','Lasagna',8.99,6.99,64,2),(39,'Palmini','5oz','Palmini Low Carb Lasagna','Pasta','Lasagna',12.99,10.99,64,2),(40,'Chef Boyardee','5oz','Chef Boyardee Lasagna','Pasta','Lasagna',9.99,8.99,64,2),(41,'Quinoa','7oz','Quinoa Mac and Cheese','Pasta','Macaroni',13.99,12.99,644,2),(42,'Mrs Leepers','7oz','Mrs Leepers Gluten free Mac and Cheese','Pasta','Macaroni',14.99,13.99,634,2),(43,'Kraft','7oz','Kraft Macaroni and Cheese','Pasta','Macaroni',14.99,13.99,264,2),(44,'Velveeta','7oz','Velveeta Macaroni','Pasta','Macaroni',13.99,12.99,1624,2),(45,'Ronzoni','7oz','Ronzoni Rigatoni','Pasta','Rigatoni',12.99,11.99,14,2),(46,'Organic','7oz','Organic Brown Rigatoni','Pasta','Rigatoni',15.99,12.99,114,2),(47,'Ronzoni','7oz','Garafalo Rigatoni','Pasta','Rigatoni',13.99,12.99,134,2),(48,'Angel Soft','2lb','Angel Soft Single Sheet','Bathroom','ToiletPaper',12.99,11.99,16,2),(49,'Charmin Ultrta','2lb','Charmin Ultrta Soft','Bathroom','ToiletPaper',15.99,14.99,164,2),(50,'Charmin Ultrta','2lb','Charmin Ultrta Strong','Bathroom','ToiletPaper',16.99,15.99,1645,2),(51,'Green Forest','2lb','Green Forest Two Ply','Bathroom','ToiletPaper',16.99,15.99,124,2),(52,'Soft Soap','2oz','Soft Soap Fresh Breeze','Bathroom','HandSoap',13.99,12.99,14,2),(53,'Dial','2oz','Dial Coconut Water','Bathroom','HandSoap',10.99,9.99,16,2),(54,'Meyers','4lb','Meyers Clean Day','Bathroom','HandSoap',11.99,10.99,23,2),(55,'Meyers','4lb','Meyers Fresh Breeze','Bathroom','HandSoap',10.99,9.99,14,2),(56,'Febreze','7oz','Febreze Spring Breeze','Bathroom','AirFreshner',7.99,6.99,19,2),(57,'Febreze','7oz','Febreze Outdoor Fresh','Bathroom','AirFreshner',6.99,5.99,6,2),(58,'Air Wick','5oz','Air Wick Air Freshener','Bathroom','AirFreshner',10.99,9.99,60,2),(59,'Bath and Body Works','3oz','Bath and Body Works Scented','Bathroom','AirFreshner',10.99,9.99,53,2),(60,'Crest','3oz','Crest 3D White Toothpaste','Bathroom','Toothpaste',9.99,8.99,64,2),(61,'Colgate','3oz','Colgate Advanced Whitening Toothpaste','Bathroom','Toothpaste',8.99,7.99,45,2),(62,'Sensodyne','3oz','Sensodyne Whitening Toothpaste','Bathroom','Toothpaste',8.99,7.99,64,2);

UNLOCK TABLES;

--
-- Table structure for table `vendorinfo`
--

DROP TABLE IF EXISTS `vendorinfo`;

CREATE TABLE `vendorinfo` (
  `vendor_id` int(11) NOT NULL AUTO_INCREMENT,
  `company_name` varchar(50) NOT NULL,
  `department` varchar(100) NOT NULL,
  `street_address` varchar(50) NOT NULL,
  `city` varchar(50) NOT NULL,
  `state` varchar(2) NOT NULL,
  `zip_code` int(11) NOT NULL,
  `phone_number` double NOT NULL,
  `fax_number` double NOT NULL,
  `email` varchar(50) NOT NULL,
  PRIMARY KEY (`vendor_id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;


--
-- Dumping data for table `vendorinfo`
--

LOCK TABLES `vendorinfo` WRITE;

INSERT INTO `vendorinfo` VALUES (1,'Krasdale Foods Inc','Frozen and Dairy','400 Food Center Dr','Bronx','NY',10474,7183781100,9146975200,'web-inquires@krasdalefoods.com'),(2,'J & J NY Distributors','Poultry','1343 Lafayette Ave','Bronx','NY',10474,7185890517,7185890517,'info@jjnycorp.com');

UNLOCK TABLES;

--
-- Current Database: `cart_order_management`
--