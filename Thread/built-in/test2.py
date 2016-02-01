# -*- coding:utf-8 -*-
__author__ = 'walkskyer'
"""

"""
import threading
import time

# 方法1：将要执行的方法作为参数传给Thread的构造方法
def func():
    for i in xrange(200):
        print 'func() passed to Thread:%s\n' % i
        time.sleep(0.002)


t = threading.Thread(target=func)
t.start()

# 方法2：从Thread继承，并重写run()
class MyThread(threading.Thread):
    def run(self):
        for i in xrange(100):
            print 'MyThread extended from Thread:%s\n' % i
            time.sleep(0.001)

t = MyThread()
t.start()


if __name__ == "__main__":
    pass