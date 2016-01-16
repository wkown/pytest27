# -*- coding:utf-8 -*-
__author__ = 'walkskyer'
"""

"""
from lxml import etree
from lxml.html import fromstring
import urllib
if __name__ == "__main__":
    htmlContent = urllib.urlopen('file:test.html').read()
    htmlContent.decode('utf-8')
    tree = fromstring(htmlContent)
    print type(tree)
    #获取所有匹配a的元素
    print [etree.tostring(e) for e in tree.cssselect('a')]

    #更加精确
    s_tab_a = tree.cssselect('div#s_tab a')
    #打印所有匹配元素的文本
    print [etree.tostring(e) for e in s_tab_a]
    #元素的所有属性的键值对
    print [e.items() for e in s_tab_a]
    #获取特定属性
    print [e.get('href') for e in s_tab_a]
    #获取元素的text
    print ' '.join([e.text for e in s_tab_a])

    print '================================'
    #另一个测试
    qrcode_text = tree.cssselect('.qrcode-text')
    #打印所有匹配元素的文本
    print [etree.tostring(e) for e in qrcode_text]
    for ex in  [e for e in qrcode_text]:
        print '%s %s' % (etree.tostring(ex), [etree.tostring(x) for x in ex])