# -*- coding:utf-8 -*-
__author__ = 'walkskyer'
"""
剪切板操作测试
"""
import sys
from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import *
from ui.ui import Ui_Form
import time


class Widget(QtGui.QWidget):
    def __init__(self):
        super(QtGui.QWidget, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.clipboard = QtGui.QApplication.clipboard()
        QObject.connect(self.ui.getClipboard, SIGNAL('clicked()'), self.getClipBoard)
        QObject.connect(self.ui.setClipboard, SIGNAL('clicked()'), self.setClipBoard)

    def getClipBoard(self):
        text = self.clipboard.text()
        lenoftext = len(text)
        image = self.clipboard.image()
        image_isNull= image.isNull()
        if not image_isNull:
            image_format= image.format()
        mimeData = self.clipboard.mimeData()
        mimeText = mimeData.text()
        print type(text)
        print text
        self.ui.textEdit.setText(text)

    def setClipBoard(self):
        self.clipboard.setText('hello' + str(time.time()))


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    ex = Widget()
    ex.show()
    sys.exit(app.exec_())