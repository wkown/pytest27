# -*- coding:utf-8 -*-
__author__ = 'walkskyer'
"""
"""
from ghost import Ghost
if __name__ == "__main__":
    ghost = Ghost()
    with ghost.start(display=True) as session:
        page, extra_resources = session.open('https://2.taobao.com/')
        assert page.http_status == 200
        #session.show()
        print page.content

        page, extra_resources = session.open('https://s.2.taobao.com/list/list.htm?spm=2007.1000261.1867087.117.Ul3sEI&catid=50100406&st_trust=1&ist=1')
        assert page.http_status == 200
        # session.show()
        print page.content

        page, extra_resources = session.open('https://2.taobao.com/item.htm?spm=2007.1000337.16.4.dwOdst&id=530140067687')
        assert page.http_status == 200
        # session.show()
        print page.content.decode('gbk')