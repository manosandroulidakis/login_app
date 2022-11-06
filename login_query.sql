CREATE DATABASE IF NOT EXISTS `login` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `login`;

CREATE TABLE IF NOT EXISTS `accounts` (
`id` int(11) NOT NULL AUTO_INCREMENT,
`username` varchar(50) NOT NULL,
`password` varchar(255) NOT NULL,
`email` varchar(100) NOT NULL,
PRIMARY KEY (`id`)
)ENGINE=Innodb AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

CREATE TABLE IF NOT EXISTS `inputs` (
`id` int(11) NOT NULL AUTO_INCREMENT,
`username` varchar(50) NOT NULL,
`first_name` varchar(50) NOT NULL,
`last_name` varchar(255) NOT NULL,
`location` varchar(100) NOT NULL,
PRIMARY KEY (`id`)
)ENGINE=Innodb AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;