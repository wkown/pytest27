# -*- coding:utf-8 -*-
__author__ = 'walkskyer'
"""这个程序提供了一个不需要正则解析url的方法。
来源地址http://www.oschina.net/code/snippet_1160609_27470
"""
import urllib
#读出一个URL下的a标签里href地址为.html的所有地址
def test1():
    content = urllib.urlopen('http://www.hoopchina.com').read()
    s1=0
    while s1>=0:
        begin = content.find(r'<a',s1)
        m1 = content.find(r'href=',begin)
        m2 = content.find(r'>',m1)
        if(content[m1:m2].find(r'.html')!=-1):
            m2 = content.find(r'.html',m1)
            url = content[m1+6:m2+5]
            print url
        s1=m2

"""下面这个是对上一个的演进版。
http://www.oschina.net/code/snippet_1390415_27567
"""
def test2():
    content = urllib.urlopen('http://www.leizhiping.cn').read()
    s1=0
    while s1>=0:
        begin = content.find(r'<a',s1)
        m1 = content.find(r'href=',begin)
        m2 = content.find(r'>',m1)

        s1 = m2
        if(begin<=0):
            break
        elif(content[m1:m2].find(r" ")!=-1):
            m2 = content[m1:m2].find(r' ')
            url = content[m1+6:m1+m2-1]
            print url
        elif m2>=0:
            url = content[m1+6:m2-1]
            print url
    print "end."
if __name__ == "__main__":
    test2()