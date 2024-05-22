/*
SQLyog Community v13.1.5  (64 bit)
MySQL - 5.6.12-log : Database - cruice_on_myhand
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`cruice_on_myhand` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `cruice_on_myhand`;

/*Table structure for table `activities in work` */

DROP TABLE IF EXISTS `activities in work`;

CREATE TABLE `activities in work` (
  `activity_id` int(11) NOT NULL AUTO_INCREMENT,
  `work_id` int(11) DEFAULT NULL,
  `staff_id` int(11) DEFAULT NULL,
  `date` date DEFAULT NULL,
  `status` varchar(60) DEFAULT NULL,
  `activities` varchar(60) DEFAULT NULL,
  PRIMARY KEY (`activity_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `activities in work` */

/*Table structure for table `allocate room` */

DROP TABLE IF EXISTS `allocate room`;

CREATE TABLE `allocate room` (
  `allocation_id` int(11) NOT NULL AUTO_INCREMENT,
  `room_id` int(11) DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`allocation_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `allocate room` */

/*Table structure for table `allocate work` */

DROP TABLE IF EXISTS `allocate work`;

CREATE TABLE `allocate work` (
  `allocate_work_id` int(11) NOT NULL AUTO_INCREMENT,
  `staff_id` int(11) DEFAULT NULL,
  `work_id` int(11) DEFAULT NULL,
  `status` varchar(150) DEFAULT NULL,
  PRIMARY KEY (`allocate_work_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `allocate work` */

/*Table structure for table `book hall` */

DROP TABLE IF EXISTS `book hall`;

CREATE TABLE `book hall` (
  `bh_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL,
  `ship_id` int(11) DEFAULT NULL,
  `date` date DEFAULT NULL,
  `status` varchar(50) DEFAULT NULL,
  `required_time_from` time DEFAULT NULL,
  `require_time_to` time DEFAULT NULL,
  PRIMARY KEY (`bh_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `book hall` */

/*Table structure for table `booking` */

DROP TABLE IF EXISTS `booking`;

CREATE TABLE `booking` (
  `booking_id` int(11) NOT NULL AUTO_INCREMENT,
  `ship_id` int(11) DEFAULT NULL,
  `login_id` int(11) DEFAULT NULL,
  `status` varchar(50) DEFAULT NULL,
  `date` date DEFAULT NULL,
  `no_user` int(11) DEFAULT NULL,
  PRIMARY KEY (`booking_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `booking` */

/*Table structure for table `complaint` */

DROP TABLE IF EXISTS `complaint`;

CREATE TABLE `complaint` (
  `complaint_id` int(11) NOT NULL AUTO_INCREMENT,
  `date` date DEFAULT NULL,
  `ul_id` int(11) DEFAULT NULL,
  `complaint` varchar(200) DEFAULT NULL,
  `reply` varchar(200) DEFAULT NULL,
  `status` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`complaint_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `complaint` */

/*Table structure for table `facilities` */

DROP TABLE IF EXISTS `facilities`;

CREATE TABLE `facilities` (
  `f_id` int(11) NOT NULL AUTO_INCREMENT,
  `ship_id` int(11) DEFAULT NULL,
  `facilities` varchar(200) DEFAULT NULL,
  `description` varchar(555) DEFAULT NULL,
  `charge` int(11) DEFAULT NULL,
  PRIMARY KEY (`f_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `facilities` */

/*Table structure for table `journey` */

DROP TABLE IF EXISTS `journey`;

CREATE TABLE `journey` (
  `journey_id` int(11) NOT NULL AUTO_INCREMENT,
  `ship_id` int(11) DEFAULT NULL,
  `start_port` varchar(100) DEFAULT NULL,
  `end_port` varchar(200) DEFAULT NULL,
  `start_date` date DEFAULT NULL,
  `end_date` date DEFAULT NULL,
  `status` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`journey_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `journey` */

/*Table structure for table `location` */

DROP TABLE IF EXISTS `location`;

CREATE TABLE `location` (
  `location_id` int(11) NOT NULL AUTO_INCREMENT,
  `ship_id` int(11) DEFAULT NULL,
  `date` date DEFAULT NULL,
  `time` time DEFAULT NULL,
  `latitude` varchar(50) DEFAULT NULL,
  `longitude` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`location_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `location` */

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `login_id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(50) DEFAULT NULL,
  `password` varchar(50) DEFAULT NULL,
  `type` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`login_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `login` */

insert  into `login`(`login_id`,`username`,`password`,`type`) values 
(1,'admin','admin','admin');

/*Table structure for table `port` */

DROP TABLE IF EXISTS `port`;

CREATE TABLE `port` (
  `port_id` int(11) NOT NULL AUTO_INCREMENT,
  `port_name` varchar(50) DEFAULT NULL,
  `country_name` varchar(50) DEFAULT NULL,
  `country_code` varchar(50) DEFAULT NULL,
  `latitude` varchar(100) DEFAULT NULL,
  `longitude` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`port_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `port` */

/*Table structure for table `rating` */

DROP TABLE IF EXISTS `rating`;

CREATE TABLE `rating` (
  `rating_id` int(10) NOT NULL AUTO_INCREMENT,
  `user_id` int(10) DEFAULT NULL,
  `ship_id` int(11) DEFAULT NULL,
  `rating` varchar(100) DEFAULT NULL,
  `review` varchar(500) DEFAULT NULL,
  `date` date DEFAULT NULL,
  PRIMARY KEY (`rating_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `rating` */

/*Table structure for table `room` */

DROP TABLE IF EXISTS `room`;

CREATE TABLE `room` (
  `room_id` int(11) NOT NULL AUTO_INCREMENT,
  `ship_id` int(11) DEFAULT NULL,
  `room_no` int(11) DEFAULT NULL,
  `class` varchar(60) DEFAULT NULL,
  `rate` int(11) DEFAULT NULL,
  PRIMARY KEY (`room_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `room` */

/*Table structure for table `schedule` */

DROP TABLE IF EXISTS `schedule`;

CREATE TABLE `schedule` (
  `s_id` int(11) NOT NULL AUTO_INCREMENT,
  `ship_id` int(11) DEFAULT NULL,
  `j_id` varchar(50) DEFAULT NULL,
  `departure_time` varchar(300) DEFAULT NULL,
  `arrival_time` varchar(333) DEFAULT NULL,
  `date` date DEFAULT NULL,
  `arrival_port` varchar(50) DEFAULT NULL,
  `departure_port` varchar(60) DEFAULT NULL,
  PRIMARY KEY (`s_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `schedule` */

/*Table structure for table `ship` */

DROP TABLE IF EXISTS `ship`;

CREATE TABLE `ship` (
  `ship_id` int(11) NOT NULL AUTO_INCREMENT,
  `login_id` int(11) DEFAULT NULL,
  `ship_name` varchar(50) DEFAULT NULL,
  `discription` varchar(600) DEFAULT NULL,
  `capacity` int(50) DEFAULT NULL,
  `photo` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`ship_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `ship` */

/*Table structure for table `staff` */

DROP TABLE IF EXISTS `staff`;

CREATE TABLE `staff` (
  `staff_id` int(11) NOT NULL AUTO_INCREMENT,
  `ship_id` int(11) DEFAULT NULL,
  `login_id` int(11) DEFAULT NULL,
  `name` varchar(50) DEFAULT NULL,
  `place` varchar(50) DEFAULT NULL,
  `pin` int(11) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  `phone` int(11) DEFAULT NULL,
  `work` varchar(50) DEFAULT NULL,
  `photo` varchar(150) DEFAULT NULL,
  PRIMARY KEY (`staff_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `staff` */

/*Table structure for table `user` */

DROP TABLE IF EXISTS `user`;

CREATE TABLE `user` (
  `user_id` int(11) NOT NULL AUTO_INCREMENT,
  `login_id` int(11) DEFAULT NULL,
  `name` varchar(50) DEFAULT NULL,
  `place` varchar(50) DEFAULT NULL,
  `post` varchar(50) DEFAULT NULL,
  `pin` varchar(50) DEFAULT NULL,
  `phone` int(11) DEFAULT NULL,
  `email` varchar(60) DEFAULT NULL,
  `gender` varchar(60) DEFAULT NULL,
  `image` varchar(300) DEFAULT NULL,
  PRIMARY KEY (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `user` */

/*Table structure for table `work` */

DROP TABLE IF EXISTS `work`;

CREATE TABLE `work` (
  `work_id` int(11) NOT NULL AUTO_INCREMENT,
  `ship_id` int(11) DEFAULT NULL,
  `work` varchar(50) DEFAULT NULL,
  `date` date DEFAULT NULL,
  `status` varchar(15) DEFAULT NULL,
  PRIMARY KEY (`work_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `work` */

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
