# -*- coding:utf-8 -*-
from mysql import MySql
from smsDaYu import send_sms
from sign import md5
import os
import conf
import shutil
import time
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

curr_path = os.path.dirname(__file__)
if not curr_path:
    curr_path = os.getcwd()
    if not curr_path.endswith('util'):
        curr_path += '/util'

cfg = conf.load_config('main', curr_path+'/../config')

db_cfg = dict(cfg.items('db'))
db = MySql()
db.connect(db_cfg['host'], db_cfg['user'], db_cfg['pwd'], db_cfg['db'], db_cfg['charset'], int(db_cfg['port']))


notify_info = dict()


def get_notify_dirs():
    """
    获取数据库监控目录
    :return:
    """
    client_id = cfg.get('common', 'client_id')
    if client_id <= 0:
        print 'err'
    rows = db.fetchAll('cf_channel', {'monitorid': client_id}, None, 0, 100)
    dirs = set()
    for row in rows:
        dirs.add(row['directory'])
    return rows,dirs
# 调整监控目录配置
if cfg.get('file', 'notify_dir_source') == 'db' and cfg.get('common', 'client_id') > 0:
    notify_info, dirs=get_notify_dirs()
    if len(dirs) > 0:
        cfg.set('file', 'notify_dir', ';'.join(dirs))
    else:
        cfg.set('file', 'notify_dir', '')



def add_file(file_path):
    """
    添加文件
    :param file_path:
    :return:
    """
    if not os.path.isfile(file_path):
        return

    data = {
        'channel_id': '0',
        'path': file_path,
        'dir': os.path.dirname(file_path),
        'status': '0'
    }
    data['path_md5'] = md5(data['path'])
    for info in notify_info:
        if file_path.startswith(info['directory']):
            data['channel_id'] = str(info['id'])
            break

    return db.replace('cf_file', data)


def move_file(file_path):
    """
    移动文件到隔离区
    :param file_path:
    :return:
    """
    if not os.path.isfile(file_path):
        return
    filename = os.path.basename(file_path)

    domain = 'unknown'
    for info in notify_info:
        if file_path.startswith(info['directory']):
            if info['domainname']:
                domain = str(info['domainname'])
            break

    isolate_dir = '%s/%s/%s/' % (cfg.get('file', 'isolate_dir'), time.strftime('%Y%m/%d'), domain)

    if not os.path.isdir(isolate_dir) and not isolate_dir.startswith('/'):
        isolate_dir = '%s/%s' % (curr_path, isolate_dir)

    if not os.path.isdir(isolate_dir):
        os.makedirs(isolate_dir)

    isolate_path = '%s/%s' % (os.path.realpath(isolate_dir), filename)

    shutil.move(file_path, isolate_path)
    if not os.path.isfile(file_path):
        # where = 'path="%s"' % file_path
        where = {
            'path_md5': md5(file_path)
        }
        data = {
            'isolate_path': isolate_path,
            'status': '1',
            'modified': str(int(time.time()))
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
        rows = db.fetchAll(table='cf_file', where={'msg_id': '0', 'status': '0'}, offset=(page - 1) * per_page,
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

    curr_time = str(int(time.time()))
    data = {'file_count': str(file_count), 'dir_count': str(dir_count),  'modified': curr_time, 'dateline': curr_time}

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
    contacts = db.fetchAll(table='cf_contact', limit=100)

    sms_cfg = dict(cfg.items('sms'))

    for info in contacts:
        #print info
        if not info['mobile']:
            continue

        msg_page = 1
        msg_per_page = 10
        msg_id = info['msg_id']
        msg_where = 'msg_id > %s' % str(info['msg_id'])
        while True:
            msg_rows = db.fetchAll(table='cf_msg', where=msg_where, offset=(msg_page-1)*msg_per_page, limit=msg_per_page)
            msg_page += 1
            if not msg_rows:
                break
            for msg_row in msg_rows:
                param = {
                    'name': info['name'],
                    #'dirs': msg_row['dirs'],
                    'num': str(msg_row['file_count']),
                    'time': time.strftime('%m-%d %H:%M:%S')
                }
                result = send_sms(info['mobile'], param, sms_cfg)
                if result:
                    msg_id = msg_row['msg_id']

            if msg_id > info['msg_id']:
                db.update('cf_contact',
                          {'contact_id': str(info['contact_id'])},
                          {'msg_id': str(msg_id), 'modified': str(int(time.time()))})
                info['msg_id'] = msg_id


if __name__ == '__main__':
    #print 'add_file:', add_file('../target-file/original-01.html')
    #move_file('../target-file/original-01.html')
    #prepare_msg()
    #send_msg()
    pass
