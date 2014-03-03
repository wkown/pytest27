# -*- coding: utf-8 -*-
# filename:test6-1.py
# datetime:2014-03-03 11:10
__author__ = 'walkskyer'
"""
QCheckBox 复选框
"""
import sys
from PyQt4 import QtGui, QtCore


class Example(QtGui.QWidget):
    def __init__(self):
        super(Example, self).__init__()

        self.initUI()

    def initUI(self):
        self.setGeometry(300,300,250,150)
        self.setWindowTitle('CheckBox')

        self.cb = QtGui.QCheckBox('Show title', self)
        self.cb.setFocusPolicy(QtCore.Qt.NoFocus)
        self.cb.move(10,10)
        self.cb.toggle()
        self.connect(self.cb, QtCore.SIGNAL('stateChanged(int)'),
                     self.changeTitle)

    def changeTitle(self, value):
        if self.cb.isChecked():
            self.setWindowTitle('Checkbox')
        else:
            self.setWindowTitle('')
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    ex.show()
    app.exec_()
