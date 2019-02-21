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
    ratio = raw_input("ratio:")

    targetDir = "./pics"
    if not os.path.exists(targetDir):
        os.mkdir(targetDir)


    count = 1
    while os.path.isfile("%s/pic_%04d.jpg" % (targetDir, count)):
        count += 1

    for f in scan_dir(rootDir):
        targetFile = "%s/pic_%04d.jpg" % (targetDir, count)
        im = Image.open(f)
        if im.width > 700:
            continue
        print "%s" % (im,)
        width = int(im.width/int(ratio))
        height = int(im.height/int(ratio))
        im.resize((width, height), Image.ANTIALIAS).save(targetFile, "JPEG", quality=60)
        count += 1