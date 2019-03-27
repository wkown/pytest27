# coding=utf8
__author__ = 'weijie'
'''
爬oschina的jquery文档
来源网址:http://www.oschina.net/code/snippet_100281_20482
'''
import urllib
import re


def getHtml(url, filepath):
    print 'getting the ' + url
    page = urllib.urlopen(url)
    html = page.read()
    page.close()
    file = url[len('http://www.ostools.net/uploads/apidocs/jquery/'):]
    if file == '':
        file = 'index.html'
        #print file
    file = repr(file)
    #print file[1:-1]
    fileHandle = open(filepath + file[1:-1], 'w')
    fileHandle.write(html)
    fileHandle.close()
    print 'getted the ' + url
    return html


def getSubFile(html):
    reg = '<a href=".*.html">'
    fileList = re.compile(reg).findall(html)
    return fileList


filepath = 'D:/jquery/'
html = getHtml('http://www.ostools.net/uploads/apidocs/jquery', filepath)
#print html
fileList = getSubFile(html)
#print fileList
for file in fileList:
    #print file[9:-2]
    getHtml('http://www.ostools.net/uploads/apidocs/jquery/' + file[9:-2], filepath)