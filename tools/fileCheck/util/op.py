# -*- coding:utf8 -*-
from mysql import MySql
from smsDaYu import send_sms
import os
import conf
import shutil
import time

cfg = conf.load_config('main')

db_cfg = dict(cfg.items('db'))
db = MySql()
db.connect(db_cfg['host'], db_cfg['user'], db_cfg['pwd'], db_cfg['db'], db_cfg['charset'], int(db_cfg['port']))


def add_file(file_path):
    """
    添加文件
    :param file_path:
    :return:
    """
    if not os.path.isfile(file_path):
        return

    data = {
        'path': file_path,
        'dir': os.path.dirname(file_path),
        'status': '0'
    }
    return db.insert('cf_file', data)


def move_file(file_path):
    """
    移动文件到隔离区
    :param file_path:
    :return:
    """
    if not os.path.isfile(file_path):
        return
    filename = os.path.basename(file_path)
    isolate_dir = '%s/%s' % (cfg.get('file', 'isolate_dir'), time.strftime('%Y%m/%d'))
    if not os.path.isdir(isolate_dir):
        os.makedirs(isolate_dir)
    isolate_path = '%s/%s' % (isolate_dir, filename)

    shutil.move(file_path, isolate_path)
    if not os.path.isfile(file_path):
        # where = 'path="%s"' % file_path
        where = {
            'path': file_path
        }
        data = {
            'isolate_path': isolate_path,
            'status': '1'
        }
        return db.update('cf_file', where, data)


def prepare_msg():
    """
    准备消息数据
    :return:
    """
    file_count = dir_count = 0
    dir_bag = set()
    file_bag = set()
    file_id = []
    page = 1
    per_page = 100

    while True:
        rows = db.fetchAll(table='cf_file', where={'msg_id': '0', 'status': '1'}, offset=(page - 1) * per_page,
                           limit=per_page)
        if not rows:
            break
        for row in rows:
            file_bag.add(row['path'])
            dir_bag.add(os.path.dirname(row['path']))
            file_id.append(str(row['file_id']))
        page += 1

    file_count = len(file_bag)
    dir_count = len(dir_bag)
    if dir_count <= 0:
        return None

    dirs = ','.join(dir_bag)
    curr_time = str(int(time.time()))
    data = {'file_count': str(file_count), 'dir_count': str(dir_count), 'dirs': dirs, 'modified': curr_time,
            'dateline': curr_time}

    msg_id = db.insert('cf_msg', data)
    if msg_id <= 0:
        return None

    where = 'file_id in(%s)' % ','.join(file_id)
    db.update('cf_file', where, {'msg_id': str(msg_id)})


def send_msg():
    """
    发送短信消息
    :return:
    """


if __name__ == '__main__':
    print 'add_file:', add_file('../target-file/original-01.html')
    move_file('../target-file/original-01.html')
    prepare_msg()
