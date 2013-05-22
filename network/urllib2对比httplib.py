# -*- coding:utf8 -*-
__author__ = 'weijie'
'''一开始测试以为httplib比urllib2速度要快很多
后来发现写这个代码的人写错了。
把conn.request('GET', '/')写成了conn.request('get', '/')。
当然她测试的网址是：www.cnseay.com，当时速度差别很大很惊异，查看返回的内容时竟然是个404错误页面。难怪这么快！！！
代码来源:www.oschina.net/code/snippet_1011036_21490
'''
import time
print time.time()
import urllib2

response = urllib2.urlopen('http://www.baidu.com/')

print response.getcode()
a=response.read()
response.close()


print time.time()
import httplib
conn = httplib.HTTPConnection("www.baidu.com")
conn.request('GET', '/')

res = conn.getresponse()

print res.status
b=res.read()
conn.close()
print time.time()

#print a
print b