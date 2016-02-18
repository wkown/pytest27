# -*- coding:utf-8 -*-
__author__ = 'walkskyer'
"""
pydns test 01
"""
import sys, DNS
if __name__ == "__main__":
    query = sys.argv[1]
    DNS.DiscoverNameServers()

    reqobj = DNS.Request()

    answerobj = reqobj.req(name=query, qtype=DNS.Type.ANY)
    if not len(answerobj.answers):
        print  "Not Found"
    for item in answerobj.answers:
        print "%-5s %s" % (item['typename'], item['data'])