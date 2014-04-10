# -*- coding: utf-8 -*-
# filename:test3.py
# datetime:2014-03-13 18:07
__author__ = 'walkskyer'
"""

"""
import multiprocessing
import time
import random

class Worker(multiprocessing.Process):

    def run(self):
        time.sleep(random.random()*10)
        print 'In %s' % self.name
        return

if __name__ == '__main__':
    jobs = []
    for i in range(5):
        p = Worker()
        jobs.append(p)
        p.start()
    for j in jobs:
        j.join()
