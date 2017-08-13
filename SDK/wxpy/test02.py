# -*- coding:utf-8 -*-
__author__ = 'walkskyer'
"""
简单的接收和处理消息测试
"""
from wxpy import *
import time


if __name__ == "__main__":
    bot = Bot(cache_path='cache/wxpy.pkl')

    @bot.register()
    def reply(msg):
        print msg
        return 'hello'


    friend = bot.friends().search(u'书生')[0]
    while True:
        friend.send_msg(u'主动发布')
        time.sleep(20)

embed()