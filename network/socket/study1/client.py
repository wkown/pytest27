# -*- coding:utf-8 -*-
__author__ = 'walkskyer'
"""

"""
import socket
import time


if __name__ == "__main__":
    s = socket.socket(
    socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("127.0.0.1", 18080))
    count = 10
    for i in xrange(0, 10):
        s.send('hello%s' % i)
        try:
            print s.recv(1024)
        except socket.error, e:
            print e
    s.close()
