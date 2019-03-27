# -*- coding:utf-8 -*-
"""给框架增加窗口部件"""
__author__ = 'weijie'
import wx


class InsertFrame(wx.Frame):

    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, u'有按钮的框架', size=(300, 120))
        panel = wx.Panel(self)#创建画板
        button = wx.Button(panel, label=u'关闭', pos=(125, 10), size=(50, 50))#将按钮添加到画板
        #绑定按钮的单击事件
        self.Bind(wx.EVT_BUTTON, self.OnCloseMe, button)
        #绑定窗口的关闭事件
        self.Bind(wx.EVT_CLOSE, self.OnCloseWindow)

    def OnCloseMe(self, event):
        dlg = wx.MessageDialog(None, u'是否关闭程序？', u'关闭程序', wx.YES_NO | wx.ICON_QUESTION)
        result = dlg.ShowModal()
        if result == wx.ID_YES:
            self.Close(True)

    def OnCloseWindow(self, event):
        self.Destroy()

if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = InsertFrame(None, -1)
    frame.Show()
    app.MainLoop()