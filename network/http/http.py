# -*- coding:utf-8 -*-
__author__ = 'walkskyer'
"""
http请求模拟
https://www.bicky.me/archive/python-make-http-request-by-socket-library/
"""
import socket

param_data = 'param1=a&param2=b'
param_lenth = str(len(param_data))


request_str = '''GET /?'''+param_data+''' HTTP/1.1\r\nHost: *.*.*.*\r\n\r\n'''

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('127.0.0.1', 80))
sock.send(request_str)
data = sock.recv(4096)
sock.close()
print 'GET method fetch data:'
print data.split('\r\n\r\n')[1]


request_str = '''POST / HTTP/1.1\r\nHost: *.*.*.*\r\nContent-Type: application/x-www-form-urlencoded\r\nContent-Length: '''+param_lenth+'''\r\n\r\n'''+param_data

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('127.0.0.1', 80))
sock.send(request_str)
data = sock.recv(4096)
sock.close()
print 'POST method fetch data:'
print data.split('\r\n\r\n')[1]


request_str = '''PUT / HTTP/1.1\r\nHost: *.*.*.*\r\nContent-Length: '''+param_lenth+'''\r\n\r\n'''+param_data

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('127.0.0.1', 80))
sock.send(request_str)
data = sock.recv(4096)
sock.close()
print 'PUT method fetch data:'
print data.split('\r\n\r\n')[1]


request_str = '''DELETE / HTTP/1.1\r\nHost: *.*.*.*\r\nContent-Length: '''+param_lenth+'''\r\n\r\n'''+param_data

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('127.0.0.1', 80))
sock.send(request_str)
data = sock.recv(4096)
sock.close()
print 'DELETE method fetch data:'
print data.split('\r\n\r\n')[1]
if __name__ == "__main__":
    pass