# -*- coding:utf-8 -*-
__author__ = 'walkskyer'
"""
"""
from PIL import Image
import os
from collections import deque
import sys, getopt


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
def usage():
    print "usage: "
    sys.exit(1)

if __name__ == "__main__":

    srcDir = ""
    ratio = 4
    targetDir = "./pics"
    count = 1

    try:
        opts, args = getopt.getopt(sys.argv[1:], "hs:t:r:c:", ["src-dir=","target-dir=","ratio=","count="])
    except getopt.GetoptError:
        usage()

    if len(opts) == 0:
        usage()

    for opt, arg in opts:
        if opt == "-h":
            usage()
        if opt in ("-s", "--src-dir"):
            srcDir = arg
        if opt in ("-t", "--target-dir"):
            targetDir = arg
        if opt in ("-r", "--ratio"):
            ratio = arg
        if opt in ("-c", "--count"):
            count = int(arg)

        if not srcDir:
            usage()


    if not os.path.exists(targetDir):
        os.mkdir(targetDir)


    while os.path.isfile("%s/pic_%04d.jpg" % (targetDir, count)):
        count += 1

    for f in scan_dir(srcDir):
        targetFile = "%s/pic_%04d.jpg" % (targetDir, count)
        im = Image.open(f)
        if im.width > 700:
            continue
        print "%s" % (im,)
        width = int(im.width/int(ratio))
        height = int(im.height/int(ratio))
        im.resize((width, height), Image.ANTIALIAS).save(targetFile, "JPEG", quality=60)
        count += 1