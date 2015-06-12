# -*- coding:utf-8 -*-
__author__ = 'walkskyer'
"""
gevent 玩具2
"""
import gevent
from gevent import monkey
monkey.patch_all()
from collections import deque


class Client():
    def __init__(self):
        self.msg_queue = deque()

    def msg_append(self, msg):
        if not msg:
            return None
        self.msg_queue.append(msg)

    def msg_pop(self):
        if len(self.msg_queue)>0:
            return self.msg_queue.popleft()
        return None

    def msg_len(self):
        return len(self.msg_queue)




def print_msg(name, client):
    while True:
        if client.msg_len() > 0:
            print '%s:%s' % (name, client.msg_pop())

        if name == 'g1':
            print '*************************************'
        gevent.sleep(10)

def insert_msg(client_que):
    while True:
        msg = raw_input('please input a msg:')
        if msg:
            for client in client_que:
                client.msg_append(msg)
        gevent.sleep(3)

if __name__ == "__main__":
    client_que = deque()

    for i in xrange(1,10):
        client = Client()
        client_que.append(client)
        gevent.spawn(print_msg, 'g%s' % i, client).start()

    gevent.joinall([gevent.spawn(insert_msg,client_que)])