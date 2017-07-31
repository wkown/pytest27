# !/usr/bin/env python
# -*- coding:utf-8 -*-

import httplib, urllib
import socket
import time
from common import *

params = dict(
    login_email=raw_input("email:"),  # replace with your email
    login_password=raw_input("password:"),  # replace with your password
    format="json",
    domain_id=raw_input('domain_id:'),  # replace with your domain_od, can get it by API Domain.List
    record_id=raw_input('record_id:'),  # replace with your record_id, can get it by API Record.List
    sub_domain=raw_input('sub_domain:'),  # replace with your sub_domain
    record_line="默认",
)
current_ip = None

if __name__ == '__main__':
    while True:
        try:
            ip = getip()
            print ip
            if current_ip != ip:
                params['ip'] = ip
                if ddns(params):
                    current_ip = ip
        except Exception, e:
            print e
            pass
        time.sleep(30)