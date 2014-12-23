# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window.ui'
#
# Created: Tue Dec 23 15:01:48 2014
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

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(403, 303)
        self.verticalLayoutWidget = QtGui.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 401, 301))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.save_path_edit = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.save_path_edit.setObjectName(_fromUtf8("save_path_edit"))
        self.horizontalLayout.addWidget(self.save_path_edit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_2 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_2.addWidget(self.label_2)
        self.pic_url_edit = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.pic_url_edit.setObjectName(_fromUtf8("pic_url_edit"))
        self.horizontalLayout_2.addWidget(self.pic_url_edit)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_3 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_3.addWidget(self.label_3)
        self.count_edit = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.count_edit.setObjectName(_fromUtf8("count_edit"))
        self.horizontalLayout_3.addWidget(self.count_edit)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.textEdit = QtGui.QTextEdit(self.verticalLayoutWidget)
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.verticalLayout.addWidget(self.textEdit)
        self.saveB = QtGui.QPushButton(self.verticalLayoutWidget)
        self.saveB.setObjectName(_fromUtf8("saveB"))
        self.verticalLayout.addWidget(self.saveB)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "保存图片", None))
        self.label.setText(_translate("Form", "目标目录", None))
        self.label_2.setText(_translate("Form", "图片地址", None))
        self.label_3.setText(_translate("Form", "图片索引", None))
        self.saveB.setText(_translate("Form", "保存", None))

