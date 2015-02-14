# -*- coding:utf-8 -*-
__author__ = 'walkskyer'
"""
下载整个网页资源文件及结构
移植自php脚本
20150214
"""
import re
import urllib
import os
from urlparse import urlparse

pattern = {
    'js': re.compile('<script.*?src="(.*?)".*?></script>', re.IGNORECASE),
    'css': re.compile('<link.*?href="(.*?)".*?>', re.IGNORECASE),
    'page_image': re.compile('<img.*?src="(.*?)".*?>', re.IGNORECASE),
    'css_image': re.compile('url\((.*?)\)', re.IGNORECASE),
}
dirs = {'js': 'js',
        'css': 'css',
        'page_image': 'images',
        'css_image': 'images',
        'inner_css': '../images'
}
inner_files = {'css': {'pattern': re.compile('url\([\'\"]?(.*?)[\'\"]?\)', re.IGNORECASE), 'dir': '../images'}}


def wk_basename(v):
    """
    获取文件名
    :param v:
    :return:
    """
    filename = os.path.basename(v.trim())

    pos = filename.find('?')
    if (pos) != False:
        filename = filename[0, pos]
    return filename


def real_url(uri, base_url=''):
    """
    返回真实的url
    :param uri:
    :param base_url:
    :return:
    """
    if uri.find('//') == False or uri.find('http://') == False:
        return uri

    url_info = urlparse(base_url)
    root_path = '%s://%s' % (url_info['scheme'], url_info['netloc'])
    if uri[0] == '/':
        uri = root_path + uri
    elif uri == '.':
        uri = base_url
    else:
        uri = base_url + '/' + uri
    return uri


def download_filse(file_list, dir, base_url=''):
    """
    下载文件列表
    :param file_list:
    :param dir:
    :param base_url:
    :return:
    """
    if not os.path.isdir(dir):
        print 'curr dir: %s and I will make dir： %s<br>\n' % (os.getcwd(), dir)
        os.mkdir(dir)

    for v in file_list:
        filename = wk_basename(v.trim());
        print "%s_filename:%s<br>\n" % (dir, filename)
        download_file(dir + '/' + filename, v, base_url)


def download_file(filename, url, base_url=''):
    """
    下载文件
    :param filename:
    :param url:
    :param base_url:
    :return:
    """
    url = url.trim().replace('\'', '').replace('"', '')
    url = real_url(url, base_url)

    print "download: %s <br>\n" % url
    file_put_contents(filename, file_get_contents(url))


def file_put_contents(filename, content):
    f = open(filename, 'wb')
    f.write(content)
    f.close()


def file_get_contents(url):
    return urllib.urlopen(url).read()


if __name__ == "__main__":
    url = 'http://www.273.cn/mobile/#'

    url_info = urlparse(url)
    root_path = '%s://%s' % (url_info.scheme, url_info.netloc)
    base_url = os.path.dirname(url)
    base_name = os.path.basename(url)
    pos = int(base_name.find('.'))
    if pos is -1:
        ext = None
    else:
        ext = base_name[pos + 1]
    if ext not in ('html', 'htm', 'php', 'asp', 'jsp', 'aspx'):
        base_url = url[0:url.rfind('/')]
        base_name = 'index.html'

    page_content = file_get_contents(url)

    content = file_get_contents(url)
    for k, v in pattern.items():
        matches = v.findall(content)
        print matches

