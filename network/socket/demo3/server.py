# -*- coding:utf-8 -*-
__author__ = 'walkskyer'
"""
 udp 广播 server
"""
import socket
host=''
port=10000
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
s.setsockopt(socket.SOL_SOCKET,socket.SO_BROADCAST,1)
s.bind((host,port))
while 1:
    try:
        data,addr=s.recvfrom(1024)
        print "got data from",addr
        s.sendto("broadcasting",addr)
        print data
    except KeyboardInterrupt:
        raise