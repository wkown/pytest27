# -*- coding:utf-8 -*-
__author__ = 'walkskyer'
"""
"""
import socks
import socket
import urllib
socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, "127.0.0.1", 16000)
socket.socket = socks.socksocket

if __name__ == "__main__":
    while True:
        url = raw_input('url:')
        if not url:
            continue
        try:
            resp = urllib.urlopen('http://%s' % url)
            print 'result:',resp.read()[:200]
            print "\n"
        except Exception, e:
            print e