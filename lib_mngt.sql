-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jul 19, 2023 at 10:19 AM
-- Server version: 10.4.27-MariaDB
-- PHP Version: 8.2.0

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `lib_mngt`
--

-- --------------------------------------------------------

--
-- Table structure for table `book`
--

CREATE TABLE `book` (
  `id` int(10) NOT NULL,
  `book_name` varchar(30) NOT NULL,
  `status` int(2) DEFAULT 1,
  `isActive` int(11) NOT NULL,
  `added_by` varchar(25) DEFAULT 'admin',
  `updated_at` timestamp NULL DEFAULT current_timestamp(),
  `created_at` timestamp NULL DEFAULT current_timestamp(),
  `category` varchar(50) NOT NULL,
  `author` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

--
-- Dumping data for table `book`
--

INSERT INTO `book` (`id`, `book_name`, `status`, `isActive`, `added_by`, `updated_at`, `created_at`, `category`, `author`) VALUES
(1, 'Rich Dad Poor Dad', 1, 1, 'admin', '2023-07-14 08:02:47', '2023-07-14 08:02:47', 'Education', ''),
(2, 'fssf', 1, 1, 'admin', '2023-07-19 07:59:10', '2023-07-19 07:59:10', 'Entrepreneur', 'test'),
(3, 'tsed', 1, 1, 'admin', '2023-07-19 07:59:45', '2023-07-19 07:59:45', 'Comic', 'test'),
(4, 'tsed', 1, 1, 'admin', '2023-07-19 08:02:54', '2023-07-19 08:02:54', 'Education', 'test'),
(5, 'tsed', 1, 0, 'admin', '2023-07-19 08:03:27', '2023-07-19 08:03:27', 'Education', 'test'),
(6, 'tsed', 1, 0, 'admin', '2023-07-19 08:03:32', '2023-07-19 08:03:32', 'Education', 'test'),
(7, 'tsed', 1, 1, 'admin', '2023-07-19 08:04:34', '2023-07-19 08:04:34', 'Biography', 'test'),
(8, 'dfsfs', 1, 1, 'admin', '2023-07-19 08:10:09', '2023-07-19 08:10:09', 'Entrepreneur', '54545');

-- --------------------------------------------------------

--
-- Table structure for table `book_log`
--

CREATE TABLE `book_log` (
  `id` int(3) NOT NULL,
  `book_id` int(5) NOT NULL,
  `user_id` int(5) NOT NULL,
  `status` int(3) DEFAULT NULL,
  `remark` varchar(255) DEFAULT NULL,
  `return_date` timestamp NULL DEFAULT NULL ON UPDATE current_timestamp(),
  `updated_at` timestamp NOT NULL DEFAULT current_timestamp(),
  `created_at` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

--
-- Dumping data for table `book_log`
--

INSERT INTO `book_log` (`id`, `book_id`, `user_id`, `status`, `remark`, `return_date`, `updated_at`, `created_at`) VALUES
(1, 1, 1, 0, NULL, '2023-07-14 05:09:50', '2023-07-13 12:55:11', '2023-07-13 12:55:11'),
(2, 1, 1, 0, '', '2023-07-14 06:15:02', '2023-07-14 06:14:00', '2023-07-14 06:14:00'),
(3, 1, 3, 0, '', '2023-07-14 07:08:50', '2023-07-14 07:08:36', '2023-07-14 07:08:36'),
(4, 1, 3, 0, '', '2023-07-14 07:11:36', '2023-07-14 07:09:05', '2023-07-14 07:09:05'),
(5, 1, 3, 0, '', '2023-07-14 07:11:38', '2023-07-14 07:11:25', '2023-07-14 07:11:25'),
(6, 1, 3, 0, '', '2023-07-14 07:13:09', '2023-07-14 07:11:51', '2023-07-14 07:11:51'),
(7, 1, 3, 0, '', '2023-07-14 07:13:24', '2023-07-14 07:13:17', '2023-07-14 07:13:17'),
(8, 1, 3, 0, '', '2023-07-14 07:13:39', '2023-07-14 07:13:31', '2023-07-14 07:13:31'),
(9, 1, 3, 0, '', '2023-07-14 07:14:03', '2023-07-14 07:13:57', '2023-07-14 07:13:57'),
(10, 1, 3, 0, '', '2023-07-14 07:15:20', '2023-07-14 07:15:13', '2023-07-14 07:15:13'),
(11, 1, 1, 0, '', '2023-07-14 07:19:53', '2023-07-14 07:19:48', '2023-07-14 07:19:48'),
(12, 1, 3, 0, '', '2023-07-14 07:34:38', '2023-07-14 07:34:29', '2023-07-14 07:34:29'),
(13, 1, 1, 0, '', '2023-07-14 07:35:55', '2023-07-14 07:35:53', '2023-07-14 07:35:53'),
(14, 1, 1, 0, '', '2023-07-14 11:43:35', '2023-07-14 11:43:31', '2023-07-14 11:43:31'),
(15, 1, 1, 0, '', '2023-07-14 11:47:26', '2023-07-14 11:47:12', '2023-07-14 11:47:12'),
(16, 1, 3, 0, '', '2023-07-14 11:50:00', '2023-07-14 11:49:30', '2023-07-14 11:49:30'),
(17, 1, 4, 0, '', '2023-07-19 06:28:02', '2023-07-19 06:27:59', '2023-07-19 06:27:59'),
(18, 1, 4, 0, '', '2023-07-19 06:28:19', '2023-07-19 06:28:13', '2023-07-19 06:28:13'),
(19, 4, 4, 0, '', '2023-07-19 08:06:49', '2023-07-19 08:05:30', '2023-07-19 08:05:30'),
(20, 2, 4, 0, '', '2023-07-19 08:06:49', '2023-07-19 08:05:35', '2023-07-19 08:05:35'),
(21, 3, 4, 0, '', '2023-07-19 08:06:50', '2023-07-19 08:05:39', '2023-07-19 08:05:39'),
(22, 7, 4, 0, '', '2023-07-19 08:06:51', '2023-07-19 08:05:42', '2023-07-19 08:05:42'),
(23, 1, 4, 0, '', '2023-07-19 08:06:52', '2023-07-19 08:06:21', '2023-07-19 08:06:21'),
(24, 8, 3, 0, '', '2023-07-19 08:10:54', '2023-07-19 08:10:42', '2023-07-19 08:10:42');

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `id` int(10) NOT NULL,
  `name` varchar(25) NOT NULL,
  `username` varchar(25) NOT NULL,
  `password` varchar(125) NOT NULL,
  `email` varchar(30) NOT NULL,
  `phone_no` int(10) NOT NULL,
  `isAdmin` varchar(10) NOT NULL DEFAULT 'false',
  `createdAt` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`id`, `name`, `username`, `password`, `email`, `phone_no`, `isAdmin`, `createdAt`) VALUES
(1, 'admin', 'admin', '1234', 'admin@email.com', 1234567980, 'true', '2023-07-14 12:04:35'),
(3, 'test user', 'testuser', '1234', 'test@email.com', 1234567890, 'false', '2023-07-14 12:04:48'),
(4, 'test', 'test', '1234', 'mahetajack@gmaiil.com', 123, 'false', '2023-07-19 06:27:31'),
(5, 'van', 'asd', '1234', 'mahetajack@gmaiil.com', 123, 'false', '2023-07-19 08:07:10');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `book`
--
ALTER TABLE `book`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `book_log`
--
ALTER TABLE `book_log`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `book`
--
ALTER TABLE `book`
  MODIFY `id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `book_log`
--
ALTER TABLE `book_log`
  MODIFY `id` int(3) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=25;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
