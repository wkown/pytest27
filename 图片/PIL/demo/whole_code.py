#!/usr/bin/env python
# −*− coding: UTF−8 −*−
__author__ = 'walkskyer'
"""
完整处理代码
"""
import os, Image


def binary(f):
    """
    二值去噪
    :param f:
    :return:
    """
    img = Image.open(f)
    # img = img.convert('1')
    pixdata = img.load()
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
    return img


def division(img):
    """
    分割字符,并将分割的字符按顺序存入列表中
    :param img:
    :return:
    """
    font = []
    flagx = [0 for x in range(img.size[0])]
    pix = img.convert('RGB').load()

    # 横坐标上的像素分布
    for x in range(img.size[0]):
        for y in range(img.size[1]):
            v = pix[x, y]
            if pix[x, y][0] < 90:
                flagx[x] += 1
    print flagx

    result = list()
    for i in range(img.size[0]):
        if flagx[i] > 0 and flagx[i - 1] <= 0:
            tmp = i  #记录0->n的坐标
        if flagx[i] > 0 and ( len(flagx)==(i+1) or flagx[i + 1] <= 0):
            #完成一个字符的横坐标扫描，针对这段用同样的方法扫描纵坐标
            flagy = [0 for x in range(img.size[1])]
            for y in range(img.size[1]):
                for x in range(i + 1)[tmp:]:
                    if pix[x, y][0] < 90:
                        flagy[y] += 1
            #用flagy记录纵坐标像素分布
            for j in range(img.size[1]):
                if flagy[j] > 0 and flagy[j - 1] <= 0:
                    ttmp = j  #记录0->n的点
                if flagy[j] > 0 and flagy[j + 1] <= 0:
                    result.append([tmp, i, ttmp + 1, j + 1])
    print result

    for i in result:
        x1, x2, y1, y2 = i
        x3 = 0
        if (x2 - x1) > 8:
            x3 = x2
            x2 = x1 + 7
        font.append(img.crop((x1, y1 - 1, x2 + 1, y2)).convert('RGB'))
        if x3 > 0:
            font.append(img.crop((x1 + 8, y1 - 1, x3 + 1, y2)).convert('RGB'))
    return font


def recognize(img):
    """
    匹配验证码
    :param img:
    :return:
    """
    fontMods = []
    for i in range(10):
        fontMods.append((str(i), Image.open("./font/use/%d.jpg" % i)))
    fontMods.append((str('-'), Image.open("./font/use/%s.jpg" % '-')))
    fontMods.append((str('0'), Image.open("./font/use/%s.jpg" % '0_1')))
    fontMods.append((str('*'), Image.open("./font/use/%s.jpg" % 'star')))
    result = ""
    font = division(img)
    for i in font:
        target = i
        points = []
        for mod in fontMods:
            diffs = 0
            #如果尺寸不一致，先算上尺寸上不同的数量
            if abs(target.size[0]-mod[1].size[0])>1 or abs(target.size[1]-mod[1].size[1])>1:
                diffs = abs((target.size[0]*target.size[1])-(mod[1].size[0]*mod[1].size[0]))

            for yi in xrange(target.size[1]):
                try:
                    for xi in xrange(target.size[0]):
                        if mod[1].getpixel((xi, yi)) != target.getpixel((xi, yi)):
                            diffs += 1
                except IndexError, e:
                    #print e
                    pass
            points.append((diffs, mod[0]))
        points.sort()
        result += points[0][1]
    return result


if __name__ == '__main__':
    codedir = "../test/"
    count=1
    for imgfile in os.listdir(codedir):
        if imgfile.endswith(".jpg"):
            print "count:%s" % count
            dir = "./result/"
            print imgfile
            img = binary(codedir + imgfile)
            num = recognize(img)
            file_name,ext=imgfile.split('.')
            dir += (file_name+'_'+num +".png")
            print "save to", dir
            img.save(dir)
            count+=1