# -*- coding:utf-8 -*-
__author__ = 'walkskyer'
"""
python图像处理之二值去噪
来源:http://blog.feshine.net/technology/1164.html
"""
from PIL import Image
def binary(filename):
    img = Image.open(filename) # 读入图片
    img = img.convert("RGBA")
    pixdata = img.load()
    #二值化
    for y in xrange(img.size[1]):
        for x in xrange(img.size[0]):
            if pixdata[x, y][0] < 90:
                pixdata[x, y] = (0, 0, 0, 255)
    for y in xrange(img.size[1]):
        for x in xrange(img.size[0]):
            if pixdata[x, y][1] < 136:
                pixdata[x, y] = (0, 0, 0, 255)
    for y in xrange(img.size[1]):
        for x in xrange(img.size[0]):
            if pixdata[x, y][2] > 0:
                pixdata[x, y] = (255, 255, 255, 255)
    img.save("../tmp/input-black.gif", "GIF")
    #放大图像 方便识别
    #im_orig = Image.open('tmp/input-black.jpg')
    #big = im_orig.resize((1000, 500), Image.NEAREST)

if __name__ == "__main__":
    while True:
        file_name=raw_input('filename:')
        binary('../pic/%s.jpg' % file_name)