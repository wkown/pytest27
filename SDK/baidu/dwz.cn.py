# -*- coding:utf-8 -*-
__author__ = 'walkskyer'
"""
"""
import requests, json



def shortUrl(longUrl):
    if len(longUrl) == 0:
        return None
    dwzUrl="http://dwz.cn/create.php"
    data = {
        "access_type": "web",
        "alias": "",
        "url": longUrl
    }
    resp = requests.post(dwzUrl, data)
    if resp.status_code == 200:
        return resp.content

if __name__ == "__main__":
    while True:
        url = raw_input("Input a long url:").strip()
        '''if len(url) == 0 or not url.startswith("http://") or not url.startswith("http://"):
            print "Invalid Url!"
            continue'''
        data = shortUrl(url)
        print json.loads(data)