# -*- coding:utf-8 -*-
import ConfigParser
import os


def load_config(name='main', file_path='../config'):
    """
    加载配置
    :param name:
    :param file_path:
    :return:
    """
    config_file = "%s/%s.ini" % (file_path, name)
    if not os.path.isfile(config_file):
        return None
    config = ConfigParser.SafeConfigParser()
    local_config_file = "%s/%s-local.ini" % (file_path, name)
    if os.path.isfile(local_config_file):
        config.read(local_config_file)
    else:
        config.read(config_file)
    return config


if __name__ == '__main__':
    config_main = load_config()
    print "%s[%s]:%s" % ('sms', 'appkey', config_main.get('sms', 'appkey'))
