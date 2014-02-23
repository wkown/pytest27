# -*- coding:utf-8 -*-
# test2-1.py
__author__ = 'adminer'
"""
状态栏
"""

import sys
from PyQt4 import QtGui


class MainWindow(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)

        self.resize(250, 150)
        self.setWindowTitle('statusBar')

        self.statusBar().showMessage('Ready')

app = QtGui.QApplication(sys.argv)
main = MainWindow()
main.show()
sys.exit(app.exec_())