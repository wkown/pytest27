# -*- coding:utf-8 -*-
__author__ = 'walkskyer'
"""
test1
"""
from lxml import etree
import urllib
from io import StringIO, BytesIO
if __name__ == "__main__":
    xml = '<a xmlns="test"><b xmlns="test"/></a>'
    root = etree.fromstring(xml)
    print etree.tostring(root)

    html = urllib.urlopen('http://www.baidu.com').read()
    html = html.decode('utf-8')
    parser = etree.HTMLParser()
    htmlTree = etree.parse(StringIO(html),parser=parser)
    print etree.tostring(htmlTree.getroot(),pretty_print=True,method="html")
