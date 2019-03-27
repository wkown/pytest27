# -*- coding:utf-8 -*-
__author__ = 'weijie'

import wx


class Frame(wx.Frame):
    pass


class App(wx.App):
    def OnPreInit(self):
        self.frame = Frame(parent=None, title='spare')
        self.frame.Show()
        self.SetTopWindow(self.frame)
        return True

if __name__ == '__main__':
    app = App()
    app.MainLoop()