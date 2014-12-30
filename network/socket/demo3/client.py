# -*- coding:utf-8 -*-
__author__ = 'walkskyer'
"""
 udp 广播 client
"""
import socket,sys
addr=('<broadcast>',10000)
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET,socket.SO_BROADCAST,1)
s.sendto("hello from client",addr)
while 1:
    data=s.recvfrom(1024)
    if not data:
        break
    print data