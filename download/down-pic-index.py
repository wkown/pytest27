# -*- coding:utf-8 -*-
__author__ = 'walkskyer'
"""
"""
import requests
import os, sys, getopt

url_pattern = ''
start_index = 1
end_index = 0

def usage():
    print "usage:"
    sys.exit()

try:
    opts, args = getopt.getopt(sys.argv[1:], 'hu:s:e:', ["url-pattern=", "start-index=", "end-index="])
except getopt.GetoptError:
    usage()

if not len(opts):
    usage()

for opt, argv in opts:
    if opt in ("-h"):
        usage()
    if opt in ("-u", "--url-pattern"):
        url_pattern = argv
    if opt in ("-s", "--start-index"):
        start_index = argv
    if opt in ("-e", "--end-index"):
        end_index = int(argv)

target_dir = "./pics"
if not os.path.isdir(target_dir):
    os.mkdir(target_dir)

for i in xrange(start_index, end_index+1):
    url = url_pattern.replace('*', str(i))
    print url
    filename = os.path.basename(url)
    path_file = "%s/%s" % (target_dir, filename)
    if os.path.isfile(path_file):
        continue

    req = requests.get(url)
    with open(path_file, 'wb') as f:
        f.write(req.content)
        f.close()
    print "%s:from:%s  to: %s" % (i,url, path_file)