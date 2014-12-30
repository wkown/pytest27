# -*- coding:utf-8 -*-
__author__ = 'walkskyer'
"""
 tcp client
"""
import socket

HOST = '127.0.0.1'
PORT = 50007
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 定义socket类型，网络通信，TCP
s.connect((HOST, PORT))  # 要连接的IP与端口
while 1:
    cmd = raw_input("Please input cmd:")  # 与人交互，输入命令
    s.sendall(cmd)  # 把命令发送给对端
    data = s.recv(1024)  # 把接收的数据定义为变量
    print data  # 输出变量
s.close()  #关闭连接