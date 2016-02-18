# -*- coding:utf-8 -*-
__author__ = 'walkskyer'
"""
七牛上传文件测试 上传图片
"""
from qiniu import Auth
from qiniu import put_file, put_data, etag
import qiniu.config
if __name__ == "__main__":
    access_key = 'ttTgMAScydzGfjdhHKf2Bx6BN6JVUXzV3G4SC54B'
    secret_key = '5Chrb0yqHcXsNeXd2xwA7hxjZPhaBAfmesF3BvjA'
    bucket_name = 'test'

    q = Auth(access_key, secret_key)

    localfile = 'assets/0004.jpg'
    key = 'test/0001.jpg'
    mime_type = "image/jpeg"

    token = q.upload_token(bucket_name, key)
    ret, info = put_file(token, key, localfile, mime_type=mime_type, check_crc=True)
    print(info)
    assert ret['key'] == key
    assert ret['hash'] == etag(localfile)