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

    def create_url(self, url, body={}):
        """create url with param"""
        if len(body) > 0:
            return "%s?%s" % (url, urllib.urlencode(body))
        return url


class ApiConfig:
    """ api config object
    """
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
        self.config = json.loads(re.sub('/\*.*?\*/', '', json_str))

    def get_item(self, url, group):
        if self.config['api'].has_key(group) and len(self.config['api'][group]['items']) > 0:
            for item in self.config['api'][group]['items']:
                if url == item['url']:
                    return ApiItem(item)
        return None

    def get_group(self,group):
        if self.config['api'].has_key(group):
            return self.config['api'][group]
        return None

    def get_common_config(self, key):
        if key in self.config:
            return self.config[key]
        return None

    def get_datatype(self):
        return tuple(self.get_common_config('dataType').split('|'))


class ApiItem:
    """ the group item
    """
    def __init__(self, item_conf):
        # interface name
        self.name = item_conf['name']
        # interface url
        self.url = item_conf['url']
        # param item
        self.postField = self.getField = {}
        if 'postField' in item_conf:
            self.postField = item_conf['postField']
        if 'getField' in item_conf:
            self.getField = item_conf['getField']

        # item dataType
        self.dataType = item_conf['dataType']
        # item return data
        self.returnData = item_conf['returnData']


if __name__ == "__main__":

    #hc = HttpClient(host="webapp.zwj")
    #print hc.post('/app/user/register')
    #print hc.post('/app/user/login')

    ac = ApiConfig('./test_template/tpl_test.json')
    print ac.config
    print ac.get_common_config('host')
    print ac.get_datatype()
    print ac.get_group('app')
    item = ac.get_item('/app/user/register', 'app')
    print item
    print item.url
    print item.name
    print item.dataType
    print item.postField
    print item.getField
