# -*- coding:utf-8 -*-
__author__ = 'walkskyer'
"""
去掉文件名的中括号和中文中括号
"""
import os
import glob
import re
import platform

def isWindows():
    return 'Windows' in platform.system()

isWin = isWindows()

start_path=raw_input('请输入文件路径(结尾加上/)：')
if isWin:
    start_path = start_path.decode('utf-8', 'ignore')
print 'start_path:', start_path
stack = [start_path]
patterns = (u'\[.*?\]',u'【.*?】')


while len(stack) > 0:
    print 'stack:%s' % stack
    for curr_path in glob.iglob('%s/*' % stack.pop()):
        if os.path.isdir(curr_path):
            stack.append(curr_path)
            #print stack
            print 'dir:%s' % curr_path
            continue
        #if isWin:
        #    curr_path = curr_path.decode('gbk', 'ignore')
        print 'file:%s' % curr_path
        filename = newname = os.path.basename(curr_path)
        #设置新文件名
        for pattern in patterns:
            newname = re.sub(pattern, '', newname)

        print 'new name:' , newname
        targetname = curr_path.replace(filename, newname)

        #用os模块中的rename方法对文件改名
        os.rename(curr_path, targetname)
        print curr_path, '======>',targetname