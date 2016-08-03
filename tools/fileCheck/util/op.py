# -*- coding:utf8 -*-
from mysql import MySql
from smsDaYu import send_sms
import os
import conf

cfg = conf.load_config('main')

db_cfg = dict(cfg.items('db'))
db = MySql()
db.connect(db_cfg['host'], db_cfg['user'], db_cfg['pwd'], db_cfg['db'], db_cfg['charset'], db_cfg['port'])


def add_file(file_path):
    """
    添加文件
    :param file_path:
    :return:
    """


def move_file(file_path):
    """
    移动文件到隔离区
    :param file_path:
    :return:
    """


def send_msg():
    """
    发送短信消息
    :return:
    """