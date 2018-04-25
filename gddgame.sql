drop database if exists gddpeli;
create database gddpeli;
use gddpeli;


# Dump of table Places
# ------------------------------------------------------------

DROP TABLE IF EXISTS `Places`;

CREATE TABLE `Places` (
  `Place_Id` int(11) NOT NULL,
  `Name` varchar(30) NOT NULL DEFAULT '',
  `Description` text NOT NULL,
  PRIMARY KEY (`Place_Id`)
);

# Dump of table Has_passages
# ------------------------------------------------------------

DROP TABLE IF EXISTS Has_passages;

CREATE TABLE Has_passages (
  Place_Id int NOT NULL,
  Has_passagesPlace_Id int NOT NULL,
  PRIMARY KEY (Place_Id,Has_passagesPlace_Id),
  FOREIGN KEY (Place_Id) REFERENCES Places (Place_Id),
  FOREIGN KEY (Has_passagesPlace_Id) REFERENCES Places (Place_Id)
);



# Dump of table Item_types
# ------------------------------------------------------------

DROP TABLE IF EXISTS `Item_types`;

CREATE TABLE `Item_types` (
  `Itemtype_Id` int(11) NOT NULL,
  `Place_Id` int(11) NOT NULL,
  PRIMARY KEY (`Itemtype_Id`),
  FOREIGN KEY (`Place_Id`) REFERENCES `Places` (`Place_Id`)
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
  FOREIGN KEY (`Place_Id`) REFERENCES `Places` (`Place_Id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


# Dump of table Item_types_Action
# ------------------------------------------------------------

DROP TABLE IF EXISTS `Item_types_Action`;

CREATE TABLE `Item_types_Action` (
  `Action` varchar(11) NOT NULL DEFAULT '',
  `Itemtype_Id` int(11) NOT NULL,
  PRIMARY KEY (`Action`,`Itemtype_Id`),
  FOREIGN KEY (`Itemtype_Id`) REFERENCES `Item_types` (`Itemtype_Id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



# Dump of table Items
# ------------------------------------------------------------

DROP TABLE IF EXISTS Items;

CREATE TABLE Items (
  Item_Id int(11) NOT NULL,
  Itemtype_Id int(11) NOT NULL,
  Player_Id int(11) NOT NULL,
  PRIMARY KEY (Item_Id),
  FOREIGN KEY (Itemtype_Id) REFERENCES Item_types (Itemtype_Id),
  FOREIGN KEY (Player_Id) REFERENCES `Player` (Player_Id)
);


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
  FOREIGN KEY (`Place_Id`) REFERENCES `Places` (`Place_Id`),
  FOREIGN KEY (`Connects_Person_Id`) REFERENCES `Persons` (`Person_Id`)
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
  FOREIGN KEY (`Person_Id`) REFERENCES `Persons` (`Person_Id`),
  FOREIGN KEY (`Place_Id`) REFERENCES `Places` (`Place_Id`),
  FOREIGN KEY (`Item_Id`) REFERENCES `Items` (`Item_Id`),
  FOREIGN KEY (`Connects_Person_Id`) REFERENCES `Persons` (`Connects_Person_Id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

