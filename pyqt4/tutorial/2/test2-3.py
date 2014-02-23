# -*- coding:utf-8 -*-
# test2-3.py
__author__ = 'adminer'
"""
工具栏
"""
import sys
from PyQt4 import QtGui, QtCore


class MainWindow(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)

        self.resize(250, 150)
        self.setWindowTitle('toolBar')

        self.exit = QtGui.QAction(QtGui.QIcon('exit.png'), 'Exit', self)
        self.exit.setShortcut('Ctrl+Q')
        self.exit.setStatusTip('Exit application')
        self.connect(self.exit, QtCore.SIGNAL('triggered()'),QtCore.SLOT('close()'))

        self.statusBar()

        self.toolbar = self.addToolBar('Exit')
        self.toolbar.addAction(self.exit)

app = QtGui.QApplication(sys.argv)
main = MainWindow()
main.show()
sys.exit(app.exec_())