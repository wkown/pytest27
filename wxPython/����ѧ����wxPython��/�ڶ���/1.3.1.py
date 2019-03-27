# -*- coding:utf-8  -*-
#!/usr/bin/env python
__author__ = 'weijie'

import wx
import sys


class Frame(wx.Frame):

    def __init__(self, parent, id, title):
        print "Frame __init__"
        wx.Frame.__init__(self, parent, id, title)

class App(wx.App):

    def __init__(self, redirect=True, filename=None):
        print "App __init__"
        wx.App.__init__(self, redirect, filename)

    def OnInit(self):
        print "OnInit"    #输出到stdout
        self.frame = Frame(parent=None, id=-1, title='Startup')  #创建框架
        self.frame.Show()
        self.SetTopWindow(self.frame)
        print    sys.stderr, "A pretend error message"    #输出到stderr
        return True

    def OnExit(self):
        print "OnExit"

if __name__ == '__main__':
    app = App(redirect=True) #1 文本重定向从这开始
    print "before MainLoop"
    app.MainLoop()  #2 进入主事件循环
    print "after MainLoop"