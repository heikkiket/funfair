# ************************************************************
# Sequel Pro SQL dump
# Version 4541
#
# http://www.sequelpro.com/
# https://github.com/sequelpro/sequelpro
#
# Host: 127.0.0.1 (MySQL 5.7.21)
# Database: gddpeli
# Generation Time: 2018-04-25 17:28:27 +0000
# ************************************************************


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


# Dump of table Directions
# ------------------------------------------------------------

DROP TABLE IF EXISTS `Directions`;

CREATE TABLE `Directions` (
  `Direction_Id` varchar(10) NOT NULL DEFAULT '',
  `Description` varchar(20) NOT NULL DEFAULT '',
  PRIMARY KEY (`Direction_Id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

LOCK TABLES `Directions` WRITE;
/*!40000 ALTER TABLE `Directions` DISABLE KEYS */;

INSERT INTO `Directions` (`Direction_Id`, `Description`)
VALUES
	('e','East'),
	('n','North'),
	('ne','Northeast'),
	('nw','Northwest'),
	('s','South'),
	('se','Southeast'),
	('sw','Southwest'),
	('w','West');

/*!40000 ALTER TABLE `Directions` ENABLE KEYS */;
UNLOCK TABLES;


# Dump of table Has_passages
# ------------------------------------------------------------

DROP TABLE IF EXISTS `Has_passages`;

CREATE TABLE `Has_passages` (
  `Place_Id` int(11) NOT NULL,
  `Has_passagesPlace_Id` int(11) NOT NULL,
  `Direction_Id` varchar(10) NOT NULL DEFAULT '',
  PRIMARY KEY (`Place_Id`,`Has_passagesPlace_Id`),
  KEY `Has_passagesPlace_Id` (`Has_passagesPlace_Id`),
  CONSTRAINT `has_passages_ibfk_1` FOREIGN KEY (`Place_Id`) REFERENCES `Places` (`Place_Id`),
  CONSTRAINT `has_passages_ibfk_2` FOREIGN KEY (`Has_passagesPlace_Id`) REFERENCES `Places` (`Place_Id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

LOCK TABLES `Has_passages` WRITE;
/*!40000 ALTER TABLE `Has_passages` DISABLE KEYS */;

INSERT INTO `Has_passages` (`Place_Id`, `Has_passagesPlace_Id`, `Direction_Id`)
VALUES
	(1,2,'n'),
	(2,3,'w'),
	(2,5,'sw'),
	(2,7,'se'),
	(2,9,'n'),
	(3,2,'e'),
	(3,4,'n'),
	(4,3,'s'),
	(4,9,'ne'),
	(5,2,'sw'),
	(5,6,'se'),
	(5,8,'e'),
	(5,9,'nw'),
	(6,5,'nw'),
	(6,7,'s'),
	(6,8,'n'),
	(7,2,'nw'),
	(7,6,'n'),
	(8,5,'w'),
	(8,6,'s'),
	(9,2,'s'),
	(9,4,'sw'),
	(9,5,'se'),
	(9,10,'ne'),
	(9,11,'n'),
	(9,12,'nw'),
	(10,9,'sw'),
	(11,9,'sw'),
	(11,12,'w'),
	(12,9,'se'),
	(12,11,'e'),
	(12,13,'e'),
	(13,12,'w');

/*!40000 ALTER TABLE `Has_passages` ENABLE KEYS */;
UNLOCK TABLES;


# Dump of table Item_types
# ------------------------------------------------------------

DROP TABLE IF EXISTS `Item_types`;

CREATE TABLE `Item_types` (
  `Itemtype_Id` int(11) NOT NULL,
  `Name` varchar(40) NOT NULL,
  `Place_Id` int(11) NOT NULL,
  PRIMARY KEY (`Itemtype_Id`),
  KEY `Place_Id` (`Place_Id`),
  CONSTRAINT `item_types_ibfk_1` FOREIGN KEY (`Place_Id`) REFERENCES `Places` (`Place_Id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

LOCK TABLES `Item_types` WRITE;
/*!40000 ALTER TABLE `Item_types` DISABLE KEYS */;

INSERT INTO `Item_types` (`Itemtype_Id`, `Name`, `Place_Id`)
VALUES
	(1,'Ride Tickets',1),
	(2,'Game Prizes',7),
	(3,'Drinks from Cafe',12),
	(4,'Foods from Cafe',12),
	(5,'Candies',11);

/*!40000 ALTER TABLE `Item_types` ENABLE KEYS */;
UNLOCK TABLES;


# Dump of table Item_types_Action
# ------------------------------------------------------------

DROP TABLE IF EXISTS `Item_types_Action`;

CREATE TABLE `Item_types_Action` (
  `Action` varchar(11) NOT NULL DEFAULT '',
  `Itemtype_Id` int(11) NOT NULL,
  PRIMARY KEY (`Action`,`Itemtype_Id`),
  KEY `Itemtype_Id` (`Itemtype_Id`),
  CONSTRAINT `item_types_action_ibfk_1` FOREIGN KEY (`Itemtype_Id`) REFERENCES `Item_types` (`Itemtype_Id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

LOCK TABLES `Item_types_Action` WRITE;
/*!40000 ALTER TABLE `Item_types_Action` DISABLE KEYS */;

INSERT INTO `Item_types_Action` (`Action`, `Itemtype_Id`)
VALUES
	('Buy',1),
	('Eat',1),
	('Buy',3),
	('Drink',3),
	('Buy',4),
	('Eat',4),
	('Buy',5),
	('Eat',5);

/*!40000 ALTER TABLE `Item_types_Action` ENABLE KEYS */;
UNLOCK TABLES;


# Dump of table Items
# ------------------------------------------------------------

DROP TABLE IF EXISTS `Items`;

CREATE TABLE `Items` (
  `Item_Id` int(11) NOT NULL,
  `Name` varchar(40) DEFAULT NULL,
  `Itemtype_Id` int(11) NOT NULL,
  `Player_Id` int(11) DEFAULT NULL,
  PRIMARY KEY (`Item_Id`),
  KEY `Itemtype_Id` (`Itemtype_Id`),
  KEY `Player_Id` (`Player_Id`),
  CONSTRAINT `items_ibfk_1` FOREIGN KEY (`Itemtype_Id`) REFERENCES `Item_types` (`Itemtype_Id`),
  CONSTRAINT `items_ibfk_2` FOREIGN KEY (`Player_Id`) REFERENCES `Player` (`Player_Id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

LOCK TABLES `Items` WRITE;
/*!40000 ALTER TABLE `Items` DISABLE KEYS */;

INSERT INTO `Items` (`Item_Id`, `Name`, `Itemtype_Id`, `Player_Id`)
VALUES
	(1,'Ride tickets',1,NULL),
	(2,'Stuffed Teddy Bear',2,NULL),
	(3,'Blue pencil',2,NULL),
	(4,'Funfair themed playing cards',2,NULL),
	(5,'Cup of coffee',3,NULL),
	(6,'Cup of tea',3,NULL),
	(7,'Can of soda',3,NULL),
	(8,'Bottle of water',3,NULL),
	(9,'Cinnamon bun',4,NULL),
	(10,'Cookie',4,NULL),
	(11,'Chocolate brownie',4,NULL),
	(12,'Pink candy floss',5,NULL),
	(13,'Candies',5,NULL),
	(14,'Licorice',5,NULL);

/*!40000 ALTER TABLE `Items` ENABLE KEYS */;
UNLOCK TABLES;


# Dump of table Line
# ------------------------------------------------------------

DROP TABLE IF EXISTS `Line`;

CREATE TABLE `Line` (
  `Lines_Id` int(11) NOT NULL,
  `Line_Text` text NOT NULL,
  `Person_Id` int(11) NOT NULL,
  `Place_Id` int(11) NOT NULL,
  `Item_Id` int(11) DEFAULT NULL,
  `Connects_Person_Id` int(11) DEFAULT NULL,
  PRIMARY KEY (`Lines_Id`),
  KEY `Person_Id` (`Person_Id`),
  KEY `Place_Id` (`Place_Id`),
  KEY `Item_Id` (`Item_Id`),
  KEY `Connects_Person_Id` (`Connects_Person_Id`),
  CONSTRAINT `line_ibfk_1` FOREIGN KEY (`Person_Id`) REFERENCES `Persons` (`Person_Id`),
  CONSTRAINT `line_ibfk_2` FOREIGN KEY (`Place_Id`) REFERENCES `Places` (`Place_Id`),
  CONSTRAINT `line_ibfk_3` FOREIGN KEY (`Item_Id`) REFERENCES `Items` (`Item_Id`),
  CONSTRAINT `line_ibfk_4` FOREIGN KEY (`Connects_Person_Id`) REFERENCES `Persons` (`Connects_Person_Id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

LOCK TABLES `Line` WRITE;
/*!40000 ALTER TABLE `Line` DISABLE KEYS */;

INSERT INTO `Line` (`Lines_Id`, `Line_Text`, `Person_Id`, `Place_Id`, `Item_Id`, `Connects_Person_Id`)
VALUES
	(1,'There is bad blood around in our funfair. Walk around to find out!',8,1,NULL,NULL),
	(2,'You want to buy ride tickets? Okey, here you go.',8,1,1,NULL),
	(3,'Would you have guessed the clown is my mother? It feels like I\'ve live my whole life here. Sometimes I wonder about the meaning of life. I study philosophy.',8,1,NULL,NULL),
	(4,'I’m not sure, but I think candy shop keeper and security officer don’t get along very well.',1,2,NULL,NULL),
	(5,'I think carousel keeper and Elna don’t get along very well.',5,6,NULL,NULL),
	(6,'It’s such a nice day today. I think the kids will have a blast when I perform later. The janitor roasted some marshmallows last night.',1,2,NULL,NULL);

/*!40000 ALTER TABLE `Line` ENABLE KEYS */;
UNLOCK TABLES;


# Dump of table Persons
# ------------------------------------------------------------

DROP TABLE IF EXISTS `Persons`;

CREATE TABLE `Persons` (
  `Person_Id` int(11) NOT NULL,
  `Name` varchar(30) NOT NULL DEFAULT '',
  `Connectable` int(11) DEFAULT NULL,
  `Place_Id` int(11) NOT NULL,
  `Connects_Person_Id` int(11) DEFAULT NULL,
  PRIMARY KEY (`Person_Id`),
  KEY `Place_Id` (`Place_Id`),
  KEY `Connects_Person_Id` (`Connects_Person_Id`),
  CONSTRAINT `persons_ibfk_1` FOREIGN KEY (`Place_Id`) REFERENCES `Places` (`Place_Id`),
  CONSTRAINT `persons_ibfk_2` FOREIGN KEY (`Connects_Person_Id`) REFERENCES `Persons` (`Person_Id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

LOCK TABLES `Persons` WRITE;
/*!40000 ALTER TABLE `Persons` DISABLE KEYS */;

INSERT INTO `Persons` (`Person_Id`, `Name`, `Connectable`, `Place_Id`, `Connects_Person_Id`)
VALUES
	(1,'Elna the Clown',1,2,NULL),
	(2,'The Magician',1,7,NULL),
	(3,'Security Officer',1,5,NULL),
	(4,'Bumper Car Operator',1,3,NULL),
	(5,'Carousel Operator',1,5,NULL),
	(6,'Cafe Keeper',1,12,NULL),
	(7,'Candy Shop Keeper',1,11,NULL),
	(8,'Ticket Vendor',NULL,1,NULL),
	(9,'Funfair Director',NULL,13,NULL),
	(10,'Ferris Wheel Operator',NULL,8,NULL);

/*!40000 ALTER TABLE `Persons` ENABLE KEYS */;
UNLOCK TABLES;


# Dump of table Places
# ------------------------------------------------------------

DROP TABLE IF EXISTS `Places`;

CREATE TABLE `Places` (
  `Place_Id` int(11) NOT NULL,
  `Name` varchar(30) NOT NULL DEFAULT '',
  `Description` text NOT NULL,
  `Details` text,
  PRIMARY KEY (`Place_Id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

LOCK TABLES `Places` WRITE;
/*!40000 ALTER TABLE `Places` DISABLE KEYS */;

INSERT INTO `Places` (`Place_Id`, `Name`, `Description`, `Details`)
VALUES
	(1,'Ticket Office','You are at the ticket office.','The ticket office is near the entrance of the funfair. The ticket vendor is selling tickets. To the south there is exit but you don\'t want to leave just yet. To the north there seems to be some kind of stage.'),
	(2,'Open Air Stage','You are at the open air stage.','There is Elna the clown at the open air stage.'),
	(3,'Bumper Cars','You are at Bumper Cars.','There is a bumper car opetaror. She seems to be a bit angry to some teens who are all just hitting each other\'s cars.'),
	(4,'Roller Coaster','You are at the Wormster.','Old man runs the roller coaster very slowly. He seems not to want to talk with you. The roller coaster itself seems smiley though, it looks like a green happy worm. '),
	(5,'Security Station','You are now at the Security Station. ','The security station is a small booth with a red cross on the roof. There is a security officer.'),
	(6,'Carousel','You are now at the Carousel.','There is a carousel operator working. She seems like a nice girl.'),
	(7,'Game Hall','You are now at the Game Hall.','There is a lot of games to choose from. The magician seems to be managing all the games. You see at least Bottle Pyramid and Pull-A-String -games being played.'),
	(8,'Ferris Wheel','You are at the Ferris Wheel. ','You see an old Ferris Wheel and want to jump in. It seems not to be working though. There is a mechanics working on it but they are too busy to notice you. On the ground there is a ferris wheel operator sitting and looking bored.'),
	(9,'Ticket Office','You are at the Food Court.','To the north there is a Candy Shop, southwest Cafe, southeast Mirror Maze, southwest Rollercoaster, south open air stage and southeast Security Station.\n'),
	(10,'Mirror Maze','You are at the Mirror Maze.','The mirror maze is full on mirrors. You see some kids making funny faces. Best to leave where you came from, to the southwest where is the food court crossing point.'),
	(11,'Candy Shop','You are at the Candy Shop.','The candy shop keeper is chewing a licorice. She has big eyeglasses and pink hair. There is a lot of candies and loose licorice around you and a candy floss machine in the corner. '),
	(12,'Cafe','You are at the Cafe. ','Everything smells so good you almost want to have a cup of coffee. There seems to be good looking cinnamon buns, cookies and brownies on the shelf as well. There is a cafe keeper. He seems happy and old.'),
	(13,'Campfire','You are at the campfire behind the Cafe.','You are at the campfire. The cafe keeper yells you from the cafe to come back. The only way out is west back to the cafe.');

/*!40000 ALTER TABLE `Places` ENABLE KEYS */;
UNLOCK TABLES;


# Dump of table Player
# ------------------------------------------------------------

DROP TABLE IF EXISTS `Player`;

CREATE TABLE `Player` (
  `Player_Id` int(11) NOT NULL,
  `Name` varchar(30) NOT NULL DEFAULT '',
  `Score` int(11) NOT NULL,
  `Place_Id` int(11) NOT NULL,
  PRIMARY KEY (`Player_Id`),
  KEY `Place_Id` (`Place_Id`),
  CONSTRAINT `player_ibfk_1` FOREIGN KEY (`Place_Id`) REFERENCES `Places` (`Place_Id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;




/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
