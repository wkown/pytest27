# -*- coding: utf-8 -*-
# test5-4.py
__author__ = 'adminer'
"""
QFileDialog
"""
import sys
from PyQt4 import QtGui, QtCore

class Example(QtGui.QMainWindow):
    def __init__(self):
        super(Example, self).__init__()

        self.initUI()

    def initUI(self):
        self.textEdit = QtGui.QTextEdit()
        self.setCentralWidget(self.textEdit)
        self.statusBar()
        self.setFocus()

        openFile = QtGui.QAction(QtGui.QIcon('open.png'), 'Open', self)
        openFile.setShortcut('Ctrl+O')
        openFile.setStatusTip('Open new File')
        self.connect(openFile, QtCore.SIGNAL('triggered()'), self.showDialog)

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(openFile)

        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('OpenFile')

    def showDialog(self):
        filename = QtGui.QFileDialog.getOpenFileName(self,
                                                     'Open file',
                                                     '/home')
        fname = open(filename)
        data = fname.read()
        #self.textEdit.append(data)
        self.textEdit.setText(data)

app = QtGui.QApplication(sys.argv)
ex = Example()
ex.show()
app.exec_()

