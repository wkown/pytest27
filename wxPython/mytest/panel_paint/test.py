# -*- coding:utf-8 -*-
__author__ = 'walkskyer'
"""
"""
import wx


class MCard(wx.StaticText):
    def __init__(self, *args, **kwargs):
        wx.StaticText.__init__(self, *args, **kwargs)
        self.setBitmap('31.jpg')
        self.SetSize((447, 681))

        self.Bind(wx.EVT_PAINT, self.OnPaint)
        self.Bind(wx.EVT_LEFT_UP, self.OnClick)

    def setBitmap(self, filename):
        self.bmp = wx.Image(filename, wx.BITMAP_TYPE_JPEG).ConvertToBitmap()

    def OnPaint(self, *args, **kwargs):
        dc = wx.PaintDC(self)
        dc.DrawBitmap(self.bmp, 0,0, True)

    def OnClick(self, evt):
        pos = self.GetPosition()
        self.SetPosition((pos[0],pos[1]+20))

if __name__ == "__main__":
    app = wx.App(False)
    frame = wx.Frame(None, size=(2000, 900))
    frame.Center()
    posX=0
    card1 = MCard(frame, wx.ID_ANY, pos=(posX, 0))
    posX += 100
    card2 = MCard(frame, wx.ID_ANY,pos=(posX, -1))
    posX += 100
    card3 = MCard(frame, wx.ID_ANY,pos=(posX, -1))
    frame.Show()
    app.MainLoop()