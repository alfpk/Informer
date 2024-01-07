-- phpMyAdmin SQL Dump
-- version 5.2.1deb1
-- https://www.phpmyadmin.net/
--
-- Хост: localhost:3306
-- Время создания: Дек 28 2023 г., 21:26
-- Версия сервера: 10.11.4-MariaDB-1~deb12u1
-- Версия PHP: 8.2.7

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- База данных: `ostmc`
--

-- --------------------------------------------------------

--
-- Структура таблицы `bot_bday_registry`
--

CREATE TABLE `bot_bday_registry` (
  `id` int(11) NOT NULL,
  `name` varchar(64) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci DEFAULT NULL,
  `family` varchar(64) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci DEFAULT NULL,
  `roadname` varchar(64) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci DEFAULT NULL,
  `bday` date NOT NULL,
  `role` varchar(32) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;

--
-- Дамп данных таблицы `bot_bday_registry`
--

INSERT INTO `bot_bday_registry` (`id`, `name`, `family`, `roadname`, `bday`, `role`) VALUES
(2, NULL, NULL, 'OST MC', '2013-03-07', NULL),
(3, 'Кирилл', 'Петров', 'ALF', '1979-04-26', 'Secretary'),
(4, 'Вячеслав', 'Харинов', 'Отец Вячеслав', '1961-03-27', 'President'),
(5, 'Всеволод', 'Купцов', 'Бульдог', '1980-02-10', 'Vice President'),
(6, 'Максим', 'Лисовский', 'Лис', '1978-03-07', 'RoadCaptain'),
(7, 'Геннадий', 'Зубковский', 'Капитан', '1954-11-12', 'Treasurer'),
(8, 'Даниил', 'Бартенев', 'М4С', '1982-10-22', 'Secretary'),
(9, 'Павел', 'Андреев', 'Сантехник', '1975-10-17', 'Member'),
(10, 'Денис', 'Филиппов', 'Дэн', '1985-09-14', 'Member'),
(11, 'Сергей', 'Филиппчук', 'Хулиган', '1985-02-06', 'Member'),
(12, 'Рейнов', 'Влад', 'Кочевник', '1975-02-02', 'Member'),
(13, 'Павел', 'Зотов', 'Стоматолог', '1987-06-04', 'Member'),
(14, 'Денис', 'Карпов', 'Мазай', '1976-06-10', 'Member'),
(15, 'Сергей', 'Раевский', 'Раевский', '1970-05-23', 'Member'),
(16, 'Алексей', 'Поташевский', 'Паралайнен', '1971-06-15', NULL);

-- --------------------------------------------------------

--
-- Структура таблицы `club_registry`
--

CREATE TABLE `club_registry` (
  `id` int(11) NOT NULL,
  `name` varchar(64) DEFAULT NULL,
  `mid_name` varchar(64) DEFAULT NULL,
  `family` varchar(64) DEFAULT NULL,
  `road_name` varchar(64) DEFAULT NULL,
  `status` varchar(64) DEFAULT NULL,
  `bday` date DEFAULT NULL,
  `phone` varchar(15) DEFAULT NULL,
  `email` varchar(32) DEFAULT NULL,
  `gmail` varchar(32) DEFAULT NULL,
  `out_state` varchar(32) DEFAULT NULL,
  `standing` varchar(15) DEFAULT NULL,
  `description` varchar(64) DEFAULT NULL,
  `img_filename` varchar(15) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_general_ci;

--
-- Индексы сохранённых таблиц
--

--
-- Индексы таблицы `bot_bday_registry`
--
ALTER TABLE `bot_bday_registry`
  ADD PRIMARY KEY (`id`);

--
-- Индексы таблицы `club_registry`
--
ALTER TABLE `club_registry`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT для сохранённых таблиц
--

--
-- AUTO_INCREMENT для таблицы `bot_bday_registry`
--
ALTER TABLE `bot_bday_registry`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=17;

--
-- AUTO_INCREMENT для таблицы `club_registry`
--
ALTER TABLE `club_registry`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
