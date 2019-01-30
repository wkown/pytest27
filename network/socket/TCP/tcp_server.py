# -*- coding:utf-8 -*-
__author__ = 'walkskyer'
"""
"""
import socket
import threading

bind_ip = "0.0.0.0"
bind_port = 9999

# 创建server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 绑定端口
server.bind((bind_ip, bind_port))

# 监听最大处理5个连接
server.listen(5)

def handle_client(client):
    # 获取请求数据
    request = client.recv(1024)

    print "[*] Received :%s" % request

    # 响应数据
    client.send("ACK!")
    client.close()

# 主循环

while True:

    client, addr = server.accept()

    print "[*] Accept connection from %s:%s" % (addr[0], addr[1])

    client_handle = threading.Thread(target=handle_client, args=(client,))
    client_handle.start()