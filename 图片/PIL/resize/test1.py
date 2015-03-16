# -*- coding:utf-8 -*-
__author__ = 'walkskyer'
"""
等比例缩放
"""
import Image
import os

if __name__ == "__main__":
    infile = raw_input('give me a file with path:')

    new_width = raw_input('give me the with you will convert:')  # 200
    new_width = float(new_width)
    img = Image.open(infile)
    img_size = img.size  # PIL的size属性结构：(width, height)
    new_height = new_width * img_size[1] / img_size[0]
    new_image = img.resize((int(new_width), int(new_height)))
    new_image.save("%s/convert_%s" % (os.path.dirname(infile), os.path.basename(infile)))