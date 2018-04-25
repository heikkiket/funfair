# ************************************************************
# Sequel Pro SQL dump
# Version 4541
#
# http://www.sequelpro.com/
# https://github.com/sequelpro/sequelpro
#
# Host: 127.0.0.1 (MySQL 5.5.5-10.2.13-MariaDB)
# Database: gddgame
# Generation Time: 2018-04-25 10:54:03 +0000
# ************************************************************


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


# Dump of table Has_passages
# ------------------------------------------------------------

DROP TABLE IF EXISTS `Has_passages`;

CREATE TABLE `Has_passages` (
  `Place_Id` int(11) NOT NULL,
  `Has_passagesPlace_Id` int(11) NOT NULL,
  PRIMARY KEY (`Place_Id`,`Has_passagesPlace_Id`),
  KEY `Has_passagesPlace_Id_2` (`Has_passagesPlace_Id`),
  CONSTRAINT `has_passages_ibfk_1` FOREIGN KEY (`Place_Id`) REFERENCES `testgame`.`Places` (`Place_Id`),
  CONSTRAINT `has_passages_ibfk_2` FOREIGN KEY (`Has_passagesPlace_Id`) REFERENCES `testgame`.`Places` (`Place_Id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



# Dump of table Item_types
# ------------------------------------------------------------

DROP TABLE IF EXISTS `Item_types`;

CREATE TABLE `Item_types` (
  `Itemtype_Id` int(11) NOT NULL,
  `Place_Id` int(11) NOT NULL,
  PRIMARY KEY (`Itemtype_Id`),
  KEY `Place_Id` (`Place_Id`),
  CONSTRAINT `item_types_ibfk_1` FOREIGN KEY (`Place_Id`) REFERENCES `testgame`.`Places` (`Place_Id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



# Dump of table Item_types_Action
# ------------------------------------------------------------

DROP TABLE IF EXISTS `Item_types_Action`;

CREATE TABLE `Item_types_Action` (
  `Action` varchar(11) NOT NULL DEFAULT '',
  `Itemtype_Id` int(11) NOT NULL,
  PRIMARY KEY (`Action`,`Itemtype_Id`),
  KEY `Itemtype_Id` (`Itemtype_Id`),
  CONSTRAINT `item_types_action_ibfk_1` FOREIGN KEY (`Itemtype_Id`) REFERENCES `testgame`.`Item_types` (`Itemtype_Id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



# Dump of table Items
# ------------------------------------------------------------

DROP TABLE IF EXISTS `Items`;

CREATE TABLE `Items` (
  `Item_Id` int(11) NOT NULL,
  `Itemtype_Id` int(11) NOT NULL,
  `Player_Id` int(11) NOT NULL,
  PRIMARY KEY (`Item_Id`),
  KEY `Itemtype_Id` (`Itemtype_Id`),
  KEY `Player_Id` (`Player_Id`),
  CONSTRAINT `items_ibfk_1` FOREIGN KEY (`Itemtype_Id`) REFERENCES `testgame`.`Item_types` (`Itemtype_Id`),
  CONSTRAINT `items_ibfk_2` FOREIGN KEY (`Player_Id`) REFERENCES `testgame`.`Player` (`Player_Id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



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
  CONSTRAINT `line_ibfk_1` FOREIGN KEY (`Person_Id`) REFERENCES `testgame`.`Persons` (`Person_Id`),
  CONSTRAINT `line_ibfk_2` FOREIGN KEY (`Place_Id`) REFERENCES `testgame`.`Places` (`Place_Id`),
  CONSTRAINT `line_ibfk_3` FOREIGN KEY (`Item_Id`) REFERENCES `testgame`.`Items` (`Item_Id`),
  CONSTRAINT `line_ibfk_4` FOREIGN KEY (`Connects_Person_Id`) REFERENCES `testgame`.`Persons` (`Connects_Person_Id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



# Dump of table Persons
# ------------------------------------------------------------

DROP TABLE IF EXISTS `Persons`;

CREATE TABLE `Persons` (
  `Person_Id` int(11) NOT NULL,
  `Name` varchar(30) NOT NULL DEFAULT '',
  `Connectable` int(11) NOT NULL,
  `Place_Id` int(11) NOT NULL,
  `Connects_Person_Id` int(11) DEFAULT NULL,
  PRIMARY KEY (`Person_Id`),
  KEY `Place_Id` (`Place_Id`),
  KEY `Connects_Person_Id` (`Connects_Person_Id`),
  CONSTRAINT `persons_ibfk_1` FOREIGN KEY (`Place_Id`) REFERENCES `testgame`.`Places` (`Place_Id`),
  CONSTRAINT `persons_ibfk_2` FOREIGN KEY (`Connects_Person_Id`) REFERENCES `testgame`.`Persons` (`Person_Id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



# Dump of table Places
# ------------------------------------------------------------

DROP TABLE IF EXISTS `Places`;

CREATE TABLE `Places` (
  `Place_Id` int(11) NOT NULL,
  `Name` varchar(30) NOT NULL DEFAULT '',
  `Description` text NOT NULL,
  PRIMARY KEY (`Place_Id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



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
  CONSTRAINT `player_ibfk_1` FOREIGN KEY (`Place_Id`) REFERENCES `testgame`.`Places` (`Place_Id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;




/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
