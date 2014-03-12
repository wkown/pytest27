# -*- coding: utf-8 -*-
# filename:qthread.py
# datetime:2014-03-12 22:04
__author__ = 'walkskyer'
"""

"""

import sys
from PyQt4 import QtGui, QtCore
import time
import random


class MyThread(QtCore.QThread):
    #作用：trigger将是main与该thread交流的通道。
    # 其中int是这个通道中可以传输的数据类型，还可以用其他的类型，如QtCore.pyqtSignal(type(""))（通道可以传输string）。
    trigger = QtCore.pyqtSignal(int)

    def __init__(self, parent=None):
        super(MyThread, self).__init__(parent)

    def setup(self, thread_no):
        self.thread_no = thread_no

    def run(self):
        time.sleep(random.random()*50)  # random sleep to imitate working
        self.trigger.emit(self.thread_no)


class Main(QtGui.QMainWindow):
    def __init__(self, parent=None):
        super(Main, self).__init__(parent)
        self.text_area = QtGui.QTextBrowser()
        self.thread_button = QtGui.QPushButton('Start threads')
        self.thread_button.clicked.connect(self.start_threads)

        central_widget = QtGui.QWidget()
        central_layout = QtGui.QHBoxLayout()
        central_layout.addWidget(self.text_area)
        central_layout.addWidget(self.thread_button)
        central_widget.setLayout(central_layout)
        self.setCentralWidget(central_widget)

    def start_threads(self):
        self.threads = []              # this will keep a reference to threads
        for i in range(10):
            thread = MyThread(self)    # create a thread
            #作用：把trigger这个通道的出口连到update_text函数。
            thread.trigger.connect(self.update_text)  # connect to it's signal
            thread.setup(i)            # just setting up a parameter
            thread.start()             # start the thread
            self.threads.append(thread) # keep a reference

    def update_text(self, thread_no):
        """作用：实现update_text函数，这个例子里是把信息输出到一个文本框。"""
        self.text_area.append('thread # %d finished' % thread_no)

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)

    mainwindow = Main()
    mainwindow.show()

    sys.exit(app.exec_())
