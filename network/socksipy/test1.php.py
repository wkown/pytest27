# -*- coding:utf-8 -*-
__author__ = 'walkskyer'
"""
"""
import win_inet_pton
import socks
import socket
import urllib2

proxy_address = raw_input('proxy address:')
if not proxy_address:
    proxy_address = '127.0.0.1:17000'

proxy_address = proxy_address.split(':')
print proxy_address
socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, proxy_address[0], int(proxy_address[1]))
socket.socket = socks.socksocket

if __name__ == "__main__":
    while True:
        url = raw_input('url:')
        if not url:
            continue
        try:
            resp = urllib2.urlopen('http://%s' % url)
            s = resp.read()
            print 'len:', len(s)
            print 'result:',s#[:200]
            print "\n"
        except Exception, e:
            print e