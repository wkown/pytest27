# -*- coding:utf-8 -*-
import wx
__author__ = 'walkskyer'
"""
gui
"""


class MyFrame(wx.Frame):
    def __init__(self, *args, **kwargs):
        wx.Frame.__init__(self, *args, **kwargs)
        self.Center()
        self.CreateStatusBar()

        self.vSizer = wx.BoxSizer(wx.VERTICAL)


class MyPanel(wx.Panel):
    def __init__(self, *args, **kwargs):
        wx.Panel.__init__(self, *args, **kwargs)
        # 动态控件组 label text des
        self.dynamicList = []

if __name__ == "__main__":
    app = wx.App(False)
    frame = MyFrame(None,size = (600, 800))
    frame.Show()
    app.MainLoop()