#!/usr/bin/python
# -*- coding:utf-8 -*-
__author__ = 'walkskyer'
"""
备份mysql指定的数据库
"""
import time
import ConfigParser
import os

if __name__ == "__main__":
    config = ConfigParser.SafeConfigParser()
    file_path = os.path.dirname(os.path.realpath(__file__))
    config.read('%s/mysql_backup.ini' % file_path)
    cfg_common = dict(config.items('common'))
    datetime = time.strftime('%w_%H%M')#按周命名最多可存储最近一周的备份
    for i in xrange(1, 1000):
        try:
            db = dict(config.items('db%s' % i))
            filename = "%s_%s" % (db['db'], datetime)
            cmd = "%smysqldump --opt -h%s -u %s --password=%s %s > %s/%s.sql" % (
                cfg_common['mysqldump_path'], db['host'], db['user'], db['pwd'], db['db'], cfg_common['path'], filename)
            #print cmd
            os.system(cmd)
        except Exception, e:
            # print e
            break
