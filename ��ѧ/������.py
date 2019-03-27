# coding=utf8
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
def is_palindrome3(num):
    '''判断是否为回文数的方法 is_palindrome2的改进版'''
    s = str(num)
    if (s[0] == s[-1]): #修改之后效率明显提升
        return s == s[::-1]
    return False


def filterNum(n):
    '''增加filter后没有见到效果啊！
    来源网址：http://www.oschina.net/code/snippet_1026590_20768
    '''
    s = str(n)
    return s == s[::-1] if s[-1] in '123' else False

if __name__ == '__main__':
    start=1
    end = 100000000
    print '第一:'
    t = time.clock()
    print [(x, x * x) for x in xrange(start,end) if is_palindrome(x) and is_palindrome(x * x)]
    print time.clock() - t

    print '第二:'
    t=time.clock()
    print [(x, x * x) for x in xrange(start,end) if is_palindrome2(x) and is_palindrome2(x*x)]
    print 'time:',time.clock()-t

    print '第三:'
    t=time.clock()
    print [(x, x * x) for x in xrange(start,end) if is_palindrome3(x) and is_palindrome3(x*x)]
    print 'time:',time.clock()-t

    print '第四:'
    t=time.clock()
    print [(x, x * x) for x in xrange(start,end) if filterNum(x) and is_palindrome3(x*x)]
    print 'time:',time.clock()-t