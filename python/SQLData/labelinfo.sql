# SQL-Front 5.1  (Build 4.16)

/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE */;
/*!40101 SET SQL_MODE='STRICT_TRANS_TABLES,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES */;
/*!40103 SET SQL_NOTES='ON' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS */;
/*!40014 SET FOREIGN_KEY_CHECKS=0 */;


# Host: 127.0.0.1    Database: labels
# ------------------------------------------------------
# Server version 5.0.67-community-nt

DROP DATABASE IF EXISTS `labels`;
CREATE DATABASE `labels` /*!40100 DEFAULT CHARACTER SET utf8 */;
USE `labels`;

#
# Source for table labelinfo
#

DROP TABLE IF EXISTS `labelinfo`;
CREATE TABLE `labelinfo` (
  `Id` int(11) NOT NULL auto_increment,
  `SN` varchar(16) NOT NULL default '',
  `YZM` varchar(16) NOT NULL default '',
  `DT` varchar(16) NOT NULL default '',
  `PT` varchar(16) NOT NULL default '',
  PRIMARY KEY  (`Id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

#
# Dumping data for table labelinfo
#

LOCK TABLES `labelinfo` WRITE;
/*!40000 ALTER TABLE `labelinfo` DISABLE KEYS */;
/*!40000 ALTER TABLE `labelinfo` ENABLE KEYS */;
UNLOCK TABLES;

/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
