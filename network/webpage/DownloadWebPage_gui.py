# -*- coding:utf-8 -*-
import wx
import wx.lib.newevent
import wx.lib.dialogs
from wx.lib.wordwrap import wordwrap

import sys
import os
import time
import thread
import DownloadsWebPage as w_dwp
import icon_images

__author__ = 'walkskyer'
"""
为下载网页程序增加Gui界面
"""

# 定义事件
(DwpPrint, EVT_DWP_PRINT) = wx.lib.newevent.NewEvent()

app_info = {
    'name': u"网页下载器",
    'usage': u"用法:\n"
             u"一般情况下只需要在目标网址填写好想要下载的网址即可。\n\n"
             u"此时，聪明的你，一定想到了，有些网页需要登录下载怎么办？\n"
             u"这时有个解决办法，就是手动将不能直接下载的网页保存到本地，注意保存网页一定只保存网页，不要选择保存全部。"
             u"然后，同样输入目标网址，并且选择，保存好的网页源文件，点击下载即可。\n\n"
             u"聪明的你一定注意到还有个保存文件名，顾名思义了！",
    'description': u"用于下载完整网页的程序，本程序同时保存网页中可探测的资源文件:js/css/图片/css中的图片，并且根据资源类型进行分类，放置到不同的目录中方便使用",
    'version': '1.0.0',
    'developers': ["walkskyer"]
}


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
        gridSizer = wx.GridBagSizer(vgap=4, hgap=4)

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

        #参数设置
        self.lbl_target_filename = wx.StaticText(self, size=lblSize, label=u"附加参数:", style=wx.ALIGN_RIGHT)
        gridSizer.Add(self.lbl_target_filename, pos=(3, 0), flag=wx.ALIGN_RIGHT)
        self.checkbox_save_basename = wx.CheckBox(self, -1, u'保存路径名', style=wx.ALIGN_RIGHT)
        gridSizer.Add(self.checkbox_save_basename, pos=(3, 1))
        self.Bind(wx.EVT_CHECKBOX, self.OnSaveBasename, self.checkbox_save_basename)


        #下载按钮
        self.btn_download = wx.Button(self, label=u"下载")
        self.Bind(wx.EVT_BUTTON, self.OnDownload, self.btn_download)

        #使用布局
        mainSizer.Add(gridSizer, 0, wx.EXPAND)
        mainSizer.Add(self.btn_download, 0, wx.CENTER)
        mainSizer.Add(self.txt_log, 1, wx.EXPAND)

        self.SetSizerAndFit(mainSizer)

    def PrintLog(self, evt):
        self.txt_log.WriteText(w_dwp.getCodeStr(evt.value, 'utf-8').decode('utf-8'))

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
            style=wx.FD_OPEN
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

    def OnSaveBasename(self, evt):
        w_dwp.on_save_basename = not evt.IsChecked()
        if w_dwp.on_save_basename:
            self.txt_log.WriteText(u'文件名存储方式:使用原始文件名保存\n')
        else:
            self.txt_log.WriteText(u'文件名存储方式:使用路径名转换文件名保存\n')

    def OnDownload(self, evt):

        url = target_name = base_url = ''

        url = self.txt_url.GetValue()
        if url == "":
            dlg = wx.MessageDialog(self, u'请填写一个有效的目标网址!如:http://www.baidu.com',
                               u'请输入目标网址',
                               wx.OK | wx.ICON_INFORMATION)
            dlg.SetOKLabel(u'确定')
            dlg.ShowModal()
            dlg.Destroy()
            return

        local_file = self.get_local_filename()

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


class DwpFrame(wx.Frame):
    def __init__(self, *args, **kwargs):
        wx.Frame.__init__(self, *args, **kwargs)
        self.Center()
        self.SetIcon(icon_images.AppIcon.GetIcon())
        self.CreateStatusBar()

        self.setup_menu()


    def setup_menu(self):
        #文件菜单
        menu_file = wx.Menu()
        menu_sub_exit = menu_file.Append(wx.ID_EXIT, u'退出(&E)',u'退出程序')
        self.Bind(wx.EVT_MENU, self.MenuExit,  menu_sub_exit)
        #帮助菜单
        menu_help = wx.Menu()
        menu_sub_help = menu_help.Append(wx.ID_HELP, u"使用手册(&M)", u"程序使用手册")
        self.Bind(wx.EVT_MENU, self.MenuHelp,  menu_sub_help)
        menu_sub_about = menu_help.Append(wx.ID_ABOUT, u"关于(&A)", u"关于这个程序的信息")
        self.Bind(wx.EVT_MENU, self.MenuAbout,  menu_sub_about)

        menuBar = wx.MenuBar()
        menuBar.Append(menu_file, u"文件(&F)")
        menuBar.Append(menu_help, u"帮助(&H)")
        self.SetMenuBar(menuBar)


    def MenuAbout(self, evt):
        info = wx.AboutDialogInfo()
        info.SetName(app_info['name'])
        info.SetVersion(app_info['version'])
        #info.SetCopyright("walkskyer")
        info.SetDescription(wordwrap(
            app_info['description'],
            350, wx.ClientDC(self)))
        #info.SetWebSite(("http://www.zhangweijie.net", u"我的博客"))
        info.SetDevelopers(app_info['developers'])
        licenseText = u"请自由使用"
        info.SetLicense(wordwrap(licenseText, 500, wx.ClientDC(self)))

        # Then we call wx.AboutBox giving it that info object
        wx.AboutBox(info)

    def MenuExit(self, evt):
        self.Destroy()

    def MenuHelp(self, evt):
        msg = app_info['usage']
        dlg = wx.lib.dialogs.ScrolledMessageDialog(self, msg, u"使用手册")
        dlg.ShowModal()

class DwpMenuAction:
    def __init__(self, frame):
        self.frame = frame




if __name__ == "__main__":
    app = wx.App(False)
    frame = DwpFrame(None, title=app_info['name'], size=(600, 600))
    panel = DownloadPanel(frame)
    stdoutX = sys.stdout
    sys.stdout = DwpStdout(panel)
    frame.Show()
    app.MainLoop()
