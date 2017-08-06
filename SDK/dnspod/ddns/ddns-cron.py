# !/usr/bin/env python
# -*- coding:utf-8 -*-

import httplib, urllib
import socket
import time
from common import *
import os
import sys
import json

print 'sys.path:', sys.path[0]

conf_file = '%s/conf.json' % sys.path[0]
if os.path.isfile('%s/conf-local.json' % sys.path[0]):
    conf_file = '%s/conf-local.json' % sys.path[0]

with open(conf_file, 'rb') as f:
    conf_str = f.read()
    f.close()

if conf_str == '':
    exit(0)

conf = json.loads(conf_str)

print conf
params = dict(
    #login_email=conf['account']['email'],  # replace with your email
    #login_password=conf['account']['password'],  # replace with your password
    login_token = conf['account']['login_token'],
    format="json",
    domain_id='',  # replace with your domain_od, can get it by API Domain.List
    record_id='',  # replace with your record_id, can get it by API Record.List
    sub_domain='',  # replace with your sub_domain
    record_line="默认",
)
"""
params = dict(
    login_email=raw_input("email:"),  # replace with your email
    login_password=raw_input("password:"),  # replace with your password
    format="json",
    domain_id=raw_input('domain_id:'),  # replace with your domain_od, can get it by API Domain.List
    record_id=raw_input('record_id:'),  # replace with your record_id, can get it by API Record.List
    sub_domain=raw_input('sub_domain:'),  # replace with your sub_domain
    record_line="默认",
)
"""

if __name__ == '__main__':
    try:
        ip = getip()
        print ip
        params['ip'] = ip
        for domain in conf['domains']:
            #print domain['full_domain'], ':', getdomainip(domain['full_domain'])
            if ip == getdomainip(domain['full_domain']):
                continue
            params['domain_id'] = domain['domain_id']
            params['record_id'] = domain['record_id']
            params['sub_domain'] = domain['sub_domain']
            ddns(params)
    except Exception, e:
        print e
        pass
    time.sleep(30)