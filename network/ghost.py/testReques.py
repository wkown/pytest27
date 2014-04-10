# -*- coding: utf-8 -*-
# filename:testReques.py
# datetime:2014-04-10 16:15
__author__ = 'walkskyer'
"""
测试ghost的get和post请求
"""
from ghost import Ghost
import urllib

if __name__ == "__main__":
    g = Ghost()
    url = 'http://test.zwj/request/request.php'
    #没有任何请求参数
    g.open(url)
    print g.content

    #get
    data = {'a': 1, 'b': 2}
    g.open(url + '?' + urllib.urlencode(data))
    print g.content

    #post
    data = {'a': 1, 'b': 2}
    g.open(url, 'post', {}, None, urllib.urlencode(data))
    print g.content
