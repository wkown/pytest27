#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
发送短信通知

使用此功能配置文件中需增加该配置
[sms]
appkey=appkey
secret=secret
sign_name=sign_name
template_code=template_code
"""
import util.op as op

if __name__ == "__main__":
    op.prepare_msg()
    op.send_msg()
