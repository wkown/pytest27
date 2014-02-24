# -*- coding: utf-8 -*-
# test4-1.py
__author__ = 'adminer'
"""
事件发送者
"""
import sys
from PyQt4 import QtGui, QtCore


class Example(QtGui.QMainWindow):
    def __init__(self):
        super(Example, self).__init__()

        self.initUI()

    def initUI(self):
        button1 = QtGui.QPushButton('Button 1', self)
        button1.move(30, 50)

        button2 = QtGui.QPushButton('Button 2', self)
        button2.move(150, 50)

        self.connect(button1, QtCore.SIGNAL('clicked()'),
                     self.buttonClicked)

        self.connect(button2, QtCore.SIGNAL('clicked()'),
                     self.buttonClicked)

        self.statusBar().showMessage('Ready')
        self.setWindowTitle('Event sender')
        self.resize(290, 150)

    def buttonClicked(self):
        sender = self.sender()
        self.statusBar().showMessage(sender.text() + ' was pressed')

app = QtGui.QApplication(sys.argv)
ex = Example()
ex.show()
sys.exit(app.exec_())