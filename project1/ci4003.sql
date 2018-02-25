-- phpMyAdmin SQL Dump
-- version 4.7.7
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Feb 25, 2018 at 05:37 PM
-- Server version: 10.1.30-MariaDB
-- PHP Version: 7.2.2

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `ci4003`
--

-- --------------------------------------------------------

--
-- Table structure for table `currency`
--

CREATE TABLE `currency` (
  `id` int(11) NOT NULL,
  `code` varchar(5) COLLATE utf8_bin NOT NULL,
  `name` varchar(30) COLLATE utf8_bin NOT NULL,
  `currency_type` text COLLATE utf8_bin NOT NULL,
  `enable` varchar(1) COLLATE utf8_bin NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

--
-- Dumping data for table `currency`
--

INSERT INTO `currency` (`id`, `code`, `name`, `currency_type`, `enable`) VALUES
(1, 'USD', 'US Dollar', 'fiat', 'Y'),
(2, 'CAD', 'Canadian Dollar', 'fiat ', 'Y'),
(3, 'EUR', 'Euro', 'fiat', 'Y'),
(4, 'GBP', 'British Pound Sterling', 'fait', 'y'),
(5, 'HKD', 'Hong Kong Dollar', 'fiat', 'Y'),
(6, 'JPY', 'Japanese Yen', 'fiat', 'Y'),
(7, 'SGD', 'Singapore Dollar', 'fiat', 'Y'),
(8, 'THB', 'Thai Baht', 'fiat', 'Y'),
(9, 'CNY', 'Chinese Yuan', 'fiat', 'Y'),
(10, 'BTC', 'Bitcoin', 'Crypto', 'Y'),
(11, 'ETH', 'Ethereum', 'Crypto', 'Y'),
(12, 'LTC', 'Litecoin', 'crypto', 'Y'),
(13, 'BCH', 'Bitcoin Cash / BCC', 'cryoto', 'Y'),
(14, 'XRP', 'Ripple', 'crypto', 'Y');

-- --------------------------------------------------------

--
-- Table structure for table `notebook`
--

CREATE TABLE `notebook` (
  `id` int(11) NOT NULL,
  `test` varchar(11) COLLATE utf8_bin NOT NULL,
  `test1` int(11) NOT NULL,
  `test2` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

--
-- Dumping data for table `notebook`
--

INSERT INTO `notebook` (`id`, `test`, `test1`, `test2`) VALUES
(1, 'บอย', 2, 3),
(2, 'boyx', 1, 1),
(3, 'ปลา', 2, 3),
(3, 'the', 2, 3),
(3, 'the', 2, 3),
(3, 'หมา', 2, 3),
(3, 'หมา', 2, 3),
(3, 'หมา', 2, 3),
(3, 'หมา', 2, 3),
(3, 'ไก่', 2, 3),
(3, 'ไก่', 2, 3),
(3, 'ไก่', 2, 3),
(8, 'thiii', 3, 2),
(36666, 'fsfsf', 3, 3),
(3, 'BNK48', 2, 3);

-- --------------------------------------------------------

--
-- Table structure for table `wallet`
--

CREATE TABLE `wallet` (
  `tansaction_id` int(11) NOT NULL,
  `date` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `currency` varchar(5) COLLATE utf8_bin NOT NULL,
  `amount` float NOT NULL,
  `status` varchar(10) COLLATE utf8_bin NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

--
-- Dumping data for table `wallet`
--

INSERT INTO `wallet` (`tansaction_id`, `date`, `currency`, `amount`, `status`) VALUES
(50, '2018-02-25 10:24:57', 'USD', 500, 'deposit'),
(51, '2018-02-25 10:25:15', 'USD', 600, 'deposit'),
(52, '2018-02-25 10:26:55', 'LTC', 33, 'deposit'),
(53, '2018-02-25 10:27:08', 'XRP', 500, 'deposit'),
(54, '2018-02-25 10:28:23', 'ETH', 200, 'deposit'),
(55, '2018-02-25 10:51:58', 'CNY', 500, 'deposit'),
(56, '2018-02-25 10:56:47', 'BTC', 500, 'deposit'),
(57, '2018-02-25 10:58:15', 'BTC', 600, 'deposit'),
(58, '2018-02-25 10:59:49', 'BTC', 200, 'deposit'),
(59, '2018-02-25 11:11:01', 'BTC', -600, 'withdraw'),
(60, '2018-02-25 11:12:50', 'BTC', -500, 'withdraw'),
(62, '2018-02-25 11:26:04', 'USD', -12, 'withdraw'),
(63, '2018-02-25 11:29:23', 'USD', -0, 'withdraw'),
(64, '2018-02-25 11:29:47', 'USD', -109, 'withdraw'),
(65, '2018-02-25 11:30:12', 'USD', -979, 'withdraw'),
(66, '2018-02-25 11:36:40', 'EUR', 900, 'deposit'),
(67, '2018-02-25 11:37:16', 'EUR', -600, 'withdraw'),
(68, '2018-02-25 11:46:20', 'EUR', -100, 'withdraw'),
(69, '2018-02-25 11:49:45', 'LTC', -5, 'withdraw'),
(70, '2018-02-25 11:50:47', 'LTC', -2, 'withdraw'),
(71, '2018-02-25 11:52:01', 'USD', 9000, 'deposit'),
(72, '2018-02-25 11:52:19', 'USD', -500, 'withdraw'),
(73, '2018-02-25 11:55:17', 'USD', -60, 'withdraw'),
(74, '2018-02-25 11:55:58', 'LTC', -4, 'withdraw'),
(75, '2018-02-25 11:59:15', 'BTC', -20, 'withdraw'),
(76, '2018-02-25 12:00:03', 'BTC', 0.5, 'deposit'),
(77, '2018-02-25 12:00:21', 'BTC', -1, 'withdraw'),
(78, '2018-02-25 12:01:10', 'BTC', -1, 'withdraw'),
(79, '2018-02-25 13:00:01', 'BTC', -20, 'withdraw'),
(80, '2018-02-25 13:02:05', 'BTC', -1, 'withdraw'),
(81, '2018-02-25 13:03:26', 'ETH', 100, 'deposit'),
(82, '2018-02-25 13:03:40', 'ETH', -100, 'withdraw'),
(83, '2018-02-25 13:05:13', 'XRP', -100, 'withdraw'),
(84, '2018-02-25 13:08:33', 'USD', -66, 'withdraw'),
(85, '2018-02-25 13:10:18', 'USD', -500, 'withdraw'),
(86, '2018-02-25 13:12:01', 'XRP', -1, 'withdraw'),
(87, '2018-02-25 13:13:28', 'XRP', -3, 'withdraw'),
(88, '2018-02-25 13:37:15', 'LTC', -1, 'withdraw'),
(89, '2018-02-25 13:38:04', 'USD', -200, 'withdraw'),
(90, '2018-02-25 13:39:01', 'BTC', -1, 'withdraw'),
(91, '2018-02-25 13:39:31', 'BTC', -2, 'withdraw'),
(92, '2018-02-25 13:43:25', 'USD', -2, 'withdraw'),
(93, '2018-02-25 13:47:12', 'USD', -3, 'withdraw'),
(94, '2018-02-25 13:47:48', 'BTC', -2, 'withdraw'),
(95, '2018-02-25 15:06:33', 'USD', -3, 'withdraw'),
(96, '2018-02-25 15:07:43', 'ETH', 200, 'deposit'),
(97, '2018-02-25 15:08:24', 'ETH', -200, 'withdraw'),
(98, '2018-02-25 15:09:44', 'XRP', -30, 'withdraw'),
(99, '2018-02-25 15:11:04', 'CAD', 600, 'deposit'),
(100, '2018-02-25 15:11:29', 'CAD', -30, 'withdraw'),
(101, '2018-02-25 16:00:38', 'HKD', 500, 'deposit'),
(102, '2018-02-25 16:00:59', 'HKD', -100, 'withdraw'),
(103, '2018-02-25 16:28:11', 'JPY', 600, 'deposit'),
(104, '2018-02-25 16:35:29', 'BTC', -1, 'withdraw');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `currency`
--
ALTER TABLE `currency`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `wallet`
--
ALTER TABLE `wallet`
  ADD PRIMARY KEY (`tansaction_id`),
  ADD KEY `tansaction_id` (`tansaction_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `currency`
--
ALTER TABLE `currency`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;

--
-- AUTO_INCREMENT for table `wallet`
--
ALTER TABLE `wallet`
  MODIFY `tansaction_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=105;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
