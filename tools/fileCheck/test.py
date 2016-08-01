# -*- coding:utf-8 -*-
import lib


if __name__ == '__main__':
    origin_file = 'test-file/original.html'
    target_file = 'test-file/original-sign.html'
    target_file = 'target-file/original.html'
    sign = lib.signature_file(origin_file)
    print sign
    lib.sign2file(sign, origin_file, target_file)

    print lib.signature_check(target_file)