# -*- coding:utf-8 -*-
__author__ = 'walkskyer'
"""
"""
import os
import glob

def replace_content(content, replcement, target):
    return content.replace(replcement, target)

def run(path, replcement, target):
    print 'path:', path
    if not os.path.isdir(path):
        return

    for path_sub in os.listdir(path):
        print path_sub

        path_sub = path+r'/'+path_sub

        print path_sub

        if os.path.isdir(path_sub):
            run(path_sub, replcement, target)
            continue
        if os.path.isfile(path_sub):
            with open(path_sub, 'rb') as f:
                content = f.read()
                content = replace_content(content, replcement, target)
                print content
                f.close()
                f = open(path_sub, 'wb')
                f.write(content)
                f.close()


if __name__ == "__main__":
    path = raw_input('give me a path:').strip()
    replace = raw_input('replace string:').strip()
    target = raw_input('target string:').strip()

    run(path, replace, target)