# -*- coding: utf-8 -*-
# filename:test6-5.py
# datetime:2014-03-03 22:03
__author__ = 'walkskyer'
"""
QCalendarWidget日历窗口组件
"""
import sys
from PyQt4 import QtGui, QtCore


class Example(QtGui.QWidget):
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Calendar')
        self.setGeometry(300, 300, 350, 300)

        self.cal = QtGui.QCalendarWidget(self)
        self.cal.setGridVisible(True)
        self.move(20, 20)
        self.connect(self.cal, QtCore.SIGNAL('selectionChanged()'), self.showDate)

        self.label = QtGui.QLabel(self)
        date = self.cal.selectedDate()
        self.label.setText(str(date.toPyDate()))
        self.label.move(130, 260)

    def showDate(self):
        date = self.cal.selectedDate()
        self.label.setText(str(date.toPyDate()))

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    ex.show()
    app.exec_()

