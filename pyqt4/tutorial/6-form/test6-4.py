# -*- coding: utf-8 -*-
# filename:test6-4.py
# datetime:2014-03-03 21:27
__author__ = 'walkskyer'
"""
QProgressBar进度条
"""
import sys
from PyQt4 import QtGui, QtCore


class Example(QtGui.QWidget):
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('QProgressBar')
        self.setGeometry(300, 300, 250, 150)

        self.pbar = QtGui.QProgressBar(self)
        self.pbar.setGeometry(30, 40, 200, 25)

        self.button = QtGui.QPushButton('Start', self)
        self.button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.button.move(40, 80)
        self.connect(self.button, QtCore.SIGNAL('clicked()'),self.doActon)

        self.timer = QtCore.QBasicTimer()
        self.step = 0

    def timerEvent(self, event):
        if self.step>= 100:
            self.timer.stop()
            return
        self.step = self.step + 1
        self.pbar.setValue(self.step)

    def doActon(self):
        if self.timer.isActive():
            self.timer.stop()
            self.button.setText('Start')
        else:
            self.timer.start(100, self)
            self.button.setText('Stop')

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    ex.show()
    app.exec_()
