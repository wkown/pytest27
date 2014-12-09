# -*- coding:utf-8 -*-
__author__ = 'walkskyer'
"""

"""
import sys
from PyQt4 import QtCore, QtGui
from ui.calculator import Ui_Dialog


class Dialog(QtGui.QDialog):
    def __init__(self):
        super(Dialog, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        for i, v in self.ui.__dict__.items():
            if isinstance(v, QtGui.QPushButton):
                self.connect(self.ui.__dict__[i], QtCore.SIGNAL('clicked()'), self.onButtonClick);
        self.ui.retranslateUi(self)

    def onButtonClick(self):
        value = self.sender().text()
        if value != '=':
            if str(self.ui.lineEdit.text()).find('=') > 0:
                self.ui.lineEdit.setText('')
            self.ui.lineEdit.setText(self.ui.lineEdit.text() + value)
        else:
            expression = str(self.ui.lineEdit.text())
            self.ui.lineEdit.setText(self.ui.lineEdit.text() + value + str(eval(expression)))


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    ex = Dialog()
    ex.show()
    sys.exit(app.exec_())
