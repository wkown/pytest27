#coding:utf-8
"""在一个qq群里下载的万能编码工具,这个工具是用来将其他编码转换为gbk。
还可以将这个工具的功能进行扩展，转换为自定编码"""
import urllib2


def getCodeStr(result):
    #gb2312    
    try:
        myResult = result.decode('gb2312').encode('gbk', 'ignore')
        return myResult
    except:
        pass
        #utf-8
    try:
        myResult = result.decode('utf-8').encode('gbk', 'ignore')
        return myResult
    except:
        pass

    #unicode
    try:
        myResult = result.encode('gbk', 'ignore')
        return myResult
    except:
        pass
        #gbk
    try:
        myResult = result.decode('gbk').encode('gbk', 'ignore')
        return myResult
    except:
        pass
        #big5
    try:
        myResult = result.decode('big5').encode('gbk', 'ignore')
        return myResult
    except:
        pass


    #m=u"中国"   #uncode编码的

#m=u"中国".encode('gbk')  #gbk编码的
#m=urllib2.urlopen("http://www.baidu.com").read()  #utf-8编码的
#m=urllib2.urlopen("http://www.qq.com").read()  #gb2312编码的
m = urllib2.urlopen("http://dir.twseo.org").read()  #big5编码的
print getCodeStr(m)