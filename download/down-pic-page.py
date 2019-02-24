# -*- coding:utf-8 -*-
__author__ = 'walkskyer'
"""
"""

import os,sys,getopt,requests,json
import html5lib
from lxml import etree
import re
from collections import deque
from urlparse import urljoin

url = ""
cookie = ""
pic_selector = ""
url_selector = ""
target_dir = "./pics"

def usage():
    print "usage:"
    sys.exit()

def get_url(url):
    r = requests.get(url,cookies=cookies)
    print r.encoding
    s=getCodeStr(r.text)
    #print s
    p = re.compile(r'<a href=\'(.*?)\'><img alt="" src=\'(.*?)\' /></a></div>')
    m = p.findall(s)
    print m
    for next, pic_url in m:
        yield next, pic_url

# convert encoding
def getCodeStr(result, target_charset='utf-8'):
    #gb2312
    try:
        myResult = result.decode('gb2312').encode(target_charset, 'ignore')
        return myResult
    except:
        pass
        #utf-8
    try:
        myResult = result.decode('utf-8').encode(target_charset, 'ignore')
        return myResult
    except:
        pass

    #unicode
    try:
        myResult = result.encode(target_charset, 'ignore')
        return myResult
    except:
        pass
        #gbk
    try:
        myResult = result.decode('gbk').encode(target_charset, 'ignore')
        return myResult
    except:
        pass
        #big5
    try:
        myResult = result.decode('big5').encode(target_charset, 'ignore')
        return myResult
    except:
        pass

if __name__ == "__main__":

    try:
        opts, args = getopt.getopt(sys.argv[1:], "hu:c:s:U:", ["url=", "cookie=","pic-selector=","url-selector="])
    except getopt.GetoptError:
        usage()

    if not len(opts):
        usage()

    for opt, argv in opts:
        if opt == "-h":
            usage()
        if opt in ("-u", "--url"):
            url = argv
        if opt in ("-c", "--cookie"):
            cookie = argv
        if opt in ("-s", "--pic-selector"):
            pic_selector = argv
        if opt in ("-s", "--url-selector"):
            url_selector = argv

    cookies = json.loads(cookie)

    if not os.path.isdir(target_dir):
        os.mkdir(target_dir)

    que = deque([url])
    base_url = url

    while len(que):
        url = que.popleft()
        for next_url, pic_url in get_url(url):
            if next_url:
                que.append(urljoin(base_url, next_url))
            if pic_url:
                pic_req = requests.get(pic_url)
                if pic_req.status_code != 200:
                    print "###### ERROR ###### url: %s, pic_url: %s" % (url, pic_url)
                filename = "%s/%s" % (target_dir, os.path.basename(pic_url))
                if os.path.isfile(filename):
                    continue
                with open(filename,'wb') as f:
                    f.write(pic_req.content)
                    f.close()

