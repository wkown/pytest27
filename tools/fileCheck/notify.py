#!/usr/bin/env python
#  -*- coding:utf-8 -*-
import os
import util.sign as sign
import util.op as op
from  pyinotify import WatchManager, Notifier, \
    ProcessEvent, IN_DELETE, IN_CREATE, IN_MODIFY, IN_CLOSE_WRITE

"""
监听程序，本程序只能在linux环境下测试
"""

class EventHandler(ProcessEvent):
    """事件处理"""

    def process_IN_CREATE(self, event):
        file_path = os.path.abspath(os.path.join(event.path, event.name))
        print "Create file: %s " % file_path

    def process_IN_DELETE(self, event):
        file_path = os.path.abspath(os.path.join(event.path, event.name))
        print "Delete file: %s " % file_path

    def process_IN_MODIFY(self, event):
        file_path = os.path.abspath(os.path.join(event.path, event.name))
        print "Modify file: %s " % file_path

    def process_IN_CLOSE_WRITE(self,event):
        file_path = os.path.abspath(os.path.join(event.path, event.name))
        print "Close file: %s " % file_path
        self.check_file(file_path)

    def check_file(self, file_path):
        """
        检查文件合法性
        :param file_path:
        :return:
        """
        if (not file_path.endswith('.html')) or (not os.path.isfile(file_path)):
            print 'file(%s) is not html file or file is not exist' % file_path
            return True

        result = sign.sign_check(file_path)
        if not result:
            print 'sign file error:%s' % file_path
            op.add_file(file_path)
            op.move_file(file_path)
            return result
        print 'sign file ok:%s' % file_path
        return result


def FSMonitor(path='.'):
    if len(path) <= 0:
        print 'There is no folder to monitor,Bye!'
        return

    if isinstance(path,unicode):
        path = path.encode('utf-8')

    wm = WatchManager()
    # IN_DELETE | IN_CREATE | IN_MODIFY | IN_CLOSE_WRITE
    mask = IN_CLOSE_WRITE
    notifier = Notifier(wm, EventHandler())
    paths = path.split(';')
    for path in paths:
        if not path:
            continue
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
    cfg = op.cfg
    FSMonitor(cfg.get('file', 'notify_dir'))
