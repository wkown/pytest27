#!/usr/bin/env python
#  -*- coding:utf-8 -*-
import os
import util.sign as sign
from  pyinotify import WatchManager, Notifier, \
    ProcessEvent, IN_DELETE, IN_CREATE, IN_MODIFY

"""
监听程序，本程序只能在linux环境下测试
"""


class EventHandler(ProcessEvent):
    """事件处理"""

    def process_IN_CREATE(self, event):
        file_path = os.path.abspath(os.path.join(event.path, event.name))
        self.check_file(file_path)
        print "Create file: %s " % file_path

    def process_IN_DELETE(self, event):
        file_path = os.path.abspath(os.path.join(event.path, event.name))
        print "Delete file: %s " % file_path

    def process_IN_MODIFY(self, event):
        file_path = os.path.abspath(os.path.join(event.path, event.name))
        self.check_file(file_path)
        print "Modify file: %s " % file_path

    def check_file(self, file_path):
        """
        检查文件合法性
        :param file_path:
        :return:
        """
        if not os.path.isfile(file_path):
            return True

        result = sign.sign_check(file_path)
        if not result:
            print '文件签名错误:%s' % file_path
            return result
        print '文件签名正确:%s' % file_path
        return result


def FSMonitor(path='.'):
    wm = WatchManager()
    mask = IN_DELETE | IN_CREATE | IN_MODIFY
    notifier = Notifier(wm, EventHandler())
    wm.add_watch(path, mask, auto_add=True, rec=True)
    print 'now starting monitor: %s' % path
    while True:
        try:
            notifier.process_events()
            if notifier.check_events():
                notifier.read_events()
        except KeyboardInterrupt, e:
            print e
            notifier.stop()
            break


if __name__ == "__main__":
    import util.conf as conf
    cfg = conf.load_config('main', 'config')
    FSMonitor(cfg.get('file', 'notify_dir'))
