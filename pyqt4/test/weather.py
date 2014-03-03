# -*- coding: cp936 -*-
# filename:weather.py
# datetime:2014-03-03 11:13
__author__ = 'walkskyer'
"""
半透明的简单的天气预报。。
"""
import sys
import urllib2
import json
from PyQt4 import QtCore, QtGui


class MyWindow(QtGui.QLCDNumber, QtGui.QWidget):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)

        self.setWindowTitle("weather")
        self.resize(100, 40)
        self.setNumDigits(0)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setWindowOpacity(0.5)
        url = 'http://m.weather.com.cn/data/101090502.html'
        re = urllib2.urlopen(url).read()
        we = json.loads(re)['weatherinfo']
        label1 = QtGui.QLabel(we['city'])
        label2 = QtGui.QLabel(we['date'])
        label3 = QtGui.QLabel(we['week'])
        label4 = QtGui.QLabel(we['temp1'])
        label5 = QtGui.QLabel(we['weather1'])
        #---------添加表格布局
        gridLayout = QtGui.QGridLayout()

        gridLayout.addWidget(label1, 0, 0)
        gridLayout.addWidget(label2, 0, 1)
        gridLayout.addWidget(label3, 0, 2)
        gridLayout.addWidget(label4, 0, 3)
        gridLayout.addWidget(label5, 0, 4)

        self.setLayout(gridLayout)

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.dragPosition = event.globalPos() - self.frameGeometry().topLeft()
            event.accept()
        if event.button() == QtCore.Qt.RightButton:
            self.close()

    def mouseMoveEvent(self, event):
        if event.buttons() & QtCore.Qt.LeftButton:
            self.move(event.globalPos() - self.dragPosition)
            event.accept()


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    demo = MyWindow()
    demo.show()
    app.exec_()
