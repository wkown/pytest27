/*
SQLyog Ultimate v11.24 (32 bit)
MySQL - 5.5.47 : Database - 2016_special_test
*********************************************************************
*/


/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
/*Table structure for table `cf_channel` */

DROP TABLE IF EXISTS `cf_channel`;

CREATE TABLE `cf_channel` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(20) NOT NULL,
  `directory` varchar(200) NOT NULL COMMENT '文件目录',
  `domainname` varchar(200) NOT NULL COMMENT '域名',
  `leader` varchar(20) NOT NULL COMMENT '负责人',
  `leadertel` varchar(20) NOT NULL COMMENT '负责人电话',
  `monitorid` int(10) NOT NULL COMMENT '对应监测点id',
  `msg_id` int(10) unsigned NOT NULL COMMENT '消息id',
  `status` tinyint(2) NOT NULL,
  `modified` int(10) unsigned NOT NULL COMMENT '修改时间',
  `dateline` int(10) unsigned NOT NULL COMMENT '创建时间',
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC;

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
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='联系人表';

/*Data for the table `cf_contact` */

/*Table structure for table `cf_file` */

DROP TABLE IF EXISTS `cf_file`;

CREATE TABLE `cf_file` (
  `file_id` int(10) unsigned NOT NULL AUTO_INCREMENT COMMENT '文件id',
  `msg_id` int(10) unsigned NOT NULL DEFAULT '0' COMMENT '消息id',
  `channel_id` int(10) unsigned NOT NULL DEFAULT '0' COMMENT '频道id',
  `path_md5` char(32) NOT NULL DEFAULT '' COMMENT '路径MD5值',
  `path` varchar(500) NOT NULL DEFAULT '' COMMENT '文件完整路径',
  `dir` varchar(500) NOT NULL DEFAULT '' COMMENT '文件完整目录路径',
  `isolate_path` varchar(500) NOT NULL DEFAULT '' COMMENT '隔离文件路径',
  `status` tinyint(3) unsigned NOT NULL DEFAULT '0' COMMENT '状态:0已记录,1已隔离,2已删除,3已恢复',
  `modified` int(10) unsigned NOT NULL DEFAULT '0' COMMENT '修改时间',
  `dateline` int(10) unsigned NOT NULL DEFAULT '0' COMMENT '删除时间',
  PRIMARY KEY (`file_id`),
  UNIQUE KEY `MD5` (`path_md5`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COMMENT='异常文件记录';

/*Data for the table `cf_file` */

/*Table structure for table `cf_monitor` */

DROP TABLE IF EXISTS `cf_monitor`;

CREATE TABLE `cf_monitor` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(20) NOT NULL COMMENT '监测点名称',
  `telephone` varchar(20) NOT NULL COMMENT '负责人电话',
  `status` tinyint(2) NOT NULL COMMENT '状态',
  `inputtime` int(20) NOT NULL COMMENT '添加时间',
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

/*Data for the table `cf_monitor` */

/*Table structure for table `cf_msg` */

DROP TABLE IF EXISTS `cf_msg`;

CREATE TABLE `cf_msg` (
  `msg_id` int(10) unsigned NOT NULL AUTO_INCREMENT COMMENT '消息id',
  `file_count` int(10) unsigned NOT NULL DEFAULT '0' COMMENT '异常文件数',
  `dir_count` int(10) unsigned NOT NULL DEFAULT '0' COMMENT '异常目录数',
  `channel_id` int(10) unsigned NOT NULL DEFAULT '0' COMMENT '频道id',
  `modified` int(10) unsigned NOT NULL DEFAULT '0' COMMENT '修改时间',
  `dateline` int(10) unsigned NOT NULL DEFAULT '0' COMMENT '创建时间',
  PRIMARY KEY (`msg_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='消息记录表';

/*Data for the table `cf_msg` */

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
