# -*- coding:utf-8 -*-
__author__ = 'walkskyer'
"""
添加测试获取剪贴板内容的功能
"""
import win32clipboard


if __name__ == "__main__":
    win32clipboard.OpenClipboard()
    s= win32clipboard.GetClipboardData(win32clipboard.CF_TEXT)
    win32clipboard.CloseClipboard()
    print s