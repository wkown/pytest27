# -*- coding:utf-8 -*-
__author__ = 'walkskyer'
"""
基本客户端操作 gopher
"""
import socket, sys

port = 70
host = sys.argv[1]
filename = sys.argv[2]

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

s.sendall(filename + "\r\n")

while 1:
    buf = s.recv(2048)
    if not len(buf):
        break
    sys.stdout.write(buf)

if __name__ == "__main__":
    pass