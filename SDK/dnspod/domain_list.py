# -*- coding:utf-8 -*-
__author__ = 'walkskyer'
import httplib, urllib
import socket
import time
import json

params = dict(
    login_email=raw_input("email:"),  # replace with your email
    login_password=raw_input("password:"),  # replace with your password
    format="json",
)

def domain_list():
    headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/json"}
    conn = httplib.HTTPSConnection("dnsapi.cn")
    conn.request("POST", "/Domain.List", urllib.urlencode(params), headers)
    response = conn.getresponse()
    print response.status, response.reason
    data = response.read()
    print data
    conn.close()
    return response.status == 200

def recorder_list(domain_id):
    headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/json"}
    conn = httplib.HTTPSConnection("dnsapi.cn")
    params['domain_id'] = domain_id
    conn.request("POST", "/Record.List", urllib.urlencode(params), headers)
    response = conn.getresponse()
    print response.status, response.reason
    data = response.read()
    print data
    conn.close()
    return response.status == 200


if __name__ == "__main__":
    domain_list()

    domain_id = raw_input('domain_id:')
    recorder_list(domain_id)