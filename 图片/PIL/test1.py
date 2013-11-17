# -*- coding:utf-8 -*-
__author__ = 'weijie'
from PIL import Image
"""将图片按等比例放缩"""
path = r'C:\Users\weijie\Pictures\[Avy][58P]'
im = Image.open(path + '\\0000.jpg')
size = im.size
print size
if size[0] > size[1]:
    rate = float(1200) / float(size[0])
else:
    rate = float(900) / float(size[1])
print rate
new_size = (int(size[0] * rate), int(size[1] * rate))
print new_size
new = im.resize(new_size, Image.BILINEAR)
new.save(path + '\\0000.small.jpg')

"""图片等宽或等高放缩"""
im = Image.open(path + '\\0038.jpg')
width = height = float(200)#目标宽度
size = im.size
print size
'''按照较大的缩小'''
if size[0] > size[1]:
    rate = width / float(size[0])
    new_size = (int(width), int(size[1] * rate))
else:
    rate = height / float(size[1])
    new_size = (int(size[0] * rate), int(width))
print rate
print new_size
new = im.resize(new_size, Image.BILINEAR)
new.save(path + '\\0038.small.jpg')