
__author__ = 'weijie'
"""
还未测试20130905-0955
http://www.oschina.net/code/snippet_1257851_24468
自己的电脑总是被别人使用,又不好意思 设置密码,所以利用python设计了一个程序来实现自由管控.
功能虽然简单,但大家可以通过其思路来实现更多的功能.
大致功能主要是两个部分,一是电脑开机时,我的手机能收到通知.二是我可以通过手机发个特定的mail,就可以控制电脑关机.
实现第一个步骤,申请一个邮箱,使这个邮箱与你的手机号码绑定,然后你在这个邮箱中设定如果有新的邮件就发短信通知.这样开机时往这个邮箱发个mail,我手机就会收到短信通知了.

第二个步骤就是通过python 脚本,定时去检查163.com邮箱中是否有指定的邮件,如果有,则执行特定功能(我的是关机).

第一步骤申请成功以后,手机也可以通过一个号码10658139来发送mail,编辑短信格式如:test@163.com(空格)主旨(空格)正文.

这样我如果想关机,就会用手机发个mail到163邮箱,主旨是'关机',程式检测到这个mail以后就会执行关机动作.
"""
#!/etc/bin/env python
#-*-encoding=utf-8-*-
#auth@:dengyongkai
#blog@:blog.sina.com.cn/kaiyongdeng

import poplib,email
from email.header import decode_header
import smtplib
import time
import os,sys
import random

def accp_mail():
    try:
        p=poplib.POP3('pop.qq.com')
        p.user('用户名')
        p.pass_('密码')
        ret = p.stat()
    except poplib.error_proto,e:
        return 1
        print "Login failed:",e
        sys.exit(1)
    #       for i in range(1,ret[0]+1):
    #               str=s.top(i,0)
    #               strlist=[]
    #               for x in str[1]:
    #                       try:
    #                               strlist.append(x.decode())
    #                       except:
    #                               try:
    #                                       strlist.append(x.decode('gbk'))
    #                               except:
    #                                       strlist.append(x.decode('big5'))
    #
    #               mm = email.message_from_string('\n'.join(strlist))
    #               sub=decode_header(mm['subject'])
    #               if sub[0][1]:
    #                       submsg = sub[0][0].decode(sub[0][1])
    #               else:
    #                       submsg = sub[0][0]
    #
    #               if submsg.strip()=='startpc':
    #                       s.dele(i)
    #                       return 0
    #
    #       s.quit()
    #       return 1
    #
    for item in p.list()[1]:
        number,octets = item.split(' ')
        #               print "Message %s: %sbytes"%(number,octets)
        lines = p.retr(number)[1]
        msg = email.message_from_string("\n".join(lines))
        #       print msg.as_string()
        print msg.get_payload()
        if msg.get_payload()=="start\n\n":
            return 0

def send_mail():
    try:
        handle = smtplib.SMTP('smtp.163.com', 25)
        handle.login('********@163.com','密码')
        msg = "To: ********@qq.com\r\nFrom: ********@163.com\r\nSubject: startpc \r\n\r\nstart\r\n"
        handle.sendmail('********@163.com','********@qq.com', msg)
        handle.close()
        return 1
    except:
        return 0


if __name__=='__main__':
    while send_mail()==0:
        time.sleep(2)

    while 1:
        time.sleep(5)
        if accp_mail()==0:
            os.system('shutdown -f -s -t 10 -c closing...')
            #print "哈哈哈哈哈哈哈，成功啦！！！！！！"
            break