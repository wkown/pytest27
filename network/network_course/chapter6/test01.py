# -*- coding:utf-8 -*-
__author__ = 'walkskyer'
"""
download web page
"""
import sys, urllib2
if __name__ == "__main__":

    req = urllib2.Request(sys.argv[1])
    fd = urllib2.urlopen(req)
    while 1:
        data = fd.read(1024)
        if not len(data):
            break
        sys.stdout.write(data)