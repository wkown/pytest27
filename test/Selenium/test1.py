# -*- coding:utf-8 -*-
__author__ = 'walkskyer'
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
"""
test1
"""

if __name__ == "__main__":

    browser = webdriver.Chrome()

    browser.get('http://www.baidu.com')
    assert u'百度' in browser.title

    elem = browser.find_element_by_name('wd')  # Find the search box
    elem.send_keys(u'app 开发' + Keys.RETURN)
    result_elem = browser.find_element_by_css_selector('.s_tab a')
    print result_elem
    print result_elem.text
    result_elem.click()
    #result_elem.send_keys(Keys.)

    #browser.quit()