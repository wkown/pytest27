# -*- coding:utf-8 -*-
__author__ = 'walkskyer'
"""
玩具代码，仅仅实现接收客户端请求，并将另一个服务器数据转发给客户端的功能
没有处理客户端请求的数据
"""
#coding=utf-8
import socket
import select
import sys

to_addr = ('127.0.0.1', 80)#转发的地址

class Proxy:
    def __init__(self, addr):
        self.proxy = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.proxy.bind(addr)
        self.proxy.listen(10)
        self.inputs = [self.proxy]
        self.route = {}

    def serve_forever(self):
        print 'proxy listen...'
        while 1:
            readable, _, _ = select.select(self.inputs, [], [])
            for self.sock in readable:
                if self.sock == self.proxy:
                    self.on_join()
                else:
                    data = self.sock.recv(8096)
                    if not data:
                        self.on_quit()
                    else:
                        self.route[self.sock].send(data)

    def on_join(self):
        client, addr = self.proxy.accept()
        print addr,'connect'
        forward = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        forward.connect(to_addr)
        self.inputs += [client, forward]
        self.route[client] = forward
        self.route[forward] = client

    def on_quit(self):
        for s in self.sock, self.route[self.sock]:
            self.inputs.remove(s)
            del self.route[s]
            s.close()

if __name__ == '__main__':
    try:
        Proxy(('',12345)).serve_forever()#代理服务器监听的地址
    except KeyboardInterrupt:
        sys.exit(1)