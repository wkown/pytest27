# !/usr/bin/env python
# -*- coding:utf-8 -*-

import httplib, urllib
import socket

current_ip = None


def ddns(params):
    headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/json"}
    conn = httplib.HTTPSConnection("dnsapi.cn")
    conn.request("POST", "/Record.Ddns", urllib.urlencode(params), headers)

    response = conn.getresponse()
    print response.status, response.reason
    data = response.read()
    print data
    conn.close()
    return response.status == 200


def getip():
    sock = socket.create_connection(('ns1.dnspod.net', 6666))
    ip = sock.recv(16)
    sock.close()
    return ip

def getdomainip(domain):
    try:
        return socket.getaddrinfo(domain, None)[0][4][0]
    except Exception, e:
        print e
        return ''