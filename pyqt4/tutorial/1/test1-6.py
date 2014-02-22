# -*- coding:utf-8 -*-
__author__ = 'adminer'
"""
屏幕居中显示窗体
"""
import sys
from PyQt4 import QtGui
import time


class Center(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)

        self.setWindowTitle('center')
        self.resize(250, 150)

    def center(self):
        screen = QtGui.QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width()-size.width())/2,
                  (screen.height()-size.height())/2)

app = QtGui.QApplication(sys.argv)
c = Center()
c.show()
time.sleep(5)
c.center()
sys.exit(app.exec_())