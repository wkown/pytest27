# -*- coding:utf-8 -*-
__author__ = 'walkskyer'
"""
print socket opt
"""
import socket

if __name__ == "__main__":
    solist = [ x for x in dir(socket) if x.startswith('SO_')]
    solist.sort()
    for x in solist:
        print x