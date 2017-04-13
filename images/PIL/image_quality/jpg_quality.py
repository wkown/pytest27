# -*- coding:utf-8 -*-
__author__ = 'walkskyer'
"""

"""
import os
import glob
from PIL import Image

if __name__ == "__main__":

    for i in glob.iglob('%s/*.jpg' % 'F:\WorkTemp\StaticPage\\rongrui\images'):
        print i
        im = Image.open(i)
        im.save(i, 'JPEG', quality = 80)

    for i in glob.iglob('%s/*.jpg' % 'F:\WorkTemp\StaticPage\\rongrui\static\images'):
        print i
        im = Image.open(i)
        im.save(i, 'JPEG', quality = 80)