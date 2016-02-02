# -*- coding:utf-8 -*-
__author__ = 'walkskyer'
"""
gevent 玩具3 聊天服务器 客户端
"""
import gevent
from gevent import monkey
#monkey.patch_all()
from collections import deque
import socket


class Client():
    def __init__(self,name):
        self.msg_queue = deque()
        self.conn = None
        self.addr = None
        self.name = name

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

    def set_conn_info(self, conn, addr):
        self.conn = conn
        self.addr = addr

    def recv(self, length=1024, flags=0):
        """
        接收指定长度消息
        :param length:
        :param flags:
        :return:
        """
        try:
            return self.conn.recv(length, flags)
        except socket.error, e:
            print e
            return None

    def recv_all(self):
        """
        接收全部消息
        :return:
        """
        data = ''
        while True:
            str_tmp = self.recv()
            if not str_tmp:
                break
            data += str_tmp
        return data

    def send(self,string='', flags=0):
        """
        发送一条消息
        :param string:
        :param flags:
        :return:
        """
        if not string and self.conn:
            self.conn.send(string, flags)

    def send_all(self):
        """
        发送队列中的全部消息
        :return:
        """
        while self.msg_len()>0:
            self.send(self.msg_pop())




def send_msg(client):
    while True:
        client.send_all()
        gevent.sleep(0.5)

def insert_msg(client):
    while True:
        msg = raw_input("say something:")
        if msg:
            client.msg_append(msg)
        gevent.sleep(0.5)

if __name__ == "__main__":
    client = Client('sock')
    client.conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.conn.connect(('127.0.0.1', 18888))
    gevent.joinall([
        gevent.spawn(send_msg, client),
        gevent.spawn(insert_msg,client)
    ])