-- MySQL dump 10.13  Distrib 8.0.19, for Win64 (x86_64)
--
-- Host: localhost    Database: wcontrol
-- ------------------------------------------------------
-- Server version	8.0.19

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `admin`
--

DROP TABLE IF EXISTS `admin`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `admin` (
  `idAdmin` int NOT NULL AUTO_INCREMENT,
  `login` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  PRIMARY KEY (`idAdmin`),
  UNIQUE KEY `idAdmin_UNIQUE` (`idAdmin`)
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `admin`
--

LOCK TABLES `admin` WRITE;
/*!40000 ALTER TABLE `admin` DISABLE KEYS */;
INSERT INTO `admin` VALUES (2,'admin22','admin2'),(3,'admin','admin'),(21,'SPWPMBB98H','I2KDX7');
/*!40000 ALTER TABLE `admin` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `workday`
--

DROP TABLE IF EXISTS `workday`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `workday` (
  `idWorkDay` int NOT NULL AUTO_INCREMENT,
  `idUser` int NOT NULL,
  `idAdmin` int NOT NULL,
  `aDate` date NOT NULL,
  `sumHours` float NOT NULL,
  `dayPay` float NOT NULL,
  PRIMARY KEY (`idWorkDay`),
  UNIQUE KEY `idWorkDay_UNIQUE` (`idWorkDay`),
  KEY `admId_idx` (`idAdmin`),
  KEY `usId_idx` (`idUser`),
  CONSTRAINT `admId` FOREIGN KEY (`idAdmin`) REFERENCES `admin` (`idAdmin`) ON UPDATE CASCADE,
  CONSTRAINT `usId` FOREIGN KEY (`idUser`) REFERENCES `worker` (`idUser`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `workday`
--

LOCK TABLES `workday` WRITE;
/*!40000 ALTER TABLE `workday` DISABLE KEYS */;
INSERT INTO `workday` VALUES (8,1,2,'2017-11-11',2,38),(12,1,3,'2017-11-12',2,22),(13,1,3,'2018-11-10',8,249.9),(14,1,3,'2016-03-11',3,63),(15,1,3,'2018-11-11',9,298.2),(17,1,3,'2020-11-11',8,249.9),(18,1,3,'2017-09-10',2,42),(20,1,3,'2020-04-03',7,201.6);
/*!40000 ALTER TABLE `workday` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `worker`
--

DROP TABLE IF EXISTS `worker`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `worker` (
  `idUser` int NOT NULL AUTO_INCREMENT,
  `name` varchar(45) NOT NULL,
  `sName` varchar(45) NOT NULL,
  `dateB` date NOT NULL,
  `hourPay` int NOT NULL,
  `dayHours` float NOT NULL,
  `email` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  PRIMARY KEY (`idUser`),
  UNIQUE KEY `idUser_UNIQUE` (`idUser`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `worker`
--

LOCK TABLES `worker` WRITE;
/*!40000 ALTER TABLE `worker` DISABLE KEYS */;
INSERT INTO `worker` VALUES (1,'Alex','Row','1967-03-04',21,5,'user@gmail.com','user'),(5,'Marta','Din','1996-12-12',19,4,'mdin@gmail.com','user'),(6,'Klara','Kross','1987-12-12',17,4,'kak@gmail.com','123'),(9,'Dana','Lu','1989-03-04',23,8,'dluna@gmail.com','123'),(14,'Mina','Fill','1998-04-11',20,7,'mif@gmail.com','123'),(15,'Maik','Krill','1989-12-12',20,6,'maikk@gmail.com','123'),(18,'Maria','Kolos','1987-10-05',23,9,'mk@gmail.com','123');
/*!40000 ALTER TABLE `worker` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping events for database 'wcontrol'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-01-27  0:43:54
