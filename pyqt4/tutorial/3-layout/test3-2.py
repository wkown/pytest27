# -*- coding:utf-8 -*-
# test3-2.py
__author__ = 'adminer'
"""
框布局
"""
import sys
from PyQt4 import QtGui


class Example(QtGui.QWidget):
    def __init__(self):
      super(Example, self).__init__()
      self.initUI()

    def initUI(self):
        okButton = QtGui.QPushButton("OK")
        cancelButton = QtGui.QPushButton("Cancel")

        hbox = QtGui.QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(okButton)
        hbox.addWidget(cancelButton)

        vbox = QtGui.QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)

        self.setLayout(vbox)
        self.setWindowTitle('box layout')
        self.resize(250, 150)

app = QtGui.QApplication(sys.argv)
ex = Example()
ex.show()
sys.exit(app.exec_())