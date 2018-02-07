# -*- coding:utf-8 -*-
__author__ = 'walkskyer'
"""
测试命令: python test01.py http://www.baidu.com
"""
import sys
from PyQt4.QtWebKit import QWebView
from PyQt4.QtGui import QApplication
from PyQt4.QtCore import QUrl

if __name__ == "__main__":
    app = QApplication(sys.argv)
    browser = QWebView()
    browser.load(QUrl(sys.argv[1]))
    browser.show()

    app.exec_()