# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calculator.ui'
#
# Created: Tue Dec 09 15:00:34 2014
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(400, 300)
        self.numB_1 = QtGui.QPushButton(Dialog)
        self.numB_1.setGeometry(QtCore.QRect(110, 100, 31, 23))
        self.numB_1.setObjectName(_fromUtf8("numB_1"))
        self.numB_2 = QtGui.QPushButton(Dialog)
        self.numB_2.setGeometry(QtCore.QRect(150, 100, 31, 23))
        self.numB_2.setObjectName(_fromUtf8("numB_2"))
        self.numB_3 = QtGui.QPushButton(Dialog)
        self.numB_3.setGeometry(QtCore.QRect(190, 100, 31, 23))
        self.numB_3.setObjectName(_fromUtf8("numB_3"))
        self.numB_4 = QtGui.QPushButton(Dialog)
        self.numB_4.setGeometry(QtCore.QRect(110, 130, 31, 23))
        self.numB_4.setObjectName(_fromUtf8("numB_4"))
        self.numB_5 = QtGui.QPushButton(Dialog)
        self.numB_5.setGeometry(QtCore.QRect(150, 130, 31, 23))
        self.numB_5.setObjectName(_fromUtf8("numB_5"))
        self.numB_6 = QtGui.QPushButton(Dialog)
        self.numB_6.setGeometry(QtCore.QRect(190, 130, 31, 23))
        self.numB_6.setObjectName(_fromUtf8("numB_6"))
        self.numB_7 = QtGui.QPushButton(Dialog)
        self.numB_7.setGeometry(QtCore.QRect(110, 160, 31, 23))
        self.numB_7.setObjectName(_fromUtf8("numB_7"))
        self.numB_8 = QtGui.QPushButton(Dialog)
        self.numB_8.setGeometry(QtCore.QRect(150, 160, 31, 23))
        self.numB_8.setObjectName(_fromUtf8("numB_8"))
        self.numB_9 = QtGui.QPushButton(Dialog)
        self.numB_9.setGeometry(QtCore.QRect(190, 160, 31, 23))
        self.numB_9.setObjectName(_fromUtf8("numB_9"))
        self.numB_0 = QtGui.QPushButton(Dialog)
        self.numB_0.setGeometry(QtCore.QRect(110, 190, 31, 23))
        self.numB_0.setObjectName(_fromUtf8("numB_0"))
        self.eqB = QtGui.QPushButton(Dialog)
        self.eqB.setGeometry(QtCore.QRect(150, 190, 71, 23))
        self.eqB.setObjectName(_fromUtf8("eqB"))
        self.symbolB = QtGui.QPushButton(Dialog)
        self.symbolB.setGeometry(QtCore.QRect(230, 100, 31, 23))
        self.symbolB.setObjectName(_fromUtf8("symbolB"))
        self.symbolB_2 = QtGui.QPushButton(Dialog)
        self.symbolB_2.setGeometry(QtCore.QRect(230, 130, 31, 23))
        self.symbolB_2.setObjectName(_fromUtf8("symbolB_2"))
        self.symbolB_3 = QtGui.QPushButton(Dialog)
        self.symbolB_3.setGeometry(QtCore.QRect(230, 160, 31, 23))
        self.symbolB_3.setObjectName(_fromUtf8("symbolB_3"))
        self.symbolB_4 = QtGui.QPushButton(Dialog)
        self.symbolB_4.setGeometry(QtCore.QRect(230, 190, 31, 23))
        self.symbolB_4.setObjectName(_fromUtf8("symbolB_4"))
        self.lineEdit = QtGui.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(40, 20, 321, 51))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.numB_1.setText(_translate("Dialog", "1", None))
        self.numB_2.setText(_translate("Dialog", "2", None))
        self.numB_3.setText(_translate("Dialog", "3", None))
        self.numB_4.setText(_translate("Dialog", "4", None))
        self.numB_5.setText(_translate("Dialog", "5", None))
        self.numB_6.setText(_translate("Dialog", "6", None))
        self.numB_7.setText(_translate("Dialog", "7", None))
        self.numB_8.setText(_translate("Dialog", "8", None))
        self.numB_9.setText(_translate("Dialog", "9", None))
        self.numB_0.setText(_translate("Dialog", "0", None))
        self.eqB.setText(_translate("Dialog", "=", None))
        self.symbolB.setText(_translate("Dialog", "+", None))
        self.symbolB_2.setText(_translate("Dialog", "-", None))
        self.symbolB_3.setText(_translate("Dialog", "*", None))
        self.symbolB_4.setText(_translate("Dialog", "/", None))

