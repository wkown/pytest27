# -*- coding:utf-8 -*-
__author__ = 'walkskyer'
"""

"""
import socket

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind(('127.0.0.1',18080))
serverSocket.listen(5)
while 1:
    (clientSocket, address) = serverSocket.accept()
    print clientSocket
    print address
    while 1:
        clientMsg = clientSocket.recv(1024)
        if not clientMsg:
            break
        print 'receive msg:'
        print clientMsg

        print 'send msg:'
        print 'Hi, I am Server'
        clientSocket.send('Hi, I am Server')
    clientSocket.close()

if __name__ == "__main__":
    pass