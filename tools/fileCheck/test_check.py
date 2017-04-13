#!/usr/bin/env python
# -*- coding:utf-8 -*-
from util import sign
import os

if __name__ == '__main__':
    origin_file = 'test-file/original.html'
    target_file = 'test-file/original-sign.html'
    target_file = 'target-file/original.html'
    sign_val = sign.sign_file(origin_file)
    print sign_val
    sign.sign2file(sign_val, origin_file, target_file)

    filename = os.path.basename(target_file)
    f = open(target_file)
    content = f.read()
    f.close()
    sign_str, sign_ret = sign.retrieve_sign(content)
    print sign_str
    print sign_ret

    print sign.sign_check(target_file)