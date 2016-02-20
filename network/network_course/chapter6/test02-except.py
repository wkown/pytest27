# -*- coding:utf-8 -*-
__author__ = 'walkskyer'
"""
print response info with exception handle
"""
import sys, urllib2
if __name__ == "__main__":

    req = urllib2.Request(sys.argv[1])
    try:
        fd = urllib2.urlopen(req)
    except urllib2.HTTPError, e:
        print "Error retrieving data:", e
        print "Server error document follows:\n"
        print e.read()
        sys.exit(1)
    except urllib2.URLError, e:
        print "Error retrieving data:", e
        sys.exit(2)
    print "Retrieved", fd.geturl()
    for key, value in fd.info().items():
        print "%s = %s" % (key, value)