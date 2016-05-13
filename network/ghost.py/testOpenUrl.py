# -*- coding:utf-8 -*-
__author__ = 'walkskyer'
"""
"""
from ghost import Ghost
if __name__ == "__main__":
    ghost = Ghost()
    while True:
        url = raw_input('give a url:')
        with ghost.start(display=True) as session:
            page, extra_resources = session.open(url)
            assert page.http_status == 200
            #session.show()
            print page.content
