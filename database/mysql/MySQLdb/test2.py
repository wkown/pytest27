#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'weijie'
import MySQLdb as mdb
import types

#使用utf8编码
con = mdb.connect('localhost', 'root',
                  '', 'test', charset="utf8")

#返回元组
with con:
    cur = con.cursor()
    cur.execute("SELECT * FROM product")    #执行查询语句
    rows = cur.fetchall()
    for row in rows:
        print row

#返回字典
with con:
    cur = con.cursor(mdb.cursors.DictCursor)
    cur.execute("SELECT * FROM product")    #执行查询语句
    rows = cur.fetchall()
    for row in rows:
        print row['pname']
        print row

#删除数据
with con:
    cur = con.cursor()
    cur.execute("DELETE FROM product")


#插入数据
insertRows = (
{'status': 1, 'auctionid': 0L, 'total_comm': 0L, 'catid': 0L, 'commission': 0.0, 'url': u'', 'bid': 0.0, 'artnum': None,
 'modified': 1368689428L, 'purl_md5': u'', 'buyclick': 0L, 'url_md5': u'', 'dateline': 1368584599L,
 'pname': u'\u95e8\u7968', 'commrate': 0.0,
 'icon': u'http://img02.taobaocdn.com/bao/uploaded/i2/T1CS5nXkVkXXcNdvI0_034920.jpg_170x170.jpg', 'click': 0L,
 'totalnum': 0L, 'purl': u''},
{'status': 2, 'auctionid': 0L, 'total_comm': 0L, 'catid': 0L, 'commission': 0.0, 'url': u'', 'bid': 0.0, 'artnum': None,
 'modified': 1368689467L, 'purl_md5': u'', 'buyclick': 0L, 'url_md5': u'', 'dateline': 1368584671L,
 'pname': u'\u597d\u95e8\u7968', 'commrate': 0.0,
 'icon': u'http://img03.taobaocdn.com/bao/uploaded/i3/16984018883285294/T12iMyXmJeXXXXXXXX_!!0-item_pic.jpg_170x170.jpg',
 'click': 0L, 'totalnum': 0L, 'purl': u''},
{'status': 1, 'auctionid': 0L, 'total_comm': 0L, 'catid': 0L, 'commission': 0.0, 'url': u'', 'bid': 0.0, 'artnum': None,
 'modified': 1368689489L, 'purl_md5': u'', 'buyclick': 0L, 'url_md5': u'', 'dateline': 1368602246L,
 'pname': u'\u7b2c\u4e09\u4e2a', 'commrate': 0.0,
 'icon': u'http://image.taobao.com/bao/uploaded/64154770/T2N6LdXndXXXXXXXXX_!!64154770.jpg_170x170.jpg', 'click': 0L,
 'totalnum': 0L, 'purl': u''},
{'status': 2, 'auctionid': 0L, 'total_comm': 0L, 'catid': 0L, 'commission': 0.0, 'url': u'', 'bid': 0.0, 'artnum': None,
 'modified': 1368693906L, 'purl_md5': u'', 'buyclick': 0L, 'url_md5': u'', 'dateline': 1368690599L,
 'pname': u'Acer/\u5b8f\u57fa S3-391-53314G52a', 'commrate': 0.0,
 'icon': u'http://img01.taobaocdn.com/bao/uploaded/i1/T1Z2DOXmNgXXa2L3k4_053042.jpg_210x210.jpg', 'click': 0L,
 'totalnum': 0L, 'purl': u''},
{'status': 1, 'auctionid': 0L, 'total_comm': 0L, 'catid': 0L, 'commission': 0.0, 'url': u'', 'bid': 0.0, 'artnum': None,
 'modified': 1368690684L, 'purl_md5': u'', 'buyclick': 0L, 'url_md5': u'', 'dateline': 1368690652L,
 'pname': u'Acer/\u5b8f\u57fa S7-391-53314G25a', 'commrate': 0.0,
 'icon': u'http://img04.taobaocdn.com/bao/uploaded/i4/14900032666264372/T1sYXoXtXfXXXXXXXX_!!0-item_pic.jpg_210x210.jpg',
 'click': 0L, 'totalnum': 0L, 'purl': u''},
{'status': 1, 'auctionid': 0L, 'total_comm': 0L, 'catid': 4L, 'commission': 0.0, 'url': u'', 'bid': 0.0, 'artnum': None,
 'modified': 1369209421L, 'purl_md5': u'', 'buyclick': 0L, 'url_md5': u'', 'dateline': 1368690717L,
 'pname': u'Lenovo/\u8054\u60f3 U310-IFI', 'commrate': 0.0,
 'icon': u'http://img03.taobaocdn.com/bao/uploaded/i3/T1pg64XiJjXXXtGCU8_101631.jpg_210x210.jpg', 'click': 0L,
 'totalnum': 0L, 'purl': u''},
{'status': 0, 'auctionid': 0L, 'total_comm': 0L, 'catid': 4L, 'commission': 0.0, 'url': u'', 'bid': 0.0, 'artnum': None,
 'modified': 1369209385L, 'purl_md5': u'', 'buyclick': 0L, 'url_md5': u'', 'dateline': 1369118753L,
 'pname': u'\u6d4b\u8bd5\u4ea7\u54c1\u5206\u7c7b', 'commrate': 0.0, 'icon': u'', 'click': 0L, 'totalnum': 0L,
 'purl': u''})
with con:
    cur = con.cursor()
    for row in insertRows:
        query = u'INSERT INTO product '
        values='VALUES ('
        column=''
        conj = u''
        for k, v in row.items():
            vType = type(v)
            numType = [types.IntType, types.LongType, types.FloatType]
            if vType in numType:
                v = str(v)
            if vType is types.NoneType:
                v = u'\'\''
            if vType is types.UnicodeType:
                v = u'\'' + v + u'\''
                v.encode('utf8')
            column += conj + u'`' + k + u'`'
            values += conj + v
            conj = u','
        values += u');'
        query = u'INSERT INTO product(' + column + ') '+ values
        cur.execute(query)
