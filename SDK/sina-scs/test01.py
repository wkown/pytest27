# -*- coding:utf-8 -*-
__author__ = 'walkskyer'
"""

"""
from sinastorage.bucket import SCSBucket
import sinastorage
if __name__ == "__main__":
    accesskey = '1ejzfhbkgyCTyFbzfFiL'
    sccretkey = 'SINA0000000001EJZFHB'
    #设置access_key,secret_key
    sinastorage.setDefaultAppInfo(accesskey, sccretkey)
    s = SCSBucket('wk-test',secure=True) # secure=True 采用https访问方式
    print s

    #文件内容
    # scsResponse = s.put('test.txt',u'hello world!')
    # print scsResponse

    #文件路径
    localfile = 'assets/0004.jpg'
    scsResponse1 = s.putFile('test.jpg', localfile)
    print scsResponse1