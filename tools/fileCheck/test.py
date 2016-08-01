# -*- coding:utf-8 -*-
import sign


if __name__ == '__main__':
    origin_file = 'test-file/original.html'
    target_file = 'test-file/original-sign.html'
    target_file = 'target-file/original.html'
    sign_val = sign.sign_file(origin_file)
    print sign_val
    sign.sign2file(sign, origin_file, target_file)

    print sign.sign_check(target_file)