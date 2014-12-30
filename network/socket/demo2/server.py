# -*- coding:utf-8 -*-
__author__ = 'walkskyer'
"""
 udp server
"""

import socket
address=('127.0.0.1',10000)
sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.bind(address)
clients=set()
while 1:
    data, addr=sock.recvfrom(2048)
    clients.add(addr)
    if not data:
        break
    print "got data from",addr
    msg='rec:%s' % data
    print msg
    for i in clients:
        print 'will send to:',i
        sock.sendto(msg, i)

sock.close()