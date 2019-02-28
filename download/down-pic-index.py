# -*- coding:utf-8 -*-
__author__ = 'walkskyer'
"""
"""
import requests
import os, sys, getopt, argparse

url_pattern = ''
start_index = 1
end_index = 0
timeout = 60
output = "./pics"

parse = argparse.ArgumentParser()
parse.add_argument("-u", "--url-pattern", type=str, help="Url")
parse.add_argument("-s", "--start-index", default=1, type=int, help="Start Index default 1")
parse.add_argument("-e", "--end-index", default=0, type=int, help="End Index default 0")
parse.add_argument("-o", "--output", default="./pics", type=str, help="The output dir")
parse.add_argument("--timeout", default=60, type=int, help="Timeout")

args = parse.parse_args()
if args.url_pattern != "":
    url_pattern = args.url_pattern
if args.start_index:
    start_index = args.start_index
if args.end_index:
    end_index = args.end_index
if args.timeout:
    timeout = args.timeout
else:
    timeout = None
if args.output != "":
    output = args.output

if not os.path.isdir(output):
    os.mkdir(output)

for i in xrange(start_index, end_index+1):
    url = url_pattern.replace('*', str(i))
    print url
    filename = os.path.basename(url)
    path_file = "%s/%s" % (output, filename)
    if os.path.isfile(path_file):
        continue

    req = requests.get(url, timeout=timeout)
    if req.status_code != 200:
        print "Request Code: %s" % req.status_code
        continue

    with open(path_file, 'wb') as f:
        f.write(req.content)
        f.close()
    print "%s:from:%s  to: %s" % (i,url, path_file)