# -*- coding:utf-8 -*-
__author__ = 'walkskyer'
"""
 udp client
"""
import socket
addr=('127.0.0.1',10000)
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
while 1:
    data=raw_input('input data:')
    if not data:
        break
    s.sendto(data,addr)
    srv_data, address = s.recvfrom(2048)
    if srv_data:
        print 'srv reply:%s' % srv_data
        print 'srv address:',  address
s.close()