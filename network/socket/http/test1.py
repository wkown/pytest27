# -*- coding:utf-8 -*-
__author__ = 'walkskyer'
import socket
"""
通过socket测试http协议
"""

if __name__ == "__main__":
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect(('www.baidu.com',80))
    s.send('GET / http/1.1\r\nHost: www.baidu.com\r\nConnection: close\r\n\r\n')
    data_buffer = []
    while True:
        d = s.recv(1024)
        if d:
            data_buffer.append(d)
        else:
            break
    s.close()
    data = ''.join(data_buffer)
    header, body = data.split('\r\n\r\n',1)
    print header
    print '-------------------------------------------'
    print '-------------------------------------------'
    print body
