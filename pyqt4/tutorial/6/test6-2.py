# -*- coding: utf-8 -*-
# filename:test6-2.py
# datetime:2014-03-03 11:36
__author__ = 'walkskyer'
"""
切换按钮
"""
import sys
from PyQt4 import QtGui, QtCore


class Example(QtGui.QWidget):
    def __init__(self):
        super(Example, self).__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('ToggleButton')
        self.setGeometry(300,300,280,170)

        self.color = QtGui.QColor(0, 0, 0)

        self.red = QtGui.QPushButton('Red', self)
        self.red.setCheckable(True)
        self.red.move(10, 10)
        self.connect(self.red, QtCore.SIGNAL('clicked()'), self.setColor)

        self.green = QtGui.QPushButton('Green', self)
        self.green.setCheckable(True)
        self.green.move(10, 60)
        self.connect(self.green, QtCore.SIGNAL('clicked()'), self.setColor)

        self.blue = QtGui.QPushButton('Blue', self)
        self.blue.setCheckable(True)
        self.blue.move(10, 110)
        self.connect(self.blue, QtCore.SIGNAL('clicked()'), self.setColor)

        self.square = QtGui.QWidget(self)
        self.square.setGeometry(150, 20, 100, 100)
        self.square.setStyleSheet("QtWidget{background-color: %s }" %
                                  self.color.name())

    def setColor(self):
        source = self.sender()
        if source.text() == "Red":
            if self.red.isChecked():
                self.color.setRed(255)
            else: self.color.setRed(0)

        elif source.text() == "Green":
            if self.green.isChecked():
                self.color.setGreen(255)
            else: self.color.setGreen(0)

        else:
            if self.blue.isChecked():
                self.color.setBlue(255)
            else: self.color.setBlue(0)

        self.square.setStyleSheet("QWidget { background-color: %s }" %
                                  self.color.name())

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    ex.show()
    app.exec_()

