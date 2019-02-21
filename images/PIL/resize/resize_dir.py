# -*- coding:utf-8 -*-
__author__ = 'walkskyer'
"""
"""
from PIL import Image
import os
from collections import deque


def scan_dir(rootDir):
    queue = deque([rootDir])
    while len(queue) > 0:
        root = queue.popleft()
        for fname in os.listdir(root):
            path = os.path.join(root, fname)
            if os.path.isdir(path):
                queue.append(path)
            if os.path.isfile(path):
                yield path

if __name__ == "__main__":

    rootDir = raw_input("Dir include photos: ")
    count=1
    targetDir = "./pics"
    if not os.path.exists(targetDir):
        os.mkdir(targetDir)
    for f in scan_dir(rootDir):
        im = Image.open(f)
        print "%s" % (im,)
        im.resize((350, 525), Image.ANTIALIAS).save("%s/pic_%04d.jpg" % (targetDir, count), "JPEG", quality=55)
        count += 1