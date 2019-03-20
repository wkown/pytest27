# -*- coding:utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()
browser.get('https://weibo.com/?category=1760')
browser.implicitly_wait(10)
#browser.execute_script("document.documentElement.scrollTop=10000")
footer = browser.find_element_by_css_selector('.footer_link')
browser.execute_script("arguments[0].scrollIntoView();", footer)
browser.implicitly_wait(20)
print u"pageTitle：%s" % browser.title
h3 = browser.find_elements_by_css_selector('h3.list_title_b')
urls = []
for e in h3:
    anchor = e.find_element_by_css_selector('a')
    urls.append((anchor.text, anchor.get_attribute('href')))
    print anchor.text
#exit(0)

def get_content(url_info):
    print "%s:%s" % (url_info[0], url_info[1])
    browser.get(url_info[1])
    browser.implicitly_wait(10)
    try:
        x = browser.find_element_by_css_selector('.WB_artical_del').text
        return
    except Exception, e:
        pass

    org = browser.find_element_by_css_selector('.W_autocut').text
    try:
        authorEle = browser.find_element_by_css_selector('.author2in')
        author = authorEle.text
    except Exception, e:
        print e
        author = ''
    time = browser.find_element_by_css_selector('.time').text
    try:
        srcUrl = browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div/div/div/div/div[2]/div[2]/div[1]/span[5]/a').get_attribute('href')
    except Exception, e:
        print e
        srcUrl = ''
    content = browser.find_element_by_css_selector('.WB_editor_iframe_new').text
    print "org:%s|author:%s|time:%s|srcUrl:%s" % (org, author, time, srcUrl)
    print content


for u in urls:
    get_content(u)


#browser.quit()