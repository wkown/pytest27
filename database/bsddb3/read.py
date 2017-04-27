# -*- coding:utf-8 -*-
import bsddb

"""
显示数据库内容
"""

def test_db(filename):
    print 'show data from file(%s):' % filename
    count = 0
    for k, v in bsddb.hashopen(filename).iteritems():
        count += 1
        print "% 4d %s %s" % (count, k, v)

if __name__ == "__main__":
    while True:
        filename = raw_input("Please input bsddb file path:")
        test_db(filename)
        print "The read process end: %s" % filename