# -*- coding: utf8 -*-
__author__ = 'weijie'
'''mechanize的示例代码'''
import mechanize
import cookielib

br = mechanize.Browser()
cj = cookielib.LWPCookieJar()
br.set_cookiejar(cj)

# Browser options
br.set_handle_equiv(True)
br.set_handle_gzip(True)
br.set_handle_redirect(True)
br.set_handle_referer(True)
br.set_handle_robots(False)#这个是设置对方网站的robots.txt是否起作用。
# Follows refresh 0 but not hangs on refresh > 0
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
br.addheaders = [('User-agent',
                  'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]#还可以设置ip信息伪造来路

fp = br.open(u'http://www.baidu.com')
br.select_form(name='f')
br.form['wd'] = 'python' #输入关键字
br.submit() #提交表单
print br.response().read()
