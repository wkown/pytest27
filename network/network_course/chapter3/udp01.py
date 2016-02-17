# -*- coding:utf-8 -*-
__author__ = 'walkskyer'
"""

"""
import socket, traceback
if __name__ == "__main__":
    host = ''
    port = 51423

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((host, port))

    while 1:
        try:
            message, address = s.recvfrom(8192)
            print "Got data from:%s %s", (address, message)
            # Echo it back
            s.sendto(message, address)
        except(KeyboardInterrupt, SystemExit):
            raise
        except:
            traceback.print_exc()