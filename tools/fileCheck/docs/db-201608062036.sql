/*
SQLyog Ultimate v11.24 (32 bit)
MySQL - 5.5.47 : Database - 2016_checkfile
*********************************************************************
*/


/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
/*Table structure for table `cf_contact` */

DROP TABLE IF EXISTS `cf_contact`;

CREATE TABLE `cf_contact` (
  `contact_id` int(10) unsigned NOT NULL AUTO_INCREMENT COMMENT '联系人id',
  `name` varchar(20) NOT NULL DEFAULT '' COMMENT '联系人姓名',
  `mobile` varchar(15) NOT NULL DEFAULT '' COMMENT '联系人手机号',
  `msg_id` int(10) unsigned NOT NULL DEFAULT '0' COMMENT '最后接收消息id',
  `status` tinyint(4) NOT NULL DEFAULT '0' COMMENT '状态',
  `modified` int(10) unsigned NOT NULL DEFAULT '0' COMMENT '修改时间',
  `dateline` int(10) unsigned NOT NULL DEFAULT '0' COMMENT '创建时间',
  PRIMARY KEY (`contact_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 COMMENT='联系人表';

/*Data for the table `cf_contact` */

insert  into `cf_contact`(`contact_id`,`name`,`mobile`,`msg_id`,`status`,`modified`,`dateline`) values (1,'jj','13000000000',0,0,1470486127,0);

/*Table structure for table `cf_file` */

DROP TABLE IF EXISTS `cf_file`;

CREATE TABLE `cf_file` (
  `file_id` int(10) unsigned NOT NULL AUTO_INCREMENT COMMENT '文件id',
  `msg_id` int(10) unsigned NOT NULL DEFAULT '0' COMMENT '消息id',
  `path` varchar(500) NOT NULL DEFAULT '' COMMENT '文件完整路径',
  `dir` varchar(500) NOT NULL DEFAULT '' COMMENT '文件完整目录路径',
  `isolate_path` varchar(500) NOT NULL DEFAULT '' COMMENT '隔离文件路径',
  `status` tinyint(3) unsigned NOT NULL DEFAULT '0' COMMENT '状态:0已记录,1已隔离,2已删除,3已恢复',
  `modified` int(10) unsigned NOT NULL DEFAULT '0' COMMENT '修改时间',
  `dateline` int(10) unsigned NOT NULL DEFAULT '0' COMMENT '删除时间',
  PRIMARY KEY (`file_id`)
) ENGINE=MyISAM AUTO_INCREMENT=21 DEFAULT CHARSET=utf8 COMMENT='异常文件记录';

/*Data for the table `cf_file` */

insert  into `cf_file`(`file_id`,`msg_id`,`path`,`dir`,`isolate_path`,`status`,`modified`,`dateline`) values (20,16,'/home/walkskyer/dev/test_file_notify/original-02.html','/home/walkskyer/dev/test_file_notify','',0,0,0);

/*Table structure for table `cf_msg` */

DROP TABLE IF EXISTS `cf_msg`;

CREATE TABLE `cf_msg` (
  `msg_id` int(10) unsigned NOT NULL AUTO_INCREMENT COMMENT '消息id',
  `file_count` int(10) unsigned NOT NULL DEFAULT '0' COMMENT '异常文件数',
  `dir_count` int(10) unsigned NOT NULL DEFAULT '0' COMMENT '异常目录数',
  `dirs` text NOT NULL COMMENT '异常目录',
  `modified` int(10) unsigned NOT NULL DEFAULT '0' COMMENT '修改时间',
  `dateline` int(10) unsigned NOT NULL DEFAULT '0' COMMENT '创建时间',
  PRIMARY KEY (`msg_id`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8 COMMENT='消息记录表';

/*Data for the table `cf_msg` */

insert  into `cf_msg`(`msg_id`,`file_count`,`dir_count`,`dirs`,`modified`,`dateline`) values (16,1,1,'/home/walkskyer/dev/test_file_notify',1470485811,1470485811);

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
