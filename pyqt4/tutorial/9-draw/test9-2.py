# -*- coding: utf-8 -*-
# filename:test9-2.py
# datetime:2014-03-06 12:02
__author__ = 'walkskyer'
"""
绘制点
"""
import sys, random
from PyQt4 import QtGui, QtCore


class Example(QtGui.QWidget):

    def __init__(self):
        super(Example, self).__init__()

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Points')

    def paintEvent(self, e):

        qp = QtGui.QPainter()
        qp.begin(self)
        self.drawPoints(qp)
        qp.end()

    def drawPoints(self, qp):

        qp.setPen(QtCore.Qt.red)
        size = self.size()

        for i in range(1000):
            x = random.randint(1, size.width()-1)
            y = random.randint(1, size.height()-1)
            qp.drawPoint(x, y)

app = QtGui.QApplication(sys.argv)
ex = Example()
ex.show()
app.exec_()
