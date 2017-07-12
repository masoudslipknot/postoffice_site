-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Server version:               4.1.22-community-nt - MySQL Community Edition (GPL)
-- Server OS:                    Win32
-- HeidiSQL Version:             9.4.0.5125
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;


-- Dumping database structure for dhlpost
CREATE DATABASE IF NOT EXISTS `dhlpost` /*!40100 DEFAULT CHARACTER SET latin1 */;
USE `dhlpost`;

-- Dumping structure for table dhlpost.adress
CREATE TABLE IF NOT EXISTS `adress` (
  `id` int(11) NOT NULL auto_increment,
  `center_state` varchar(30) NOT NULL default '0',
  `city` varchar(30) NOT NULL default '0',
  `street` varchar(50) NOT NULL default '0',
  `post_code` int(11) NOT NULL default '0',
  `pelate` int(11) NOT NULL default '0',
  `floor` int(11) NOT NULL default '0',
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Data exporting was unselected.
-- Dumping structure for table dhlpost.customer_sender
CREATE TABLE IF NOT EXISTS `customer_sender` (
  `sex` varchar(30) default NULL,
  `id` int(11) NOT NULL auto_increment,
  `username` varchar(50) NOT NULL default '0',
  `last_degree` varchar(30) default NULL,
  PRIMARY KEY  (`id`),
  KEY `FK_customer_sender_indivisoial_customer` (`username`),
  CONSTRAINT `FK_customer_sender_indivisoial_customer` FOREIGN KEY (`username`) REFERENCES `indivisoial_customer` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Data exporting was unselected.
-- Dumping structure for table dhlpost.dispatch
CREATE TABLE IF NOT EXISTS `dispatch` (
  `id` int(11) NOT NULL auto_increment,
  `title` varchar(30) NOT NULL default '0',
  `description` varchar(100) NOT NULL default '0',
  `weight` int(11) NOT NULL default '0',
  `state` int(11) NOT NULL default '0',
  `type` varchar(30) NOT NULL default '0',
  `user_sender` varchar(30) NOT NULL default '0',
  `user_reciver` varchar(30) NOT NULL default '0',
  PRIMARY KEY  (`id`),
  KEY `FK_dispatch_user` (`user_sender`),
  KEY `FK_dispatch_user_2` (`user_reciver`),
  CONSTRAINT `FK_dispatch_user` FOREIGN KEY (`user_sender`) REFERENCES `user` (`username`),
  CONSTRAINT `FK_dispatch_user_2` FOREIGN KEY (`user_reciver`) REFERENCES `user` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Data exporting was unselected.
-- Dumping structure for table dhlpost.employee
CREATE TABLE IF NOT EXISTS `employee` (
  `id` int(11) NOT NULL auto_increment,
  `username` varchar(30) NOT NULL default '0',
  `name` varchar(40) NOT NULL default '0',
  `ssn` int(11) NOT NULL default '0',
  `mobile` int(11) NOT NULL default '0',
  `email` varchar(50) NOT NULL default '0',
  `last_degree` varchar(50) NOT NULL default '0',
  `time_stamp` timestamp NOT NULL default '0000-00-00 00:00:00',
  `employee_type` varchar(30) NOT NULL default '0',
  PRIMARY KEY  (`id`),
  KEY `FK_employee_user` (`username`),
  CONSTRAINT `FK_employee_user` FOREIGN KEY (`username`) REFERENCES `user` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Data exporting was unselected.
-- Dumping structure for table dhlpost.indivisoial_customer
CREATE TABLE IF NOT EXISTS `indivisoial_customer` (
  `username` varchar(30) NOT NULL default '',
  `name` varchar(30) NOT NULL default '',
  `ssn` int(11) NOT NULL default '0',
  `mobile` int(11) NOT NULL default '0',
  `email` varchar(40) NOT NULL default '',
  PRIMARY KEY  (`ssn`),
  KEY `FK_indivisoial_customer_user` (`username`),
  CONSTRAINT `FK_indivisoial_customer_user` FOREIGN KEY (`username`) REFERENCES `user` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Data exporting was unselected.
-- Dumping structure for table dhlpost.organizational
CREATE TABLE IF NOT EXISTS `organizational` (
  `username` varchar(30) NOT NULL default '',
  `type` varchar(30) NOT NULL default '',
  `email` varchar(30) NOT NULL default '',
  `name` varchar(30) NOT NULL default '',
  PRIMARY KEY  (`email`),
  KEY `FK_organizational_user` (`username`),
  CONSTRAINT `FK_organizational_user` FOREIGN KEY (`username`) REFERENCES `user` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Data exporting was unselected.
-- Dumping structure for table dhlpost.post_office
CREATE TABLE IF NOT EXISTS `post_office` (
  `name` varchar(30) NOT NULL default '',
  `manager` varchar(30) NOT NULL default '',
  `office_type` varchar(30) NOT NULL default '',
  `village_code` int(11) NOT NULL default '0',
  `urban_code` int(11) NOT NULL default '0',
  `city_code` int(11) NOT NULL default '0',
  `state_code` int(11) NOT NULL default '0',
  PRIMARY KEY  (`name`),
  KEY `FK_post_office_employee` (`manager`),
  CONSTRAINT `FK_post_office_employee` FOREIGN KEY (`manager`) REFERENCES `employee` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Data exporting was unselected.
-- Dumping structure for table dhlpost.recid
CREATE TABLE IF NOT EXISTS `recid` (
  `id` int(11) NOT NULL auto_increment,
  `dispachnumber` int(11) NOT NULL default '0',
  `post_name` varchar(30) NOT NULL default '0',
  `employee_name` varchar(30) NOT NULL default '0',
  `timestamp` timestamp NOT NULL default '0000-00-00 00:00:00',
  `tracking_number` int(11) NOT NULL default '0',
  PRIMARY KEY  (`id`),
  KEY `FK_recid_dispatch` (`dispachnumber`),
  KEY `FK_recid_post_office` (`post_name`),
  CONSTRAINT `FK_recid_post_office` FOREIGN KEY (`post_name`) REFERENCES `post_office` (`name`),
  CONSTRAINT `FK_recid_dispatch` FOREIGN KEY (`dispachnumber`) REFERENCES `dispatch` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Data exporting was unselected.
-- Dumping structure for table dhlpost.user
CREATE TABLE IF NOT EXISTS `user` (
  `username` varchar(30) NOT NULL default '',
  `address` int(11) NOT NULL default '0',
  `pass` varchar(33) NOT NULL default '',
  `phone` int(11) NOT NULL default '0',
  `type` varchar(33) NOT NULL default '',
  PRIMARY KEY  (`username`),
  KEY `FK_user_adress` (`address`),
  CONSTRAINT `FK_user_adress` FOREIGN KEY (`address`) REFERENCES `adress` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Data exporting was unselected.
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
