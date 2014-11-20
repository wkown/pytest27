# -*- coding:utf-8 -*-
__author__ = 'walkskyer'
"""
根据指定索引将要下载的图片保存在save_path中,文件名已从count开始。
"""
import urllib
import os

save_path = raw_input('save path:')
try:
    os.chdir(save_path)
except Exception, e:
    # print e
    #在windows中打开中文目录需要将字符集转换为gbk
    os.chdir(save_path.decode('utf-8').encode('gbk'))
print os.getcwd()

count = int(raw_input('filename index:'))
while 1:
    filename = '%04d.jpg' % count
    print 'the new file is: %s' % filename
    url = raw_input('pic url:')
    f = open(filename, 'wb')
    f.write(urllib.urlopen(url).read())
    f.close()
    print 'the new file %s was saved:' % filename
    count += 1

if __name__ == "__main__":
    pass