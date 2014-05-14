# -*- coding: utf-8 -*-
# filename:test1.py
# datetime:2014-05-14 09:48
__author__ = 'walkskyer'
"""
简单的表格测试程序
http://blog.csdn.net/vah101/article/details/6215066
"""
from PyQt4.QtGui  import *
from PyQt4.QtCore import *
class MyDialog(QDialog):
    def __init__(self, parent=None):
        super(MyDialog, self).__init__(parent)
        self.MyTable = QTableWidget(4,3)
        self.MyTable.setHorizontalHeaderLabels([u'姓名',u'身高',u'体重'])

        newItem = QTableWidgetItem(u"松鼠")
        self.MyTable.setItem(0, 0, newItem)

        newItem = QTableWidgetItem("10cm")
        self.MyTable.setItem(0, 1, newItem)

        newItem = QTableWidgetItem("60g")
        self.MyTable.setItem(0, 2, newItem)

        layout = QHBoxLayout()
        layout.addWidget(self.MyTable)
        self.setLayout(layout)


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    myWindow = MyDialog()
    myWindow.show()
    sys.exit(app.exec_())
