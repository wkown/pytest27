# -*- coding: utf-8 -*-
# test5-3.py
__author__ = 'adminer'
"""
QFontDialog
"""
import sys
from PyQt4 import QtGui, QtCore


class Example(QtGui.QWidget):
    def __init__(self):
        super(Example, self).__init__()

        self.initUI()

    def initUI(self):
        hbox = QtGui.QHBoxLayout()

        button = QtGui.QPushButton('dialog', self)
        button.setFocusPolicy(QtCore.Qt.NoFocus)
        button.move(20, 20)

        hbox.addWidget(button)

        self.connect(button, QtCore.SIGNAL('clicked()'),self.showDialog)

        self.label = QtGui.QLabel('Knowledge only matters', self)
        self.label.move(130, 20)

        hbox.addWidget(self.label)
        self.setLayout(hbox)

        self.setWindowTitle('FontDialog')
        self.setGeometry(300, 300, 250, 110)

    def showDialog(self):
        font, ok = QtGui.QFontDialog.getFont()
        if ok:
            self.label.setFont(font)

if __name__ == '__main__':

    app = QtGui.QApplication(sys.argv)
    ex = Example()
    ex.show()
    app.exec_()
