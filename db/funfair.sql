-- MySQL dump 10.16  Distrib 10.1.30-MariaDB, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: funfair
-- ------------------------------------------------------
-- Server version	10.1.30-MariaDB-0ubuntu0.17.10.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `Directions`
--

DROP TABLE IF EXISTS `Directions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Directions` (
  `Direction_Id` varchar(10) NOT NULL DEFAULT '',
  `Description` varchar(20) NOT NULL DEFAULT '',
  PRIMARY KEY (`Direction_Id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Directions`
--

LOCK TABLES `Directions` WRITE;
/*!40000 ALTER TABLE `Directions` DISABLE KEYS */;
INSERT INTO `Directions` VALUES ('e','East'),('n','North'),('ne','Northeast'),('nw','Northwest'),('s','South'),('se','Southeast'),('sw','Southwest'),('w','West');
/*!40000 ALTER TABLE `Directions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Has_passages`
--

DROP TABLE IF EXISTS `Has_passages`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Has_passages` (
  `Place_Id` int(11) NOT NULL,
  `Has_passagesPlace_Id` int(11) NOT NULL,
  `Direction_Id` varchar(10) NOT NULL DEFAULT '',
  PRIMARY KEY (`Place_Id`,`Has_passagesPlace_Id`),
  KEY `Has_passagesPlace_Id` (`Has_passagesPlace_Id`),
  CONSTRAINT `has_passages_ibfk_1` FOREIGN KEY (`Place_Id`) REFERENCES `Places` (`Place_Id`),
  CONSTRAINT `has_passages_ibfk_2` FOREIGN KEY (`Has_passagesPlace_Id`) REFERENCES `Places` (`Place_Id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Has_passages`
--

LOCK TABLES `Has_passages` WRITE;
/*!40000 ALTER TABLE `Has_passages` DISABLE KEYS */;
INSERT INTO `Has_passages` VALUES (1,2,'n'),(2,1,'s'),(2,3,'w'),(2,5,'sw'),(2,7,'se'),(2,9,'n'),(3,2,'e'),(3,4,'n'),(4,3,'s'),(4,9,'ne'),(5,2,'sw'),(5,6,'se'),(5,8,'e'),(5,9,'nw'),(6,5,'nw'),(6,7,'s'),(6,8,'n'),(7,2,'nw'),(7,6,'n'),(8,5,'w'),(8,6,'s'),(9,2,'s'),(9,4,'sw'),(9,5,'se'),(9,10,'ne'),(9,11,'n'),(9,12,'nw'),(10,9,'sw'),(11,9,'s'),(11,12,'w'),(12,9,'se'),(12,11,'e'),(12,13,'w'),(13,12,'e');
/*!40000 ALTER TABLE `Has_passages` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Item_types`
--

DROP TABLE IF EXISTS `Item_types`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Item_types` (
  `Itemtype_Id` int(11) NOT NULL,
  `Name` varchar(40) NOT NULL,
  `Place_Id` int(11) NOT NULL,
  PRIMARY KEY (`Itemtype_Id`),
  KEY `Place_Id` (`Place_Id`),
  CONSTRAINT `item_types_ibfk_1` FOREIGN KEY (`Place_Id`) REFERENCES `Places` (`Place_Id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Item_types`
--

LOCK TABLES `Item_types` WRITE;
/*!40000 ALTER TABLE `Item_types` DISABLE KEYS */;
INSERT INTO `Item_types` VALUES (1,'Ride Tickets',1),(2,'Game Prizes',7),(3,'Drinks from Cafe',12),(4,'Foods from Cafe',12),(5,'Candies',11);
/*!40000 ALTER TABLE `Item_types` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Item_types_Action`
--

DROP TABLE IF EXISTS `Item_types_Action`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Item_types_Action` (
  `Action` varchar(11) NOT NULL DEFAULT '',
  `Itemtype_Id` int(11) NOT NULL,
  PRIMARY KEY (`Action`,`Itemtype_Id`),
  KEY `Itemtype_Id` (`Itemtype_Id`),
  CONSTRAINT `item_types_action_ibfk_1` FOREIGN KEY (`Itemtype_Id`) REFERENCES `Item_types` (`Itemtype_Id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Item_types_Action`
--

LOCK TABLES `Item_types_Action` WRITE;
/*!40000 ALTER TABLE `Item_types_Action` DISABLE KEYS */;
INSERT INTO `Item_types_Action` VALUES ('Buy',1),('Buy',3),('Buy',4),('Buy',5),('Drink',3),('Eat',1),('Eat',4),('Eat',5);
/*!40000 ALTER TABLE `Item_types_Action` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Items`
--

DROP TABLE IF EXISTS `Items`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Items` (
  `Item_Id` int(11) NOT NULL,
  `Name` varchar(40) DEFAULT NULL,
  `Itemtype_Id` int(11) NOT NULL,
  `Player_Id` int(11) DEFAULT NULL,
  `Alias` text,
  PRIMARY KEY (`Item_Id`),
  KEY `Itemtype_Id` (`Itemtype_Id`),
  KEY `Player_Id` (`Player_Id`),
  CONSTRAINT `items_ibfk_1` FOREIGN KEY (`Itemtype_Id`) REFERENCES `Item_types` (`Itemtype_Id`),
  CONSTRAINT `items_ibfk_2` FOREIGN KEY (`Player_Id`) REFERENCES `Player` (`Player_Id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Items`
--

LOCK TABLES `Items` WRITE;
/*!40000 ALTER TABLE `Items` DISABLE KEYS */;
INSERT INTO `Items` VALUES (1,'Ride tickets',1,NULL,'tickets; ride tickets'),(2,'Stuffed Teddy Bear',2,NULL,NULL),(3,'Blue pencil',2,NULL,NULL),(4,'Funfair themed playing cards',2,NULL,NULL),(5,'Cup of coffee',3,NULL,'coffee; coffee cup; cup of coffee'),(6,'Cup of tea',3,NULL,'tea; tea cup; cup of tea'),(7,'Can of soda',3,NULL,'soda; can of soda; soda can; soda bottle; bottle of soda'),(8,'Bottle of water',3,NULL,'water; water bottle; bottle of water; '),(9,'Cinnamon bun',4,NULL,'bun; cinnamon bun'),(10,'Cookie',4,NULL,'cookie; chocolate cookie'),(11,'Chocolate brownie',4,NULL,'brownie; brownies; chololate brownie; chocolate brownies'),(12,'Pink candy floss',5,NULL,'candy floss; cotton candy; pink candy floss; pink cotton candy'),(13,'Candies',5,NULL,'candies; mixed candies; candy; mixed sweets; sweets'),(14,'Licorice',5,NULL,'licorice; loose licorice; piece of licorice');
/*!40000 ALTER TABLE `Items` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Line`
--

DROP TABLE IF EXISTS `Line`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Line` (
  `Lines_Id` int(11) NOT NULL AUTO_INCREMENT,
  `Line_Text` text NOT NULL,
  `Person_Id` int(11) NOT NULL,
  `Place_Id` int(11) DEFAULT NULL,
  `Item_Id` int(11) DEFAULT NULL,
  `Connects_Person_Id` int(11) DEFAULT NULL,
  `Is_tip` tinyint(1) NOT NULL,
  PRIMARY KEY (`Lines_Id`),
  KEY `Person_Id` (`Person_Id`),
  KEY `Place_Id` (`Place_Id`),
  KEY `Item_Id` (`Item_Id`),
  KEY `Connects_Person_Id` (`Connects_Person_Id`),
  CONSTRAINT `Line_Persons_FK` FOREIGN KEY (`Connects_Person_Id`) REFERENCES `Persons` (`Person_Id`),
  CONSTRAINT `line_ibfk_1` FOREIGN KEY (`Person_Id`) REFERENCES `Persons` (`Person_Id`),
  CONSTRAINT `line_ibfk_2` FOREIGN KEY (`Place_Id`) REFERENCES `Places` (`Place_Id`),
  CONSTRAINT `line_ibfk_3` FOREIGN KEY (`Item_Id`) REFERENCES `Items` (`Item_Id`)
) ENGINE=InnoDB AUTO_INCREMENT=35 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Line`
--

LOCK TABLES `Line` WRITE;
/*!40000 ALTER TABLE `Line` DISABLE KEYS */;
INSERT INTO `Line` VALUES (1,'There is bad blood around in our funfair. Walk around to find out!',8,1,NULL,NULL,0),(2,'You want to buy ride tickets? Okey, here you go.',8,1,1,NULL,0),(3,'Would you have guessed the clown is my mother? It feels like I\'ve live my whole life here. Sometimes I wonder about the meaning of life. I study philosophy.',8,1,NULL,NULL,0),(4,'My name is Elna and I\'m the funfair clown.',1,2,NULL,NULL,0),(5,'I’m proud of my parents. There isn’t many funfairs nowadays in Finland anymore. I’m bored but this is my life.',5,6,NULL,NULL,0),(6,'It’s such a nice day today. I think the kids will have a blast when I perform later. The janitor roasted some marshmallows last night.',1,2,NULL,NULL,0),(7,'My name Is Valter and I\'m the funfair magician. ',2,7,NULL,NULL,0),(8,'The magician looks at you and winks his eye. You don\'t really know what to think of him. ',2,7,NULL,NULL,0),(9,'I’m glad everything is going so smoothly today. I heard there is almost no crime in this town.',3,5,NULL,NULL,0),(10,'I think this place is really dull.',5,6,NULL,NULL,0),(11,'I think my cookies are excellent today. My name is Peter by the way.',6,12,NULL,NULL,0),(12,'Blah blah! My name is Sara.',5,6,NULL,NULL,0),(13,'I prefer dark roast when it comes to coffee.',6,12,NULL,NULL,0),(14,'I would love to cycle around this town. It’s the best when you go around a lot, you get to see new places and learn new magic tricks.',2,7,NULL,NULL,0),(15,'It seems a bit slower today. Maybe I will read today. I like to travel and sometimes I feel like travelling when exploring a new book!',1,2,NULL,NULL,0),(16,'You can come talk to me if you see a criminal.',3,5,NULL,NULL,0),(17,'I\'m Linda.',3,5,NULL,NULL,0),(18,'Oh my shoes! I\'d love to talk to you but it\'s so crazy here today.',4,3,NULL,NULL,0),(19,'Are you just like one of these vandals? Oh maybe not, you seem a bit older. I\'m Lena by the way. Sometimes I think I will have grey hair at the end of summer becouse all the reckless driving.',4,3,NULL,NULL,0),(20,'The bumper car operator is busy yells at some children. You think it\'s better not to bother her.',4,3,NULL,NULL,0),(21,'You know what\'s the purpose of reindeer? To make grass grow hehehe.',6,12,NULL,NULL,0),(22,'\"I\'m Matilda. \" The candy shop keeper says while arranging all the candy.',7,11,NULL,NULL,0),(23,'This is a cool place to work. Meet new people, see new places, eat lots of candy floss. I study geopgraphy. Won\'t really work for me as practical training for school but no worries.',7,11,NULL,NULL,0),(24,'I make excellent candy floss. You should try some.',7,11,NULL,NULL,0),(25,'I\'m Arthur. I wish the ferris wheel is repaired soon.',10,8,NULL,NULL,0),(26,'...',9,13,NULL,NULL,0),(27,'I like people who drink coffee. They are trustworthy. Here you go, enjoy!',6,12,5,NULL,0),(28,'We have a wide selection of different tea varieties. Black, white, green, chai, blue, rainbow, bubblegum..eh can\'t find anything else but black though. Here you go!',6,12,6,NULL,0);
/*!40000 ALTER TABLE `Line` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Line_templates`
--

DROP TABLE IF EXISTS `Line_templates`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Line_templates` (
  `Id` int(11) NOT NULL,
  `Text` varchar(100) NOT NULL,
  `Positive` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`Id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Line_templates`
--

LOCK TABLES `Line_templates` WRITE;
/*!40000 ALTER TABLE `Line_templates` DISABLE KEYS */;
INSERT INTO `Line_templates` VALUES (1,'I think %s and %s will get along well.',1),(2,'I think %s could get easily along with %s.',1),(3,'I think %s and %s have a similar sense of humour.',1),(4,'I think %s and %s won\'t get along very well.',0);
/*!40000 ALTER TABLE `Line_templates` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Persons`
--

DROP TABLE IF EXISTS `Persons`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Persons` (
  `Person_Id` int(11) NOT NULL,
  `Name` varchar(30) NOT NULL DEFAULT '',
  `Connectable` int(11) DEFAULT NULL,
  `Place_Id` int(11) NOT NULL,
  `Connects_Person_Id` int(11) DEFAULT NULL,
  `Alias` text,
  `Is_Connected` tinyint(1) NOT NULL DEFAULT '0',
  PRIMARY KEY (`Person_Id`),
  KEY `Place_Id` (`Place_Id`),
  KEY `Connects_Person_Id` (`Connects_Person_Id`),
  CONSTRAINT `persons_ibfk_1` FOREIGN KEY (`Place_Id`) REFERENCES `Places` (`Place_Id`),
  CONSTRAINT `persons_ibfk_2` FOREIGN KEY (`Connects_Person_Id`) REFERENCES `Persons` (`Person_Id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Persons`
--

LOCK TABLES `Persons` WRITE;
/*!40000 ALTER TABLE `Persons` DISABLE KEYS */;
INSERT INTO `Persons` VALUES (1,'Elna the Clown',1,2,NULL,'clown;the clown;pelle;elna;elna the clown',0),(2,'The Magician',1,7,NULL,'valter;magician;game keeper',0),(3,'Security Officer',1,5,NULL,'security;security officer;the security officer;linda',0),(4,'Bumper Car Operator',1,3,NULL,'lena;bumper operator;bumper cars operator;',0),(5,'Carousel Operator',1,6,NULL,'sara;carousel operator;carousel',0),(6,'Cafe Keeper',1,12,NULL,'peter;cafe keeper;cafe',0),(7,'Candy Shop Keeper',1,11,NULL,'matilda;candy shop keeper;candy keeper',0),(8,'Ticket Vendor',NULL,1,NULL,'edvin;ticker seller;ticket vendor',0),(9,'Funfair Director',NULL,13,NULL,'director;birgitta;funfair director;boss',0),(10,'Ferris Wheel Operator',NULL,8,NULL,'arthur;ferris wheel operator;ferris operator',0);
/*!40000 ALTER TABLE `Persons` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Places`
--

DROP TABLE IF EXISTS `Places`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Places` (
  `Place_Id` int(11) NOT NULL,
  `Name` varchar(30) NOT NULL DEFAULT '',
  `Description` text NOT NULL,
  `Details` text,
  `Alias` text,
  `Action` text,
  PRIMARY KEY (`Place_Id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Places`
--

LOCK TABLES `Places` WRITE;
/*!40000 ALTER TABLE `Places` DISABLE KEYS */;
INSERT INTO `Places` VALUES (1,'Ticket Office','You are at the ticket office.','The ticket office is near the entrance of the funfair. The ticket vendor is selling tickets. To the south there is exit but you don\'t want to leave just yet. To the north there seems to be some kind of stage.','ticket office',NULL),(2,'Open Air Stage','You are at the open air stage.','There is Elna the clown at the open air stage.','stage',NULL),(3,'Bumper Cars','You are at Bumper Cars.','There is a bumper car opetaror. She seems to be a bit angry to some teens who are all just hitting each other\'s cars.','bumper cars','You ride bumper cars'),(4,'Roller Coaster','You are at the Wormster.','Old man runs the roller coaster very slowly. He seems not to want to talk with you. The roller coaster itself seems smiley though, it looks like a green happy worm. ','roller coaster','You ride wormster'),(5,'Security Station','You are now at the Security Station. ','The security station is a small booth with a red cross on the roof. There is a security officer.','security;security station',NULL),(6,'Carousel','You are now at the Carousel.','There is a carousel operator working. She seems like a nice girl.','carousel','You ride carousel'),(7,'Game Hall','You are now at the Game Hall.','There is a lot of games to choose from. The magician seems to be managing all the games. You see at least Bottle Pyramid and Pull-A-String -games being played.','game hall;games',NULL),(8,'Ferris Wheel','You are at the Ferris Wheel. ','You see an old Ferris Wheel and want to jump in. It seems not to be working though. There is a mechanics working on it but they are too busy to notice you. On the ground there is a ferris wheel operator sitting and looking bored.','ferris wheel',NULL),(9,'Food Court','You are at the Food Court.','To the north there is a Candy Shop, southwest Cafe, southeast Mirror Maze, southwest Rollercoaster, south open air stage and southeast Security Station.\n','food court',NULL),(10,'Mirror Maze','You are at the Mirror Maze.','The mirror maze is full on mirrors. You see some kids making funny faces. Best to leave where you came from, to the southwest where is the food court crossing point.','maze; mirror maze',NULL),(11,'Candy Shop','You are at the Candy Shop.','The candy shop keeper is chewing a licorice. She has big eyeglasses and pink hair. There is a lot of candies and loose licorice around you and a candy floss machine in the corner. ','candy shop',NULL),(12,'Cafe','You are at the Cafe. ','Everything smells so good you almost want to have a cup of coffee. There seems to be good looking cinnamon buns, cookies and brownies on the shelf as well. There is a cafe keeper. He seems happy and old.','cafe',NULL),(13,'Campfire','You are at the campfire behind the Cafe.','You are at the campfire. The cafe keeper yells you from the cafe to come back. The only way out is west back to the cafe.','campfire',NULL);
/*!40000 ALTER TABLE `Places` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Player`
--

DROP TABLE IF EXISTS `Player`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Player` (
  `Player_Id` int(11) NOT NULL,
  `Name` varchar(30) NOT NULL DEFAULT '',
  `Score` int(11) NOT NULL,
  `Place_Id` int(11) NOT NULL,
  PRIMARY KEY (`Player_Id`),
  KEY `Place_Id` (`Place_Id`),
  CONSTRAINT `player_ibfk_1` FOREIGN KEY (`Place_Id`) REFERENCES `Places` (`Place_Id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Player`
--

LOCK TABLES `Player` WRITE;
/*!40000 ALTER TABLE `Player` DISABLE KEYS */;
/*!40000 ALTER TABLE `Player` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping routines for database 'funfair'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-05-04  9:41:33
