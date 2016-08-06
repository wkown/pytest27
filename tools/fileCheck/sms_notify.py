#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
发送短信通知
"""
import util.op as op

if __name__ == "__main__":
    op.prepare_msg()
    op.send_msg()
