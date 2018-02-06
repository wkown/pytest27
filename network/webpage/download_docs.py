# -*- coding:utf-8 -*-
__author__ = 'walkskyer'
"""
下载整站静态页晚间处理还有待优化20180206
"""

import  urllib
import re
import os
import DownloadsWebPage as w_dwp

if __name__ == "__main__":
    raw_url = raw_input('input a url : ').strip()
    if not  raw_url:
        exit(0)

    content = urllib.urlopen(raw_url).read()

    w_dwp.run_download(raw_url, os.path.dirname(raw_url),'index.html')


    matches = re.findall('<a.*?href="(.*?)".*?>',content,re.DOTALL)

    baseUrl = os.path.dirname(raw_url)
    baseDir = w_dwp.target_root_dir
    for match in matches:
        print match
        if not match.endswith('.html') or match=='index.html':
            continue

        dir = os.path.dirname(match)
        file_url = baseUrl+'/'+match
        w_dwp.target_root_dir = baseDir + '/'+dir
        w_dwp.run_download(file_url, os.path.dirname(file_url), os.path.basename(file_url))