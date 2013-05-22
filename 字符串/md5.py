# -*- coding: utf8 -*-
__author__ = 'adminer'

import hashlib


def md5(s, raw_output=False):
    res = hashlib.md5(s)
    if raw_output:
        return res.digest()
    return res.hexdigest()
if __name__ == '__main__':
    src = 'this is a test.'
    print md5(src)