# -*- coding:utf-8 -*-
__author__ = 'walkskyer'
"""
下载手册
url:http://www.runoob.com/sitemap
"""
from bs4 import BeautifulSoup
import os
import urllib
import time


def download(filename, content_url):
    tmp_dir = os.path.dirname(filename)
    if len(tmp_dir) > 0 and not os.path.isdir(tmp_dir):
        os.mkdir(tmp_dir)
    print 'content_url:', content_url
    try:
        file_content = urllib.urlopen(content_url).read()
    except Exception, e:
        print 'timeout:',e
        time.sleep(20)
        download(filename, content_url)
        pass
    print 'dowloaded:', content_url
    f = open(filename, 'wb')
    f.write(file_content)
    f.close()

if __name__ == "__main__":
    first_url = r'http://www.runoob.com/sitemap'
    base_url = os.path.dirname(first_url)
    first_soup = BeautifulSoup(urllib.urlopen(first_url).read())
    if not os.path.isdir('html'):
        os.mkdir('html')
    os.chdir('html')
    root_path = os.getcwd()
    for i in first_soup.find_all('a'):
        if (not i.has_key('href')) or (not (i['href'].endswith('html') or i['href'].endswith('htm'))):
            continue

        print i['href']
        os.chdir(root_path)
        print os.getcwd()
        dir = os.path.dirname(i['href'])
        if not os.path.isdir(dir):
            os.mkdir(dir)

        file_name = os.path.basename(i['href'])
        cat_url='%s/%s' % (base_url, i['href'])
        print 'cat_url:',cat_url

        cat_content=urllib.urlopen(cat_url).read()
        if not os.path.isfile(i['href']):
            f = open(i['href'], 'wb')
            f.write(cat_content)
            f.close()

        os.chdir(dir)
        print os.getcwd()

        cat_soup = BeautifulSoup(cat_content)
        leftcolumn = cat_soup.find('div',{'id':'leftcolumn'})
        if leftcolumn is None:
            continue
        for k in leftcolumn.find_all('a'):
            if (not k.has_key('href')) or (not (k['href'].endswith('html') or k['href'].endswith('htm'))):
                continue

            #time.sleep(2)
            print k['href']
            if not os.path.isfile(k['href']):
                href=k['href']
                if k['href'].find('\\'):
                    href=os.path.basename(k['href'])
                download(href,'%s/%s/%s' % (base_url, dir, href))
            else:
                print 'file existed'
            time.sleep(0.5)



