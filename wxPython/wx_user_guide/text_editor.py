# -*- coding:utf-8 -*-
__author__ = 'walkskyer'
"""
A simple text editor
"""
import wx
import os


class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(400, 400))
        self.control = wx.TextCtrl(self, style = wx.TE_MULTILINE)
        self.Bind(wx.EVT_TEXT, self.OnModified, self.control)

        self.CreateStatusBar()

        #Setting up the menu.
        filemenu = wx.Menu()

        # wx.ID_ABOUT and wx.ID_EXIT are standard IDs provided by wxWidgets.
        menuOpen = filemenu.Append(wx.ID_OPEN, "&Open", "Open a file")
        menuAbout = filemenu.Append(wx.ID_ABOUT, "&About", " Infomation about this program")
        filemenu.AppendSeparator()
        menuExit = filemenu.Append(wx.ID_EXIT, "&Exit", "Teminate the program")

        # Set events.
        self.Bind(wx.EVT_MENU, self.OnOpen, menuOpen)
        self.Bind(wx.EVT_MENU, self.OnAbout, menuAbout)
        self.Bind(wx.EVT_MENU, self.OnExit, menuExit)

        # Edit Menu
        editmenu = wx.Menu()
        menuSave = editmenu.Append(wx.ID_SAVE, "&Save", "Save to the file")

        self.Bind(wx.EVT_MENU, self.OnSave, menuSave)

        # Creating the member.
        menuBar = wx.MenuBar()
        menuBar.Append(filemenu,"&File")
        menuBar.Append(editmenu,"&Edit")
        self.SetMenuBar(menuBar)

        self.sizer2 = wx.BoxSizer(wx.HORIZONTAL)
        self.buttons = []
        for i in xrange(0,6):
            self.buttons.append(wx.Button(self, -1, "Button &%d" % i))
            self.sizer2.Add(self.buttons[i], 1, wx.EXPAND)

        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(self.control, 1, wx.EXPAND)
        self.sizer.Add(self.sizer2, 0, wx.EXPAND)

        self.SetSizer(self.sizer)
        self.SetAutoLayout(1)
        self.sizer.Fit(self)

        self.Show(True)

    def OnAbout(self,event):
        dlg = wx.MessageDialog(self, "A small text editor", "About Sample Editor", wx.OK)
        dlg.ShowModal()
        dlg.Destroy()

    def OnExit(self,event):
        self.Close(True)

    def OnOpen(self,event):
        """Open a file"""
        self.dirname = ''
        dlg = wx.FileDialog(self, "Choose a file", self.dirname, "", "*.*", wx.OPEN)
        if dlg.ShowModal() == wx.ID_OK:
            self.filename = dlg.GetFilename()
            self.dirname = dlg.GetDirectory()
            print self.dirname
            print os.path.join(self.dirname, self.filename)
            f = open(os.path.join(self.dirname, self.filename), 'r')
            self.control.SetValue(f.read())
            f.close()

        dlg.Destroy()

    def OnSave(self,event):
        if self.filename and self.dirname:
            f=open(os.path.join(self.dirname,self.filename),'w')
            f.write(self.control.GetValue())
            f.close()
            self.SetStatusText('The file %s has saved.' % os.path.join(self.dirname,self.filename))

    def OnModified(self,event):
        self.SetStatusText('The file %s has been modified.' % os.path.join(self.dirname,self.filename))
if __name__ == "__main__":
    app = wx.App(False)
    frame = MyFrame(None, 'Small editor')
    app.MainLoop()