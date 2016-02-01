# -*- coding:utf-8 -*-
__author__ = 'walkskyer'
"""
Timer 定时器
"""
import threading

def func():
    print 'hello timer!'

timer = threading.Timer(5, func)
timer.start()

timer = threading.Timer(5, func)
timer.start()

if __name__ == "__main__":
    pass