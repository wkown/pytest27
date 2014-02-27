# -*- coding: utf-8 -*-
__author__ = 'adminer'
"""
测试webkit
"""
import sys
from PyQt4 import QtGui, QtCore, QtWebKit

app = QtGui.QApplication(sys.argv)

webView = QtWebKit.QWebView()
webView.load(QtCore.QUrl('http://subway.simba.taobao.com/#!/login'))
webView.show()

app.exec_()