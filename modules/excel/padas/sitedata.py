# -*- coding:utf-8 -*-

import pandas as pd
import time

if __name__ == "__main__":
    datafile = raw_input("datafile:")

    if datafile == "":
        datafile = u"data.xlsx"

    dataFrame = pd.read_excel(datafile)
    #for row in dataFrame.iteritems():
    #    print row

    tpl = u"""
DROP TABLE IF EXISTS `yq_website`;
CREATE TABLE `website` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(30) NOT NULL COMMENT '站点名称',
  `domain` varchar(50) NOT NULL DEFAULT '',
  `site_domain` varchar(50) NOT NULL DEFAULT '',
  `province` varchar(10) NOT NULL DEFAULT '' COMMENT '省',
  `city` varchar(15) NOT NULL DEFAULT '' COMMENT '市',
  `type` tinyint(1) NOT NULL DEFAULT '0',
  `status` tinyint(1) NOT NULL DEFAULT '1',
  `modified` int(10) NOT NULL DEFAULT '0' COMMENT '修改时间',
  `created` int(10) NOT NULL DEFAULT '0' COMMENT '创建时间',
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=1587 DEFAULT CHARSET=utf8;

LOCK TABLES `website` WRITE;
INSERT INTO `website` VALUES """
    #(2,'sss','xxxxxxx.cn','www.xxxxxxxx.cn','sss','xxx',4,1,1527757960,0)
    tpl2 = u"(%d,'%s','%s','%s','%s','%s',%d,%d,%d,%d)"

    conj = ''
    for row in dataFrame.itertuples():
        #print row[1:-2]
        #print row[1:3]
        #print row[4:-2]
        l = list(row[1:3])
        l.extend(row[4:-3])
        l.extend([int(time.time()), int(time.time())])
        #print l
        tpl += conj + (tpl2 % tuple(l))
        conj = u','

tpl = tpl.replace("'nan'", "''")
print tpl+";\n\nUNLOCK TABLES;"
