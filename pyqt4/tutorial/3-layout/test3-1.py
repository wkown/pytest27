# -*- coding:utf-8 -*-
# test3-2.py
__author__ = 'adminer'
"""
绝对定位
"""
import sys
from PyQt4 import QtGui


class Example(QtGui.QWidget):
    def __init__(self):
        super(Example, self).__init__()

        self.initUI()

    def initUI(self):
        label1 = QtGui.QLabel('Zetcode', self)
        label1.move(15, 10)

        label2 = QtGui.QLabel('tutorial for programmers', self)
        label2.move(35, 40)

        self.setWindowTitle('Absolute')
        self.resize(150, 150)

app = QtGui.QApplication(sys.argv)
ex = Example()
ex.show()
sys.exit(app.exec_())