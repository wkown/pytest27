# -*- coding:utf-8 -*-
__author__ = 'walkskyer'
"""
七牛上传文件测试
"""
from qiniu import Auth
from qiniu import put_file, put_data, etag
import qiniu.config
if __name__ == "__main__":
    access_key = 'ttTgMAScydzGfjdhHKf2Bx6BN6JVUXzV3G4SC54B'
    secret_key = '5Chrb0yqHcXsNeXd2xwA7hxjZPhaBAfmesF3BvjA'
    bucket_name = 'test'

    q = Auth(access_key, secret_key)

    # 直接上传二进制流

    key = u'a\\b\\c"你好'
    data = u'hello bubby!'
    token = q.upload_token(bucket_name)
    ret, info = put_data(token, key, data)
    #print info
    assert ret['key'] == key

    key = ''
    data = 'hello bubby!'
    token = q.upload_token(bucket_name, key)
    ret, info = put_data(token, key, data, mime_type="application/octet-stream", check_crc=True)
    print(info)
    assert ret['key'] == key

    # 上传本地文件

    localfile = __file__
    key = 'test_file'
    mime_type = "text/plain"
    params = {'x:a': 'a'}

    token = q.upload_token(bucket_name, key)
    ret, info = put_file(token, key, localfile, mime_type=mime_type, check_crc=True)
    print(info)
    assert ret['key'] == key
    assert ret['hash'] == etag(localfile)

    # ret是一个字典，含有hash，key等信息。
    #
    # 断点续上传、分块并行上传
    #
    # 除了基本的上传外，七牛还支持你将文件切成若干块（除最后一块外，每个块固定为4M大小），每个块可独立上传，互不干扰；每个分块块内则能够做到断点上续传。
    #
    # 我们来看支持了断点上续传、分块并行上传的基本样例：

    q = Auth(access_key, secret_key)

    mime_type = "text/plain"
    params = {'x:a': 'a'}
    localfile = '.../.../...'

    key = 'big'
    token = q.upload_token(bucket_name, key)

    progress_handler = lambda progress, total: progress
    ret, info = put_file(token, key, localfile, params, mime_type, progress_handler=progress_handler)
    print(info)
    assert ret['key'] == key