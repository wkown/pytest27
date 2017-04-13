ALTER TABLE `cf_file` ADD COLUMN `channel_id` INT UNSIGNED DEFAULT 0 NOT NULL COMMENT '频道id' AFTER `msg_id`;
/* 文件增加md5索引 zwj 20160812 1526*/
ALTER TABLE `cf_file` ADD COLUMN `path_md5` CHAR(32) DEFAULT '' NOT NULL COMMENT '路径MD5值' AFTER `channel_id`;
ALTER TABLE `cf_file` ADD UNIQUE INDEX `MD5` (`path_md5`);

/* 消息表增加频道ID记录 zwj 20160812 1752 */
ALTER TABLE `cf_msg`
DROP COLUMN `dirs`,
ADD COLUMN `channel_id` INT(10) UNSIGNED DEFAULT 0 NOT NULL COMMENT '频道id' AFTER `dir_count`;