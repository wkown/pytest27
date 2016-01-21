# -*- coding:utf-8 -*-
__author__ = 'walkskyer'
"""

"""
import os
import urllib
from bs4 import BeautifulSoup

if __name__ == "__main__":

    url_root = 'http://codeigniter.org.cn/userguide2/'
    url_list = 'http://codeigniter.org.cn/userguide2/toc.html'
    path_root = 'CodeIgniter2.2.6-user_guide-html'
    index_soup = BeautifulSoup(urllib.urlopen(url_list))
    for url in index_soup.select("a"):
        if not url.has_key('href') or not (url['href'].startswith('./') or url['href'].startswith(url_root)):
            continue
        if url['href'].startswith('./'):
            curr_url = url['href']
        else:
            curr_url = url['href'].replace(url_root, '/')
        print curr_url

        abs_url = "%s%s" % (url_root, curr_url)
        relative_path = os.path.dirname(curr_url)
        curr_path = "%s/%s" % (path_root, relative_path)
        print relative_path
        print relative_path.split('/')
        print len(relative_path.split('/'))

        target_file = '%s/%s' % (path_root, curr_url)
        if os.path.isfile(target_file):
            continue
        if not os.path.isdir(curr_path):
            os.makedirs(curr_path)

        level_path = ''
        if relative_path != '/':
            level_path = '%s/' % '/'.join(['..' for i in xrange(len(relative_path.split('/'))-1)])

        curr_content = urllib.urlopen(abs_url).read()
        curr_content = curr_content.replace('http://codeigniter.org.cn/userguide2/../images/design/favicon.ico','%s%s' % (level_path, 'favicon.ico'))
        curr_content = curr_content.replace(url_root,level_path)
        f = open(target_file,'w')
        f.write(curr_content)
        f.close()
