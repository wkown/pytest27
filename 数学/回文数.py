# coding=gbk
__author__ = 'weijie'
'''
"回文数"是一种数字。如：98789, 这个数字正读是98789,倒读也是98789,正读倒读一样，所以这个数字就是回文数。
脚本来源:http://www.oschina.net/code/snippet_554209_20748
《ruby太慢了》:www.oschina.net/translate/ruby-is-too-slow-for-programming-competitions
'''
import math
import time


def is_palindrome(num):
    '''判断是否为回文数'''
    str_num = str(num)
    if (str_num[0] == str_num[-1]):
        i_len = len(str_num) / 2
        for i in xrange(i_len):
            if (str_num[i] != str_num[-(i + 1)]):
                return False
        return True


if __name__ == '__main__':
    t = time.clock()
    x = 1
    y = 100000000000000
    sqr_x = int(math.sqrt(x))
    sqr_y = int(math.sqrt(y))
    aa = [{x: x * x} for x in xrange(sqr_x, sqr_y) if is_palindrome(x) and is_palindrome(x * x)]
    print aa
    print time.clock() - t
