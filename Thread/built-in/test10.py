# -*- coding:utf-8 -*-
__author__ = 'walkskyer'
"""

"""
import threading

alist = None
condition = threading.Condition()

def doSet():
    if condition.acquire():
        while alist is None:
            condition.wait()
        for i in range(len(alist))[::-1]:
            alist[i] = 1
        condition.release()

def doPrint():
    if condition.acquire():
        while alist is None:
            condition.wait()
        for i in alist:
            print i,
        print
        condition.release()

def doCreate():
    global alist
    if condition.acquire():
        if alist is None:
            alist = [0 for i in range(10)]
            condition.notifyAll()
        condition.release()

tset = threading.Thread(target=doSet,name='tset')
tprint = threading.Thread(target=doPrint,name='tprint')
tcreate = threading.Thread(target=doCreate,name='tcreate')
tset.start()
tprint.start()
tcreate.start()
if __name__ == "__main__":
    pass