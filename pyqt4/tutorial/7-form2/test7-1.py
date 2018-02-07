# -*- coding: utf-8 -*-
# filename:test7-1.py
# datetime:2014-03-04 10:34
__author__ = 'walkskyer'
"""
QPixmap
"""

from PyQt4 import QtGui

class Example(QtGui.QWidget):
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()

    def initUI(self):
        hbox = QtGui.QHBoxLayout(self)
        pixmap = QtGui.QPixmap("rotunda.jpg")

        label = QtGui.QLabel(self)
        label.setPixmap(pixmap)

        hbox.addWidget(label)
        self.setLayout(hbox)

        self.setWindowTitle('Rotunda in Skalica')
        self.move(250, 200)

def main():

    app = QtGui.QApplication([])
    exm = Example()
    exm.show()
    app.exec_()

if __name__ == "__main__":
    main()
