# -*- coding:utf-8 -*-
__author__ = 'walkskyer'
"""
print response info
"""
import sys, urllib2
if __name__ == "__main__":

    req = urllib2.Request(sys.argv[1])
    fd = urllib2.urlopen(req)
    print "Retrieved", fd.geturl()
    for key, value in fd.info().items():
        print "%s = %s" % (key, value)