# -*- coding:utf-8 -*-
__author__ = 'walkskyer'
"""
HTML Title Retriever With Entity Support - chapter 7 - ctitle.py
"""
from htmlentitydefs import entitydefs
from HTMLParser import HTMLParser
import re
import sys


class TitleParser(HTMLParser):
    def __init__(self):
        self.taglevels = []
        self.handledtags = ['title', 'ul', 'li']
        self.processing = None
        HTMLParser.__init__(self)

    def handle_starttag(self, tag, attrs):
        """Called Whenever a start tag is encounted."""""
        if len(self.taglevels) and self.taglevels[-1] == tag:
            # Processing a previous version of this tag. close it out
            # and then start anew on this one.
            self.handle_endtag(tag)

        # Note that we're now processing this tag
        self.taglevels.append(tag)

        if tag in self.handledtags:
            # Only bother saving off the data if it's a tag we handle.
            self.data = ''
            self.processing = tag
            if tag == 'ul':
                print "List started."

    def handle_data(self, data):
        if self.processing:
            # Ordinaryly, this is slow and a bad practice, but
            # we can get away with it because a title is usually
            # small and simple.
            self.data += data

    def handle_endtag(self, tag):
        if not tag in self.taglevels:
            # We didn't have a start tag for this anyway. Just ignore.
            return

        while len(self.taglevels):
            # Obtain the last tag on the list and remove it
            starttag = self.taglevels.pop()

            # Finish processing it.
            if starttag in self.handledtags:
                self.finishprocessing(starttag)

            # If it's our tag, stop now.
            if starttag == tag:
                break
    def cleanse(self):
        """Removes extra whitespace from the document."""
        self.data = re.sub('\s+', ' ', self.data)

    def finishprocessing(self, tag):
        self.cleanse()
        if tag == 'title' and tag == self.processing:
            print "Document Title:", self.data
        elif tag == 'ul':
            print "List ended."
        elif tag == 'li' and tag == self.processing:
            print "List item:", self.data

        self.processing =None

    def handle_entityref(self, name):
        if entitydefs.has_key(name):
            self.handle_data(entitydefs[name])
        else:
            self.handle_data('&' + name + ';')
    def handle_charref(self, name):
        try:
            charnum = int(name)
        except ValueError:
            return

        if charnum < 1 or charnum > 255:
            return

        self.handle_data(chr(charnum))

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
    #fd.close()