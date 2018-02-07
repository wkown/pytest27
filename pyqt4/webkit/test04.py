# -*- coding:utf-8 -*-
__author__ = 'walkskyer'
"""
"""
import sys
from PyQt4.QtGui import QApplication
from PyQt4.QtCore import QUrl
from PyQt4.QtWebKit import QWebView, QWebPage
from PyQt4.QtNetwork import QNetworkAccessManager, QNetworkRequest
from PyQt4.QtGui import QGridLayout, QLineEdit, QWidget,QTableWidget, QTableWidgetItem, QHeaderView

class UrlInput(QLineEdit):
    def __init__(self, browser):
        super(UrlInput, self).__init__()
        self.broswer = browser
        self.returnPressed.connect(self._return_pressed)

    def _return_pressed(self):
        url = QUrl(self.text())

        self.broswer.load(url)

class RequestsTable(QTableWidget):
    header = ["url", "status", "content-type"]

    def __init__(self):
        super(RequestsTable, self).__init__()
        self.setColumnCount(3)
        self.setHorizontalHeaderLabels(self.header)
        header = self.horizontalHeader()
        header.setStretchLastSection(True)
        header.setResizeMode(QHeaderView.ResizeToContents)

    def update(self, data):
        last_row = self.rowCount()
        next_row = last_row + 1
        self.setRowCount(next_row)
        for col, dat in enumerate(data, 0):
            if not dat:
                continue
            self.setItem(last_row, col, QTableWidgetItem(dat))

class Manager(QNetworkAccessManager):
    def __init__(self, table):
        QNetworkAccessManager.__init__(self)
        # add event listener on "load finished" event
        self.finished.connect(self._finished)
        self.table = table

    def _finished(self, reply):
        """Update table with headers, status code and url.
        """
        headers = reply.rawHeaderPairs()
        headers = {str(k):str(v) for k,v in headers}
        content_type = headers.get("Content-Type")
        url = reply.url().toString()
        # getting status is bit of a pain
        status = reply.attribute(QNetworkRequest.HttpStatusCodeAttribute)
        status, ok = status.toInt()
        self.table.update([url, str(status), content_type])

class JavaScriptEvaluator(QLineEdit):
    def __init__(self, page):
        super(JavaScriptEvaluator, self).__init__()
        self.page = page
        self.returnPressed.connect(self._return_pressed)

    def _return_pressed(self):
        frame = self.page.currentFrame()
        result = frame.evaluateJavaScript(self.text())
if __name__ == "__main__":
    app = QApplication(sys.argv)

    grid = QGridLayout()
    browser = QWebView()
    url_input = UrlInput(browser)

    requests_table = RequestsTable()

    manager = Manager(requests_table)
    # to tell browser to use network access manager
    # you need to create instance of QWebPage
    page = QWebPage()
    page.setNetworkAccessManager(manager)
    browser.setPage(page)

    js_eval = JavaScriptEvaluator(page)

    grid.addWidget(url_input, 1, 0)
    grid.addWidget(browser, 2, 0)
    grid.addWidget(requests_table, 3, 0)
    grid.addWidget(js_eval, 4, 0)

    main_frame = QWidget()
    main_frame.setLayout(grid)
    main_frame.show()

    sys.exit(app.exec_())