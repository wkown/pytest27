# -*- coding:utf-8 -*-
__author__ = 'walkskyer'
"""
图形版批量下载图片
"""
import sys
from PyQt4 import QtGui
from PyQt4.QtCore import *
from ui.window import Ui_Form
import urllib
import os


class Widget(QtGui.QWidget):
    def __init__(self):
        super(QtGui.QWidget, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.clipboard = QtGui.QApplication.clipboard()
        QObject.connect(self.ui.saveB, SIGNAL('clicked()'), self.save_pic)

    def save_pic(self):
        url = self.ui.pic_url_edit.text()
        if len(url) == 0:
            url = self.clipboard.text()
        url=str(url)
        count = int(str(self.ui.count_edit.text()))
        if count <= 0:
            count = 1

        save_path = self.ui.save_path_edit.text()
        save_path = unicode(save_path)
        if len(save_path) == 0:
            save_path = os.getcwd()
        try:
            filename = '%s/%04d' % (save_path, count)
            print 'the new file is: %s' % filename
            self.ui.textEdit.append('the new file is: %s' % filename)
            ext = url[url.rfind('.'):]
            f = open(filename.encode('gbk') + ext, 'wb')
            f.write(urllib.urlopen(url).read())
            f.close()
            print 'the file %s was saved' % filename
            self.ui.textEdit.append('the file %s was saved' % filename)
            count += 1
            self.ui.count_edit.setText(str(count))
        except Exception, e:
            print e
            self.ui.textEdit.append('the file %s was saved' % filename)
            pass


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    ex = Widget()
    ex.show()
    sys.exit(app.exec_())
if __name__ == "__main__":
    pass