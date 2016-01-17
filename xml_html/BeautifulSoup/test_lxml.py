# -*- coding:utf-8 -*-
__author__ = 'walkskyer'
from bs4 import BeautifulSoup

"""
测试 bs4使用lxml解析器
"""

if __name__ == "__main__":
    f = open('../lxml/lxml.html/test.html')
    soup = BeautifulSoup(f.read(),'lxml')
    f.close()
    print soup.select('a')
    print type(soup.builder)