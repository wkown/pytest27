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
def is_palindrome2(num):
    '''一个新的判断是否为回文数的方法'''
    s = str(num)
    return s == s[::-1]

if __name__ == '__main__':
    start=1
    end = 10000000
    print 'first:'
    t = time.clock()
    aa = [{x: x * x} for x in xrange(start,end) if is_palindrome(x) and is_palindrome(x * x)]
    print aa
    print time.clock() - t

    print 'secend'
    t=time.clock()
    bb=[{x:x*x} for x in xrange(start,end) if is_palindrome2(x) and is_palindrome2(x*x)]
    print bb
    print 'time:',time.clock()-t