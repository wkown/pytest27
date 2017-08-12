# -*- coding:utf-8 -*-
__author__ = 'walkskyer'
"""
"""

from wxpy import *


if __name__ == "__main__":
    bot = Bot(cache_path='cache/wxpy.pkl')
    embed()
    bot.file_helper.send('hello world')