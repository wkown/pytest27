# -*- coding:utf-8 -*-
__author__ = 'walkskyer'
"""
HTML Title Retriever With Entity Support - chapter 7 - etitle.py
"""
from htmlentitydefs import entitydefs
from HTMLParser import HTMLParser
import sys


class TitleParser(HTMLParser):
    def __init__(self):
        self.title = ''
        self.readingtitle = 0
        HTMLParser.__init__(self)

    def handle_starttag(self, tag, attrs):
        if tag == 'title':
            self.readingtitle = 1

    def handle_data(self, data):
        if self.readingtitle:
            # Ordinaryly, this is slow and a bad practice, but
            # we can get away with it because a title is usually
            # small and simple.
            self.title += data

    def handle_endtag(self, tag):
        if tag == 'title':
            self.readingtitle = 0

    def handle_entityref(self, name):
        if entitydefs.has_key(name):
            self.handle_data(entitydefs[name])
        else:
            self.handle_data('&' + name + ';')

    def gettitle(self):
        return self.title

if __name__ == "__main__":
    if len(sys.argv) >= 2:
        filename = sys.argv[1]
    else:
        filename = raw_input('Give me a file name:')
    fd = open(filename)
    tp = TitleParser()
    tp.feed(fd.read())
    print "Title is:" , tp.gettitle()
    #fd.close()