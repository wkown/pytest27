# -*- coding: utf-8 -*-
# filename:clearComments.py
# datetime:2014-04-26 11:04
__author__ = 'walkskyer'
"""
去掉源代码中的注释
"""
import os
import glob
import re
import py_compile

class Compiler:
    def __init__(self):
        #文件扩展名
        self.ext = ".py"

        self.dist = '../dist'
        self.path = None
        #编码
        self.srcEncoding=None
        self.dstEncoding=None

    def convertEncoding(self, content, srcEncoding=None, dstEncoding=None):
        return content.decode(self.srcEncoding).encode(self.dstEncoding)

    def processDirectory(self, args, dirname, filenames):
        print self.path
        print 'Directory', dirname
        #return
        for filename in filenames:
            if not os.path.isdir(dirname+'/'+filename):
                if filename.endswith(self.ext) or self.ext == ".*":
                    print ' File', filename
                    self.toDist(dirname.replace(self.path, ''))
                    self.compile(dirname+'/'+filename)

    def compile(self, filepath):
        try:
            f1 = open(filepath, 'rb')
            temp = f1.read()
            f1.close()
            distFile = '%s/%s' % (self.dist, filepath.replace(self.path, ''))
            f2 = open(distFile, 'wb')
            f2.write(self.clearComment(filepath,temp))
            f2.close()
            print '成功'
        except Exception, e:
            print e

    def clearComment(self, filename, string):
        if filename.endswith('.php'):
            return self.clearCommentPHP(string)
        elif filename.endswith('.py'):
            return self.clearCommentPython(string)
        elif filename.endswith('.js'):
            return self.clearCommentJavaScript(string)
        elif filename.endswith('.xml') or filename.endswith('.html') or filename.endswith('.htm'):
            return self.clearCommentXml(string)
        return string

    def clearCommentPython(self, string):
        """
        清除注释
        """
        style1 = re.compile('""".*?"""', re.DOTALL)
        string = style1.sub('', string)

        style2 = re.compile("'''.*?'''", re.DOTALL)
        string = style2.sub('', string)

        replace1 = re.compile("# (-\*- .*? -\*-)\r\n")
        string = replace1.sub('{{{\\1}}}\r\n', string)

        #style3 = re.compile("^[ ]*?#.*?\r\n")
        #string = style3.sub('\r\n', string)

        replace1 = re.compile("{{{(.*?)}}}\r\n")
        string = replace1.sub('# \\1\r\n', string)

        return string

    def clearCommentPHP(self, string):
        style1 = re.compile('/\*.*?\*/', re.DOTALL)
        string = style1.sub('', string)

        """
        style3 = re.compile("//.*?\r\n")
        string = style3.sub('\r\n', string)
        """

        return string

    def clearCommentJavaScript(self, string, commpress=True):
        style1 = re.compile('/\*.*?\*/', re.DOTALL)
        string = style1.sub('', string)
        """
        style3 = re.compile("//.*?\r\n")
        string = style3.sub('\n', string)

        style3 = re.compile("//.*?\n")
        string = style3.sub('\n', string)
        """
        return string

    def clearCommentXml(self, string, commpress=True):
        style1 = re.compile('<!--.*?-->', re.DOTALL)
        string = style1.sub('', string)

        style1 = re.compile('/\*.*?\*/', re.DOTALL)
        string = style1.sub('', string)
        return string

    def toDist(self, dirname):
        """在目标目录创建文件夹"""
        if self.path is None:
            self.path = dirname
            dirname = ''
        if self.dist == '../dist':
            self.dist = '%s/%s' % (self.path, self.dist)
        if not os.path.isdir('%s/%s' % (self.dist, dirname)):
            os.mkdir('%s/%s' % (self.dist, dirname))

if __name__ == '__main__':

    print u'请输入一个目录：'
    path = raw_input()
    while not path:
        print u'请输入一个目录：'
        path = raw_input()

    obj = Compiler()
    obj.toDist(path)
    obj.ext = '.*'
    #path = raw_input()
    #path = '.'
    os.path.walk(path, obj.processDirectory, None)
