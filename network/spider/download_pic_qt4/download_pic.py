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
        QObject.connect(self.ui.select_dirB, SIGNAL('clicked()'), self.select_dir)

    def save_pic(self):
        save_path = self.ui.save_path_edit.text()
        save_path = unicode(save_path)
        if len(save_path) == 0:
            save_path = os.getcwd()
        count = int(str(self.ui.count_edit.text()))
        if count <= 0:
            count = 1

        filename = '%s/%04d' % (save_path, count)
        print 'the new file is: %s' % filename
        self.ui.textEdit.append('the new file is: %s' % filename)

        url = self.ui.pic_url_edit.text()
        if len(url) == 0:
            url = self.clipboard.text()

        flag = False
        if len(url) == 0:
            image = self.clipboard.image()
            if not image.isNull():
                image.save(filename + '.jpg', 'JPG')
                flag = True
        else:
            url = str(url)
            try:
                ext = url[url.rfind('.'):]
                f = open(filename.encode('gbk') + ext, 'wb')
                f.write(urllib.urlopen(url).read())
                f.close()
                flag = True
            except Exception, e:
                print e
                self.ui.textEdit.append(e)
                pass
        if flag:
            print 'the file %s was saved' % filename
            self.ui.textEdit.append('the file %s was saved' % filename)
            count += 1
            self.ui.count_edit.setText(str(count))

    def select_dir(self):
        selector = QtGui.QFileDialog.getExistingDirectory(self)
        print unicode(selector)
        self.ui.save_path_edit.setText(selector)



if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    ex = Widget()
    ex.show()
    sys.exit(app.exec_())
if __name__ == "__main__":
    pass