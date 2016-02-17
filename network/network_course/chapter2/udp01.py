# -*- coding:utf-8 -*-
__author__ = 'walkskyer'
"""
udp test
cmd:udp01.py host port
"""
import socket, sys

if __name__ == "__main__":
    host = sys.argv[1]
    textport = sys.argv[2]

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        port = int(textport)
    except ValueError, e:
        # That didn't work. Look it up instead.
        port = socket.getservbyname(textport, 'udp')

    s.connect((host, port))
    print "Enter data to transmit:"
    data = sys.stdin.readline().strip()
    s.sendall(data)
    print "Looking for replies; press Ctrl-C or Ctrl-Break to stop."

    while 1:
        buf = s.recv(2048)
        if not len(buf):
            break
        sys.stdout.write(buf)