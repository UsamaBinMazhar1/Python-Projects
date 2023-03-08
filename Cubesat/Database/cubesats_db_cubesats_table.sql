CREATE DATABASE  IF NOT EXISTS `cubesats_db` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `cubesats_db`;
-- MySQL dump 10.13  Distrib 8.0.27, for Win64 (x86_64)
--
-- Host: localhost    Database: cubesats_db
-- ------------------------------------------------------
-- Server version	8.0.27

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
-- Table structure for table `cubesats_table`
--

DROP TABLE IF EXISTS `cubesats_table`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cubesats_table` (
  `Time_stamp` datetime NOT NULL,
  `ConOps_magic_num_ID` varchar(255) DEFAULT NULL,
  `EPS_I_Battery_Voltage` float DEFAULT NULL,
  `EPS_I_Battery_Current` float DEFAULT NULL,
  `BCR_Voltage` float DEFAULT NULL,
  `BCR_Current` float DEFAULT NULL,
  `SOL_PAN_X_V` float DEFAULT NULL,
  `SOL_PAN_XNCurrent` float DEFAULT NULL,
  `SOL_PAN_XPCurrent` float DEFAULT NULL,
  `SOL_PAN_Y_V` float DEFAULT NULL,
  `SOL_PAN_YNCurrent` float DEFAULT NULL,
  `SOL_PAN_YPCurrent` float DEFAULT NULL,
  `SOL_PAN_Z_V` float DEFAULT NULL,
  `SOL_PAN_ZNCurrent` float DEFAULT NULL,
  `SOL_PAN_ZPCurrent` float DEFAULT NULL,
  `_3V_Bus_Current` float DEFAULT NULL,
  `_5V_Bus_Current` float DEFAULT NULL,
  `MCU_Temperature` float DEFAULT NULL,
  `Battery_Cell_1_Temp` float DEFAULT NULL,
  `Battery_Cell_2_Temp` float DEFAULT NULL,
  `Battery_Cell_3_Temp` float DEFAULT NULL,
  `Battery_Cell_4_Temp` float DEFAULT NULL,
  `Input_Condition` int DEFAULT NULL,
  `Output_Conditions_1` int DEFAULT NULL,
  `Output_Conditions_2` int DEFAULT NULL,
  `Power_ON_Cycle_Counter` int DEFAULT NULL,
  `Under_Voltage_Cond_Counter` int DEFAULT NULL,
  `Short_Circuit_Cond_Counter` int DEFAULT NULL,
  `Over_Temp_Cond_Counter` int DEFAULT NULL,
  `Battpack1_temp_sensor_1_max_temp` float DEFAULT NULL,
  `Battpack1_temp_sensor_1_min_temp` float DEFAULT NULL,
  `Default_Vals_LUPs_and_fastcharge` int DEFAULT NULL,
  `Default_Vals_OUTs_1` int DEFAULT NULL,
  `Battery_Internal_Resistance` float DEFAULT NULL,
  `Battery_Ideal_Voltage` float DEFAULT NULL,
  `UHF_Antenna_Registers` bigint DEFAULT NULL,
  `UHF_Status_Control_Word` int DEFAULT NULL,
  PRIMARY KEY (`Time_stamp`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-04-07 15:10:02
