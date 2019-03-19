# -*- coding:utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()
browser.get('https://www.baidu.com/')
print u"pageTitle：%s" % browser.title
print u"Tips:%s" % browser.find_element_by_css_selector("#su").get_attribute('value')
browser.find_element_by_css_selector("#kw").send_keys("google" + Keys.RETURN)

browser.implicitly_wait(10)
print "Url:%s" % browser.current_url
print u"pageTitle:%s" % browser.title

ele = browser.find_elements_by_css_selector("h3 a")
print ele
for e in ele:
    print e.text

# 删除内容
browser.find_element_by_css_selector("#kw").send_keys(Keys.BACKSPACE + Keys.BACKSPACE + Keys.BACKSPACE + Keys.BACKSPACE + Keys.BACKSPACE + Keys.BACKSPACE + Keys.BACKSPACE)
# 测试获取推荐关键词
browser.find_element_by_css_selector('#kw').send_keys(u"北京")
browser.implicitly_wait(10)
ele = browser.find_elements_by_css_selector(".bdsug ul li")
for e in ele:
    print e.get_attribute("data-key")
#browser.quit()
