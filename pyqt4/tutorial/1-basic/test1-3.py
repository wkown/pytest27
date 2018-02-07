# -*- coding:utf-8 -*-
__author__ = 'adminer'
# test1-3.py
"""
显示工具提示
"""

import sys
from PyQt4 import QtGui
from PyQt4 import QtCore


class Tooltip(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)

        self.setGeometry(300, 300, 250, 250)
        self.setWindowTitle('Tooltip')

        self.setToolTip('This is a <b>QWidget</b> widget')
        #因为默认的 QToolTip 字体太难看，我们改变了它。
        QtGui.QToolTip.setFont(QtGui.QFont('oldEnglish', 10))

app = QtGui.QApplication(sys.argv)
tooltip = Tooltip()
tooltip.show()
sys.exit(app.exec_())