-- MySQL dump 10.13  Distrib 8.0.30, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: conversiones
-- ------------------------------------------------------
-- Server version	8.0.30

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
-- Table structure for table `tasas_cambio`
--

DROP TABLE IF EXISTS `tasas_cambio`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tasas_cambio` (
  `moneda_origen` varchar(255) NOT NULL,
  `moneda_destino` varchar(255) NOT NULL,
  `tasa_cambio` float NOT NULL,
  PRIMARY KEY (`moneda_origen`,`moneda_destino`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tasas_cambio`
--

LOCK TABLES `tasas_cambio` WRITE;
/*!40000 ALTER TABLE `tasas_cambio` DISABLE KEYS */;
INSERT INTO `tasas_cambio` VALUES ('AUD','CAD',1.09),('AUD','EUR',0.64),('AUD','GBP',0.56),('AUD','JPY',81.15),('AUD','USD',0.75),('CAD','AUD',0.92),('CAD','EUR',0.68),('CAD','GBP',0.58),('CAD','JPY',90.67),('CAD','USD',0.8),('EUR','AUD',1.55),('EUR','CAD',1.47),('EUR','GBP',0.86),('EUR','JPY',131.67),('EUR','USD',1.2),('GBP','AUD',1.77),('GBP','CAD',1.73),('GBP','EUR',1.17),('GBP','JPY',152.4),('GBP','USD',1.39),('JPY','AUD',0.012),('JPY','CAD',0.011),('JPY','EUR',0.0076),('JPY','GBP',0.0066),('JPY','USD',0.009),('MXN','USD',0.049),('USD','AUD',1.33),('USD','CAD',1.25),('USD','EUR',0.83),('USD','GBP',0.72),('USD','JPY',110.5),('USD','MXN',20.5);
/*!40000 ALTER TABLE `tasas_cambio` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-04-02 16:54:36
