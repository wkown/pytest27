# -*- coding:utf-8 -*-
__author__ = 'walkskyer'
import socket, sys
"""

cmd: python gopher_02.py quux.org /
"""

if __name__ == "__main__":
    port = 70
    host = sys.argv[1]
    filename = sys.argv[2]

    s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    fd = s.makefile('rw', 0)

    for line in fd.readlines():
        sys.stdout.write(line)