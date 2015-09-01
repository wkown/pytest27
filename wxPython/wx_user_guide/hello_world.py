# -*- coding:utf-8 -*-
__author__ = 'walkskyer'
"""
Hello world
"""
import wx

if __name__ == "__main__":
    app = wx.App(False)
    frame = wx.Frame(None,wx.ID_ANY,'Hello world')
    frame.Show(True)
    app.MainLoop()