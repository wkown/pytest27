# -*- coding:utf-8 -*-
__author__ = 'walkskyer'
"""
severt test 01 - Chapter 1 - simple test use telnet
cmd: telnet localhost 51423
"""
import socket

host = ''
port = 51423

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SOCK_STREAM, 1)
s.bind((host, port))
s.listen(1)

print "server is runing on port %d; press ctrl-c to terminate." % port

while 1:
    clientsock, clientaddr = s.accept()
    clientfile = clientsock.makefile('rw', 0)
    clientfile.write("welcome, " + str(clientaddr) + "\n")
    clientfile.write("Pleate enter a string: ")
    line = clientfile.readline().strip()
    clientfile.write("You entered %d characters.\n" % len(line))
    clientfile.close()
    clientsock.close()

if __name__ == "__main__":
    pass