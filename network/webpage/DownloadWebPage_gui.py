# -*- coding:utf-8 -*-
__author__ = 'walkskyer'
"""
为下载网页程序增加Gui界面
"""
import wx
import wx.lib.newevent
import sys
import os
import time
import re
import thread
import DownloadsWebPage as w_dwp
import StringIO
# 定义
(DwpPrint, EVT_DWP_PRINT) = wx.lib.newevent.NewEvent()


class DwpStdout:
    def __init__(self, win=None):
        self.win = win

    def write(self, *args, **kwargs):
        val = ''.join(args)
        evt = DwpPrint(value=val)
        wx.PostEvent(self.win, evt)


class DownloadPanel(wx.Panel):
    def __init__(self, *args, **kwargs):
        wx.Panel.__init__(self, *args, **kwargs)

        self.wildcard = "Html Files (*.html,*.htm)|*.html;*.htm|" \
                        "All files (*.*)|*.*"
        self.defaultLocalTxt = u'可选择本地源文件...'

        mainSizer = wx.BoxSizer(wx.VERTICAL)
        gridSizer = wx.GridBagSizer(vgap=3, hgap=4)

        textFieldSize = (500, -1)
        lblSize = (70, -1)

        #输入网址
        self.lbl_url = wx.StaticText(self, size=lblSize, label=u"目标网址:", style=wx.ALIGN_RIGHT)
        gridSizer.Add(self.lbl_url, pos=(0, 0), flag=wx.ALIGN_RIGHT)
        self.txt_url = wx.TextCtrl(self, size=textFieldSize)
        gridSizer.Add(self.txt_url, pos=(0, 1), span=(1,3))

        #选择本地源文件
        self.lbl_local = wx.StaticText(self, size=lblSize, label=u"本地源文件:", style=wx.ALIGN_RIGHT)
        gridSizer.Add(self.lbl_local, pos=(1, 0), flag=wx.ALIGN_RIGHT)
        self.txt_local = wx.TextCtrl(self, value=self.defaultLocalTxt, size=(430, -1), style=wx.TE_READONLY)
        gridSizer.Add(self.txt_local, pos=(1, 1))

        self.btn_view_file = wx.Button(self, label=u"浏览", size=(30, 25))
        gridSizer.Add(self.btn_view_file, pos=(1, 2))
        self.Bind(wx.EVT_BUTTON, self.OnFindFile, self.btn_view_file)

        self.btn_local_clear = wx.Button(self, label=u"清除", size=(30, 25))
        gridSizer.Add(self.btn_local_clear, pos=(1, 3))
        self.Bind(wx.EVT_BUTTON, self.OnLocalClear, self.btn_local_clear)

        #保存文件名
        self.lbl_target_filename = wx.StaticText(self, size=lblSize, label=u"保存文件名:", style=wx.ALIGN_RIGHT)
        gridSizer.Add(self.lbl_target_filename, pos=(2, 0), flag=wx.ALIGN_RIGHT)
        self.txt_target_filename = wx.TextCtrl(self, size=textFieldSize, value="index.html")
        gridSizer.Add(self.txt_target_filename, pos=(2, 1), span=(1,3))

        #显示日志
        self.txt_log = wx.TextCtrl(self, style=wx.TE_MULTILINE | wx.TE_READONLY)
        self.Bind(EVT_DWP_PRINT, self.PrintLog)

        #下载按钮
        self.btn_download = wx.Button(self, label=u"下载")
        self.Bind(wx.EVT_BUTTON, self.OnDownload, self.btn_download)

        #使用布局
        mainSizer.Add(gridSizer, 0, wx.EXPAND)
        mainSizer.Add(self.btn_download, 0, wx.CENTER)
        mainSizer.Add(self.txt_log, 1, wx.EXPAND)

        self.SetSizerAndFit(mainSizer)

    def PrintLog(self, evt):
        self.txt_log.WriteText(evt.value)

    def OnLocalClear(self, evt):
        """
        清空本地文件选取框
        :param evt:
        :return:
        """
        self.txt_local.SetValue(self.defaultLocalTxt)

    def OnFindFile(self, evt):
        """
        显示文件选取框
        :param evt:
        :return:
        """
        dlg = wx.FileDialog(
            self, message=u"选择一个文件..",
            defaultDir=os.getcwd(),
            defaultFile="",
            wildcard= self.wildcard,
            style=wx.OPEN | wx.CHANGE_DIR
            )
        if dlg.ShowModal() == wx.ID_OK:
            # This returns a Python list of files that were selected.
            paths = dlg.GetPaths()
            self.txt_log.WriteText(u'选择本地文件:')
            for path in paths:
                self.txt_log.WriteText('%s\n' % path)
                self.txt_local.SetValue(path)

        # Destroy the dialog. Don't do this until you are done with it!
        # BAD things can happen otherwise!
        dlg.Destroy()

    def get_local_filename(self):
        """
        获取本地源文件名
        :return:
        """
        filename = self.txt_local.GetValue()
        if filename == '' or filename == self.defaultLocalTxt:
            return None
        return filename

    def OnDownload(self, evt):

        url = target_name = base_url = ''

        url = self.txt_url.GetValue()
        if url == "":
            dlg = wx.MessageDialog(self, u'请填写一个有效的目标网址!如:http://www.baidu.com',
                               u'请输入目标网址',
                               wx.OK | wx.ICON_INFORMATION)
            dlg.ShowModal()
            dlg.Destroy()
            return

        local_file = self.get_local_filename()

        if not os.path.isdir('html'):
            os.mkdir('html')
        os.chdir('html')

        if local_file is not None and os.path.isfile(w_dwp.getCodeStr(local_file)):
            url, base_url = local_file, url

            if base_url.find(r'://') == -1:
                base_url = 'http://%s' % base_url

            url_info = w_dwp.urlparse(base_url)
            base_name = os.path.basename(url)
            url = w_dwp.getCodeStr(url)
        else:
            if url.find(r'://') == -1:
                url = 'http://%s' % url
            url_info = w_dwp.urlparse(url)
            base_url = os.path.dirname(url)
            base_name = os.path.basename(url)

            pos = int(base_name.find('.'))
            if pos is -1:
                ext = None
            else:
                ext = base_name[pos + 1:]
            if ext not in ('html', 'htm', 'php', 'asp', 'jsp', 'aspx'):
                base_url = url[0:url.rfind('/')]
                base_name = 'index.html'

        root_path = '%s://%s' % (url_info.scheme, url_info.netloc)

        if base_url == 'http:' or base_url == 'http:/':
            base_url = root_path


        target_name = self.txt_target_filename.GetValue()
        if target_name:
            base_name = target_name

        print 'We will download the page use this url:%s' % w_dwp.getCodeStr(url, 'utf-8')
        time.sleep(2)
        thread.start_new_thread(w_dwp.run_download,(url, base_url, base_name))
        #w_dwp.run_download(url, base_url, base_name)


if __name__ == "__main__":
    app = wx.App(False)
    frame = wx.Frame(None, title="Download Web Page", size=(600, 800))
    panel = DownloadPanel(frame)
    stdoutX = sys.stdout
    sys.stdout = DwpStdout(panel)
    frame.Show()
    app.MainLoop()
