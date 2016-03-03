# -*- coding:utf-8 -*-
__author__ = 'walkskyer'
"""
Basic OpenSSL example - chapter 15 - osslbasic.py
"""
import socket, sys
from OpenSSL import SSL

if __name__ == "__main__":
    # Create SSL context object
    ctx = SSL.Context(SSL.SSLv23_METHOD)

    print "Create socket ..."
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print "done."

    # Create SSL connection object
    ssl = SSL.Connection(ctx, s)

    print "Establishing SSL..."
    ssl.connect(('www.python.org', 443))
    print "done."

    print "Requsting document...",
    ssl.sendall("GET / HTTP/1.0\r\nHost:www.python.org\r\n\r\n")
    print "done."

    while 1:
        try:
            buf = ssl.recv(4096)
        except SSL.ZeroReturnError:
            break
        sys.stdout.write(buf)

    ssl.close()