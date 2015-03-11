# -*- coding:utf-8 -*-
__author__ = 'walkskyer'
"""
验证码识别之智能切割字符
http://blog.feshine.net/technology/1165.html
"""
import Image

if __name__ == "__main__":

    dir = "../tmp/"
    img = Image.open(dir + 'input-black.gif')

    # 初始化一个数组，统计横轴上每处的像素点数
    flagx = [0 for x in range(img.size[0])]
    pix = img.convert('RGB').load()

    #横坐标上的像素分布
    for x in range(img.size[0]):
        for y in range(img.size[1]):
            v=pix[x, y]
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
        x1,x2,y1,y2=i
        if (x2-x1)>7:
            x3=x1+8
            img.crop((x3, y1-1, x2+1, y2)).convert('RGB').save("font/%d.jpg" % x3)
            x2=x3-1
        img.crop((x1, y1-1, x2+1, y2)).convert('RGB').save("font/%d.jpg" % x1)