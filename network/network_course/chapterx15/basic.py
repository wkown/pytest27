# -*- coding:utf-8 -*-
__author__ = 'walkskyer'
"""
Basic SSL example - chapter 15 - basic.py
"""
import socket, sys

def sendall(s, buf):
    byteswritten = 0
    while byteswritten < len(buf):
        byteswritten += s.write(buf[byteswritten:])

if __name__ == "__main__":
    print "Creating socket ..."
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print "done."

    print "Connecting to remote host..."
    s.connect(("github.com", 443))
    print "done."

    print "Establishing SSL..."
    ssl = socket.ssl(s)
    print "done."

    print "Requesting document..."
    sendall(ssl, "GET / HTTP/1.0\r\n\r\n")
    print "done."

    s.shutdown(1)

    while 1:
        try:
            buf = ssl.read(1024)
        except socket.sslerror, err:
            if (err[0]) in [socket.SSL_ERROR_ZERO_RETURN, socket.SSL_ERROR_EOF]:
                break
            elif (err[0]) in [socket.SSL_ERROR_WANT_READ, socket.SSL_ERROR_WANT_WRITE]:
                continue
            raise
        if len(buf) == 0:
            break

        sys.stdout.write(buf)
        s.close()
