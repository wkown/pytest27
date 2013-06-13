# -*- coding:utf-8 -*-
__author__ = 'weijie'

import wx

class MyApp(wx.App):

    def OnPreInit(self):
        frame = wx.Frame(parent=None, title='Bare')
        frame.Show()
        return True

if __name__ == '__main__':
    app = MyApp()
    app.MainLoop()
