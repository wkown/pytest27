# -*- coding:gbk -*-
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
import sys

pattern = {
    'js': re.compile(r'<script.*?src=[\'\"](.*?)[\'\"].*?></script>', re.IGNORECASE),
    'css': re.compile(r'<link.*?href=[\'\"](.*?)[\'\"].*?>', re.IGNORECASE),
    'page_image': re.compile(r'<img.*?src=[\'\"](.*?)[\'\"].*?>', re.IGNORECASE),
    'css_image': re.compile(r'url\([\'\"]?(.*?)[\'\"]?\)', re.IGNORECASE),
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
    filename = os.path.basename(v.strip())

    pos = filename.find('?')
    if (pos) != -1:
        filename = filename[0: pos]
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
    root_path = '%s://%s' % (url_info.scheme, url_info.netloc)
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
        filename = wk_basename(v.strip())
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
    url = url.strip().replace('\'', '').replace('"', '')
    url = real_url(url, base_url)

    print "download: %s <br>\n" % url
    file_put_contents(filename, file_get_contents(url))


def file_put_contents(filename, content):
    """
    write something to a file
    :param filename:
    :param content:
    :return:
    """
    f = open(filename, 'wb')
    f.write(content)
    f.close()


def file_get_contents(url):
    """
    read the file content
    :param url:
    :return:
    """
    if url.find('http://') != -1:
        return urllib.urlopen(url).read()
    f = open(url, 'rb')
    content = f.read()
    f.close()
    return content


def replace_source_file_path(matchObj):
    """
    替换
    :param matchObj:
    :return:
    """
    match = matchObj.group(1)
    if not match:
        return ''
    return matchObj.group(0).replace(match, dirs[k] + '/' + wk_basename(match))


def replace_inner_source_file_path(matchObj):
    match = matchObj.group(1)
    if not match:
        return ''
    return matchObj.group(0).replace(match, inner_files['css']['dir'] + '/' + wk_basename(match))


if __name__ == "__main__":
    # url = 'http://www.273.cn/mobile'
    print 'This tools is used to download one page from the online web site to your local host.It will download the page struct ,js,css And images.And powered by walkskyer ^_^'

    url = ''
    if len(sys.argv) <= 1:
        while len(url) <= 0:
            url = raw_input('please input a url:')

    if url.find(r'://') == -1:
        url = 'http://%s' % url

    print  'We will download the page use this url:%s' % url

    if not os.path.isdir('html'):
        os.mkdir('html')
    os.chdir('html')

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
        files1 = v.findall(content)
        print files1
        if not files1:
            continue

        download_filse(files1, dirs[k], base_url)
        # return str_replace(match[1],dirs[k].'/'.wk_basename(match[1]),match[0])
        page_content = v.sub(replace_source_file_path, page_content)

        if k == 'css':  #如果是css 还要下载css中引用的文件
            for css_file in files1:
                css_content = file_get_contents('css/' + wk_basename(css_file))
                css_matches = inner_files['css']['pattern'].findall(css_content)
                if css_matches:
                    download_filse(css_matches, dirs['css_image'], real_url(os.path.dirname(css_file), base_url))
                    css_content = inner_files['css']['pattern'].sub(replace_inner_source_file_path, css_content)
                    file_put_contents('css/' + wk_basename(css_file), css_content)

    file_put_contents(base_name, page_content)
