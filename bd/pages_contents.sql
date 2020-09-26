-- phpMyAdmin SQL Dump
-- version 4.7.1
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Sep 26, 2020 at 08:50 AM
-- Server version: 5.6.36
-- PHP Version: 5.6.31

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `pages_contents`
--

-- --------------------------------------------------------

--
-- Table structure for table `saves`
--

CREATE TABLE `saves` (
  `cle` varchar(16) NOT NULL,
  `valeur` mediumtext NOT NULL,
  `can_save` int(11) NOT NULL DEFAULT '1',
  `host_addr` varchar(32) NOT NULL,
  `creation_date` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `user_name` varchar(128) NOT NULL,
  `update_date` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `visible` tinyint(1) NOT NULL DEFAULT '1'
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `saves`
--

INSERT INTO `saves` (`cle`, `valeur`, `can_save`, `host_addr`, `creation_date`, `user_name`, `update_date`, `visible`) VALUES
('2DvCampICL', 'Hello', 1, '127.0.0.1', '2020-09-26 16:41:26', 'MAM1', '2020-09-26 16:41:26', 1),
('b1cZaWLl0e', 'Hello', 0, '127.0.0.1', '2020-09-26 16:15:43', 'Mohamed Anis MANI', '2020-09-26 16:15:43', 1),
('HerXva8vOV', 'Hello', 1, '127.0.0.1', '2020-09-26 08:38:14', 'MAM', '2020-09-26 08:38:14', 1);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `saves`
--
ALTER TABLE `saves`
  ADD PRIMARY KEY (`cle`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
