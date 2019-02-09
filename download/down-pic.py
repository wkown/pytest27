# -*- coding:utf-8 -*-
__author__ = 'walkskyer'
"""
"""
import urllib
import os

url_pattern = raw_input("url pattern: ")
start_index = 1
end_index = raw_input("end index: ")
end_index = int(end_index)

target_dir = "./pics"
if not os.path.isdir(target_dir):
    os.mkdir(target_dir)

for i in xrange(start_index, end_index+1):
    url = url_pattern.replace('*', str(i))
    print url

    pic = urllib.urlopen(url)
    filename = os.path.basename(url)
    path_file = "%s/%s" % (target_dir, filename)
    with open(path_file, 'wb') as f:
        f.write(pic.read())
        f.close()
    print "%s:from:%s  to: %s" % (i,url, path_file)