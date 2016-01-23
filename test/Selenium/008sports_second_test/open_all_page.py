# -*- coding:utf-8 -*-
__author__ = 'walkskyer'
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

"""

"""

if __name__ == "__main__":
    root_url = 'http://www.008sports.com.zwj/second'
    pages = (
    'list_association', 'list_constitution', 'list_platform', 'list_sport', 'list_sportnext', 'show_test', 'show_test2',
    'show_test3', 'show_test4', 'show_test5', 'show_test6', 'show_test7', 'show_test8', 'show_test9', 'show-news')

    browser = webdriver.Chrome()
    while True:
        for page in pages:
            browser.get('%s/%s' % (root_url, page))
            time.sleep(30)
            #browser.close()
            time.sleep(0.5)

    browser.close()
