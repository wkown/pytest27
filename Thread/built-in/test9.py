# -*- coding:utf-8 -*-
__author__ = 'walkskyer'
"""

"""
import threading

local = threading.local()
local.tname = 'main'

def func():
    local.tname = 'notmain'
    print local.tname

t1 = threading.Thread(target=func)
t1.start()
t1.join()

print local.tname
if __name__ == "__main__":
    pass