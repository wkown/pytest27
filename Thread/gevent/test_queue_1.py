# -*- coding:utf-8 -*-
__author__ = 'walkskyer'
import gevent
from gevent.queue import Queue, Empty

"""
测试队列
"""


def worker(name, task_queue):
    try:
        while True:
            t = task_queue.get(timeout=1)
            print 'Worker %s got task %s' % (name, t)
            gevent.sleep(0.5)
    except Empty:
        print '%s Quiting time!' % name


def boss(task_queue):
    for i in xrange(1, 25):
        print 'Boss send task %s ' % i
        task_queue.put(i)
        gevent.sleep(0.2)


if __name__ == "__main__":
    task = Queue()
    gevent.joinall([
        gevent.spawn(boss, task),
        gevent.spawn(worker, '张三', task),
        gevent.spawn(worker, '李四', task),
        gevent.spawn(worker, '王二麻子', task)
    ])
