# -*- coding:utf-8 -*-
__author__ = 'walkskyer'
"""
"""

import  urllib
import re
import os

if __name__ == "__main__":
    raw_url = raw_input('input a url : ').strip()
    if not  raw_url:
        exit(0)

    content = urllib.urlopen(raw_url).read()

    with open('html/index.html', 'wb') as html_file:
        html_file.write(content)
        html_file.close()


    matches = re.findall('<a.*?href="(.*?)".*?>',content,re.DOTALL)

    baseUrl = os.path.dirname(raw_url)

    for match in matches:
        print match
        if not match.endswith('.html') or match=='index.html':
            continue

        dir = os.path.dirname(match)
        if not os.path.isdir('html/'+dir):
            os.mkdir('html/'+dir)

        with open('html/'+match, 'wb') as f:
            f.write(urllib.urlopen(baseUrl+'/'+match).read())
            f.close()