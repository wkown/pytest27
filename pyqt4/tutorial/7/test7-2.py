# -*- coding: utf-8 -*-
# filename:test7-2.py
# datetime:2014-03-04 10:48
__author__ = 'walkskyer'
"""
QLineEdit
"""
from PyQt4 import QtGui
from PyQt4 import QtCore


class Example(QtGui.QWidget):
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()

    def initUI(self):
        self.label = QtGui.QLabel(self)
        edit = QtGui.QLineEdit(self)

        edit.move(60, 100)
        self.label.move(60, 40)

        self.connect(edit, QtCore.SIGNAL('textChanged(QString)'),
                     self.onChange)

        self.setWindowTitle('QLineEdit')
        self.setGeometry(250, 200, 350, 250)

    def onChange(self, text):
        self.label.setText(text)
        self.label.adjustSize()

if __name__ == "__main__":
    app = QtGui.QApplication([])
    exm = Example()
    exm.show()
    app.exec_()
