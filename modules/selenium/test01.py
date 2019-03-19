# -*- coding:utf-8 -*-
from selenium import webdriver

browser = webdriver.Firefox()
browser.get('https://www.baidu.com/')
print u"pageTitle：%s" % browser.title
print u"Tips:%s" % browser.find_element_by_css_selector("#su").get_attribute('value')
browser.quit()
