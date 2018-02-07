# -*- coding: utf-8 -*-
# test4-1.py
__author__ = 'adminer'
"""
重新实现事件处理程序
"""
import sys
from PyQt4 import QtGui, QtCore


class Example(QtGui.QWidget):
    def __init__(self):
        super(Example, self).__init__()

        self.setWindowTitle('Escape')
        self.resize(250, 150)

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Escape:
            self.close()

app = QtGui.QApplication(sys.argv)
ex = Example()
ex.show()
sys.exit(app.exec_())