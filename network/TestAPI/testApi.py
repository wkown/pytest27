# -*- coding:utf-8 -*-
import httplib
import urllib
import os
import json
import re

__author__ = 'walkskyer'
"""
api测试程序库
"""


class HttpClient:
    def __init__(self, *args, **kwargs):
        if kwargs.has_key('host'):
            self.host = kwargs['host']
        if self.host is not None:
            self.conn = httplib.HTTPConnection(self.host)
        self.response = None

    def post(self, url='', body={}, headers={}):
        return self.read("POST", url, body, headers)

    def get(self, url='', body={}, headers={}):
        return self.read("GET", url, body, headers)

    #read the respond content
    def read(self, method, url, body={}, headers={}):
        body = urllib.urlencode(body)
        if len(body) < 0:
            body = None

        self.conn.request(method, url, body, headers)
        try:
            self.response = self.conn.getresponse()
            if self.response.status == 200:
                return self.response.read()
        except httplib.ResponseNotReady, e:
            self.response = None
        return None

class ApiConfig:
    def __init__(self,filename):
        if os.path.isfile(filename):
            self.filename = filename
        self.config = None

        if self.filename:
            self.load_config()

    def load_config(self, filename=''):
        if filename is None or len(filename) == 0:
            filename = self.filename

        f = open(filename, 'rb')
        json_str = f.read()
        f.close()
        self.config = json.loads(re.sub('\/\*.*?\*\/', '', json_str))


if __name__ == "__main__":

    hc = HttpClient(host="webapp.zwj")
    print hc.post('/app/user/register')
    print hc.post('/app/user/login')

    ac = ApiConfig('./test_template/tpl_test.json')
    print ac.config