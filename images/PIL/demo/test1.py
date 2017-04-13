# -*- coding:utf-8 -*-
__author__ = 'walkskyer'
"""
验证码识别入门
http://blog.feshine.net/technology/1163.html
"""
import os, Image

if __name__ == "__main__":
    j = 1
    dir = "../tmp/"
    for f in os.listdir(dir):
        if f.endswith(".gif"):
            img = Image.open(dir + f)
            for i in range(8):
                x = 2 + i * 8
                y = 4
                img.convert('RGB').crop((x, y, x + 7, y + 11)).save("font/%d.jpg" % j)
                print "j=", j
                j += 1