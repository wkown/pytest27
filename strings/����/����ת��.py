# -*- coding:utf-8 -*-
__author__ = 'walkskyer'
"""
用来批量处理文件编码转换。功能很简单，输入需要处理的文件类型，原始编码以及目标编码，以及目录即可开始工作。
"""
import os
import glob

class Encoding:
    def __init__(self):
        #文件扩展名
        self.ext = ".*"
        #编码
        self.srcEncoding=None
        self.dstEncoding=None

    def convertEncoding(self, content, srcEncoding=None, dstEncoding=None):
        return content.decode(self.srcEncoding).encode(self.dstEncoding)

    def processDirectory(self, args, dirname, filenames):
        print 'Directory', dirname
        for filename in filenames:
            if not os.path.isdir(dirname+'/'+filename):
                if filename.endswith(self.ext) or self.ext == ".*":
                    print ' File', filename
                    self.f2f(dirname+'/'+filename)

    def f2f(self, filepath, srcEncoding=None, dstEncoding=None):
        try:
            f1 = open(filepath, 'rb')
            temp = f1.read()
            f1.close()
            f2 = open(filepath, 'wb')
            f2.write(temp.decode(self.srcEncoding).encode(self.dstEncoding))
            f2.close()
            print '转码成功'
        except Exception, e:
            print e


    def colectFileType(self, dirname, fileType):
        for filename in glob.glob(r'*.'+fileType):
            print filename

    def setExt(self, ext):
        if not ext.startswith('.'):
            ext = "." + ext
        self.ext = ext

    def setSRC(self, encoding):
        self.srcEncoding=encoding

    def setDST(self, encoding):
        self.dstEncoding=encoding

if __name__ == '__main__':
    obj = Encoding()
    print u'请输入文件类型（如php或.php)：'
    obj.setExt(raw_input())
    print u'请输入文件原始编码：'
    obj.setSRC(raw_input())
    print u'请输入文件目标类型：'
    obj.setDST(raw_input())
    """obj.setExt('html')
    obj.setSRC('gbk')
    obj.setDST('utf-8')"""
    print u'请输入文件所在目录：'
    path = raw_input()
    os.path.walk(path, obj.processDirectory, None)