# -*- coding:utf-8 -*-
__author__ = 'walkskyer'
"""
示例:遍历文件系统目录下的所有文件
"""
import os
from collections import deque

# Use os.walk()
def scan_dir_1(rootDir):
    list_dirs = os.walk(rootDir)
    for root, dirs, files in list_dirs:
        print("Root: %s" % root)
        for d in dirs:
            print("Dir: %s" % os.path.join(root,d))
        for f in files:
            print("File: %s" % os.path.join(root, f))


# 递归版
def scan_dir_2(rootDir):
    for lists in os.listdir(rootDir):
        path = os.path.join(rootDir,lists)
        if os.path.isdir(path):
            print("Dir: %s" % path)
            scan_dir_2(path)
        if os.path.isfile(path):
            print("File: %s" % path)


# 迭代版
def scan_dir_2_super(rootDir):
    queue = deque([rootDir])
    while len(queue) > 0:
        root = queue.popleft()
        for lists in os.listdir(root):
            path = os.path.join(root,lists)
            if os.path.isdir(path):
                print("Dir: %s" % path)
                queue.append(path)
            if os.path.isfile(path):
                print("File: %s" % path)

if __name__ == "__main__":
    print("#################################################")
    scan_dir_1("../../")
    print("#################################################")
    scan_dir_2("../../")