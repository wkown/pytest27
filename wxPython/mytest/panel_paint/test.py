# -*- coding:utf-8 -*-
__author__ = 'walkskyer'
"""
"""
import wx
import wx.lib.newevent

#刷新纸牌
(CardRePaint, EVT_CARD_REPAINT) = wx.lib.newevent.NewEvent()
#重设纸牌位置
(CardChangePos, EVT_CARD_CHANGEPOS) = wx.lib.newevent.NewEvent()


class MCard(wx.StaticText):
    def __init__(self, *args, **kwargs):
        wx.StaticText.__init__(self, *args, **kwargs)
        self.setBitmap('31.jpg')
        self.SetSize((447, 681))

        self.Bind(wx.EVT_PAINT, self.OnPaint)
        self.Bind(wx.EVT_LEFT_UP, self.OnClick)
        self.Bind(EVT_CARD_CHANGEPOS, self.ChangePos)

        self.is_pickup = False
        self.pos = self.GetPosition()
        if kwargs.has_key('order_index'):
            self.order_index = kwargs['order_index']

    def setBitmap(self, filename):
        self.bmp = wx.Image(filename, wx.BITMAP_TYPE_JPEG).ConvertToBitmap()

    def OnPaint(self, *args, **kwargs):
        dc = wx.PaintDC(self)
        dc.DrawBitmap(self.bmp, 0,0, True)

    def ChangePos(self, evt):
        self.SetPosition(self.pos)


    def OnClick(self, evt):
        self.is_pickup = not self.is_pickup

        #点击以后应该出发EVT_PAINT事件让所有card都执行刷新一次
        pos = self.GetPosition()
        if self.is_pickup:
            self.pos=(pos[0], pos[1]-20)
        else:
            self.pos=(pos[0], pos[1]+20)

        evt = CardRePaint()
        wx.PostEvent(self.GetParent(), evt)


class MyFrame(wx.Frame):
    def __init__(self, *args, **kwargs):
        wx.Frame.__init__(self, *args, **kwargs)
        self.Center()
        self.cards = []
        self.initCard()
        self.Bind(EVT_CARD_REPAINT,self.repaint_cards)

    def initCard(self):
        posX=0
        for i in xrange(1,6):
            self.cards.append(MCard(self, wx.ID_ANY, pos=(posX+(100*i), 50)))

    def repaint_cards(self, evt):
        for card in self.cards:
            evt = CardChangePos()
            wx.PostEvent(card, evt)

if __name__ == "__main__":
    app = wx.App(False)
    frame = MyFrame(None, size=(2000, 900))
    frame.Show()
    app.MainLoop()