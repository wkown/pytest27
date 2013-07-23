#coding=utf-8
'''
@lan_scan_v2.0
@测试时间：2013-7-21
1.扫描、汇总局域网网络在线主机情况；
2.目前只是列出了丢包率小于100%的主机iP地址，暂未对扫描结果进行进一步分析，下一步强化一下；
3.还是使用了icmp进行扫描，效率不是很高，不知道有没有更高效的方法；
4.对这个代码生成的exe文件、配合”发送扫描大楼局域网主机情况附件邮件.vbs“将扫描结果文件发送到了邮箱中

5.增加统计在线主机数量结果的写入
6.使用简单的raw_input(),让用户选择扫描何段地址，like:01 02 03
7.随后，找个方法，试着让用户自行输入要扫描的网络地址段
http://www.oschina.net/code/snippet_1174858_23088
'''

import ping_pip
from fractions import Fraction
import os
import sys
import re
import time
import random
#from __future__ import division
reload(sys)
sys.setdefaultencoding('utf-8')
'''在测试开始，打印测试开始时间，并写入result文件中去'''
testtime=time.strftime('%Y-%m-%d %H:%M:%S')
print testtime


def proc_write_begin(Lanscanoutputs):

    Lanscanoutputs.write('\n')
    Lanscanoutputs.write('*'*35),Lanscanoutputs.write("lan_scan_v2.0"),Lanscanoutputs.write('*'*36),Lanscanoutputs.write('\n')
    testtime_begin=time.strftime('%Y-%m-%d %H:%M:%S')
    Lanscanoutputs.write("The task of 'Scaning Lans' begined at:"+testtime_begin)
    Lanscanoutputs.write('\n')
    Lanscanoutputs.write("扫描开始........")
    Lanscanoutputs.write('\n')
    Lanscanoutputs.write("在线主机如下：")
    Lanscanoutputs.write('\n')
    Lanscanoutputs.write('*'*80)
    Lanscanoutputs.write('\n')

def proc_write_end(Lanscanoutputs):
    Lanscanoutputs.write('*'*80)
    Lanscanoutputs.write('\n')
    Lanscanoutputs.write("测试结束。")
    Lanscanoutputs.write('\n')
    testtime_end=time.strftime('%Y-%m-%d %H:%M:%S')
    Lanscanoutputs.write("The task of 'Scaning Lans' ended at:"+testtime_end)
    print "The Lanscanoutputs have saved as the filename of: {} for you to check.".format(Lanscanoutputs)




def one_lan_scan(Lanscanoutputs):
    '''只测试一个lan(局域网)'''
    for i in range(1,254):
        s1="214.186.4.%s" %i
        #s1="10.246.190.%s" %i
        '''丢包率小于100时，才写入Lanscanoutputs*文件中'''
        if ping_pip.quiet_ping(s1)[0]<100:
            Lanscanoutputs.write(s1)
            Lanscanoutputs.write('\n')
        else:
            pass



def more_lan_scan(Lanscanoutputs):
    '''测试若干段lan(局域网)，回头试试能不能直接让用户输入开始地址、结束地址'''

    for i in range(4,30):
        for j in range(1,127):
            s1="214.186.%s.%s" %(i,j)
            '''丢包率小于100时，才写入Lanscanoutputs*文件中'''
            if ping_pip.quiet_ping(s1)[0]<100:
                Lanscanoutputs.write(s1)
                Lanscanoutputs.write('\n')
            else:
                pass


def lan_scan_of_AF01(Lanscanoutputs):
    '''扫描：214.186.4.0网段lan(管理网)'''
    '''AF=Address Field'''
    for i in range(1,3):
        s1="214.186.4.%s" %i
        #s1="10.246.190.%s" %i
        '''丢包率小于100时，才写入Lanscanoutputs*文件中'''
        if ping_pip.quiet_ping(s1)[0]<100:
            Lanscanoutputs.write(s1)
            Lanscanoutputs.write('\n')
        else:
            pass

def lan_scan_of_AF02(Lanscanoutputs):
    '''扫描：10.246.190.0网段lan(局域网)'''
    for i in range(1,3):
        s1="10.246.190.%s" %i
        '''丢包率小于100时，才写入Lanscanoutputs*文件中'''
        if ping_pip.quiet_ping(s1)[0]<100:
            Lanscanoutputs.write(s1)
            Lanscanoutputs.write('\n')
        else:
            pass

def lan_scan_of_AF03(Lanscanoutputs):
    '''扫描：10.246.191.0网段lan(局域网)'''
    for i in range(1,3):
        s1="10.246.191.%s" %i
        '''丢包率小于100时，才写入Lanscanoutputs*文件中'''
        if ping_pip.quiet_ping(s1)[0]<100:
            Lanscanoutputs.write(s1)
            Lanscanoutputs.write('\n')
        else:
            pass

def lan_scan_of_AF04(Lanscanoutputs):
    '''测试若干段lan(局域网)，回头试试能不能直接让用户输入开始地址、结束地址'''
    '''扫描：214.186.4.0-214.186.29.254 网段lan(管理网)'''

    for i in range(4,6):
        for j in range(1,3):
            s1="214.186.%s.%s" %(i,j)
            '''丢包率小于100时，才写入Lanscanoutputs*文件中'''
            if ping_pip.quiet_ping(s1)[0]<100:
                Lanscanoutputs.write(s1)
                Lanscanoutputs.write('\n')
            else:
                pass

def proc_results(s):
    Lanscanoutputs="Lanscanputs_%s_%s.txt" %(time.strftime('%Y-%m-%d'),random.uniform(1,5))
    Lanscanoutputs=open(Lanscanoutputs,'w')
    Lanscanoutputs.write(s)


Lanscanoutputs="Lanscanputs_%s_%s.txt" %(time.strftime('%Y-%m-%d'),time.strftime('%H-%M-%S'))
Lanscanoutputs=open(Lanscanoutputs,'w')
proc_write_begin(Lanscanoutputs)
"""开始判断扫描哪个网络地址段"""
print "AF01----starting to scan 214.186.4.0"
print "AF02----starting to scan 10.246.190.0"
print "AF03----starting to scan 10.246.191.0"
print "AF04----starting to scan 214.186.4.0-214.186.29.254"

print "please choose from AF01,AF02,AF03,AF04......"

af=raw_input("Your choose >")
af=af.upper()
if af=="AF01":
    print "starting to scan AF01---214.186.4.0"
    lan_scan_of_AF01(Lanscanoutputs)
elif af=="AF02":
    print "starting to scan AF02---10.246.190.0"
    lan_scan_of_AF02(Lanscanoutputs)
elif af=="AF03":
    print "starting to scan AF03---10.246.191.0"
    lan_scan_of_AF03(Lanscanoutputs)
elif af=="AF04":
    print "starting to scan AF04---214.186.4.0-214.186.29.254"
    lan_scan_of_AF04(Lanscanoutputs)
else:
    print "input error,try again....."
    pass

"""结束判断扫描哪个网络地址段，开始执行扫描所选择的网络地址段"""
proc_write_end(Lanscanoutputs)
Lanscanoutputs.close()
	






