# -*- coding:utf-8 -*-
__author__ = 'walkskyer'
"""
gevent 玩具1
"""
import gevent
from gevent import monkey;

monkey.patch_all()
import socket
import math
import random
import time

switch = False


class Switch():
    def __init__(self):
        self.count = 0
        self.wait_count = 1

    def status(self):
        return self.wait_count > 0


def handle(name, switch):
    while True:
        if switch.status():
            print '%s:%s' % (name, random.random())

        if name == 'g1':
            print '*************************************'
        gevent.sleep(1)


if __name__ == "__main__":
    switch = Switch()
    g1 = gevent.spawn(handle, 'g1', switch)
    g1.start()

    time.sleep(6)

    g2 = gevent.spawn(handle, 'g2', switch)
    g2.start()

    time.sleep(6)

    g3 = gevent.spawn(handle, 'g3', switch)
    g3.start()

    time.sleep(6)

    g4 = gevent.spawn(handle, 'g4', switch)
    g4.start()

    time.sleep(6)

    gevent.joinall([
        gevent.spawn(handle, '1:dog', switch),
        gevent.spawn(handle, '2:cat', switch),
        gevent.spawn(handle, '3:bird', switch),
        gevent.spawn(handle, '4:people', switch),
    ])
