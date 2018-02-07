# -*- coding: utf-8 -*-
# filename:test6-3.py
# datetime:2014-03-03 20:46
__author__ = 'walkskyer'
"""
QSlider滑块
"""
import sys
from PyQt4 import QtGui, QtCore


class Example(QtGui.QWidget):
    def __init__(self):
        super(Example, self).__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Slide')
        self.setGeometry(300, 300, 250, 150)

        slider = QtGui.QSlider(QtCore.Qt.Horizontal, self)
        slider.setFocusPolicy(QtCore.Qt.NoFocus)
        slider.setGeometry(30, 40, 100, 30)
        self.connect(slider, QtCore.SIGNAL('valueChanged(int)'), self.changeValue)

        self.label = QtGui.QLabel(self)
        self.label.setPixmap(QtGui.QPixmap('audio-volume-muted.png'))
        self.label.setGeometry(160, 40, 80, 30)

    def changeValue(self, value):
        if value == 0:
            self.label.setPixmap(QtGui.QPixmap('audio-volume-muted.png'))
        elif value > 0 and value <=30:
            self.label.setPixmap(QtGui.QPixmap('audio-volume-low.png'))
        elif value > 30 and value <=60:
            self.label.setPixmap(QtGui.QPixmap('audio-volume-medium.png'))
        else:
            self.label.setPixmap(QtGui.QPixmap('audio-volume-high.png'))

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    ex.show()
    app.exec_()
