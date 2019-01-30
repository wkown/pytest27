# -*- coding:utf-8 -*-
__author__ = 'walkskyer'
"""
"""
import socket

target_host = "127.0.0.1"
target_port = 9999

# 创建socket对象
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 链接服务器
client.connect((target_host, target_port))

# 向服务器发送数据
client.send("GET / HTTP/1.1\r\nHost: www.baidu.com\r\n\r\n")

# 接收服务器响应数据
response = client.recv(4096)

print response


if __name__ == "__main__":
    pass