# -*- coding: utf-8 -*-
# filename:test9-1.py
# datetime:2014-03-05 21:59
__author__ = 'walkskyer'
"""
绘制图像
这效果与7_1不同，它打印的图片可与控件共同放缩
"""
import sys
from PyQt4 import QtGui, QtCore


class Example(QtGui.QWidget):

    def __init__(self):
        super(Example, self).__init__()

        self.initUI()

    def initUI(self):

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Draw Text')
        self.image = '../7/rotunda.jpg'

    def paintEvent(self, event):

        qp = QtGui.QPainter()
        qp.begin(self)
        self.drawImage(event, qp)
        qp.end()

    def drawImage(self, event, qp):
        qp.drawImage(event.rect(), QtGui.QImage(self.image))

app = QtGui.QApplication(sys.argv)
ex = Example()
ex.show()
app.exec_()

