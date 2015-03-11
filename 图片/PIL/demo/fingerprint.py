# -*- coding:utf-8 -*-
__author__ = 'walkskyer'
"""
生成获取图像信息横坐标的指纹
实际匹配会遇到难度
"""
import Image

if __name__ == "__main__":
    dir = "../tmp/"
    img = Image.open(dir + 'input-black.gif')

    # 初始化一个数组，统计横轴上每处的像素点数
    flagx = [0 for flag in range(img.size[0])]
    pix = img.convert('RGB').load()

    #横坐标上的像素分布
    for flag in range(img.size[0]):
        for y in range(img.size[1]):
            if pix[flag, y][0] < 90:
                flagx[flag] += 1
    print flagx

    fingerprint=list()
    flag=False
    end=start=-1
    for i in xrange(len(flagx)):
        print "%s:%s" % (i,flagx[i])
        if flagx[i]>0 and not flag:
            start=i
            flag=True

        if flagx[i]==0 and flag:
            end=i
        if start>=0 and end >start:
            x_end=0
            if end-start>9:
                x_end=end
                end=start+8
            fingerprint.append(flagx[start:end])
            if x_end:
                fingerprint.append(flagx[start+8:x_end])
            start=end=-1
            flag=False

    print fingerprint