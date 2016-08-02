# -*- coding:utf-8 -*-
import top.api
import json


def send_sms(phone_num, msg_param, sms_config):
    """
    发送短信
    :param phone_num:
    :param msg_param:
    :param sms_config:
    :return:
    """
    req = top.api.AlibabaAliqinFcSmsNumSendRequest()
    req.set_app_info(top.appinfo(sms_config['appkey'], sms_config['secret']))

    req.extend = "Extend"
    req.sms_type = "normal"
    req.sms_free_sign_name = sms_config['sign_name']
    req.sms_param = json.dumps(msg_param) #"{name:'zwj',num:'123',time:'20160802 14:30'}"
    req.rec_num = phone_num
    req.sms_template_code = "SMS_12910783"
    try:
        resp = req.getResponse()
        print (resp)
    except Exception, e:
        print (e)
        return False
    return True

if __name__ == '__main__':

    sms_config = {
        'appkey': '',
        'secret': '',
        'sign_name': '',
        'template_code': '',
    }
    msg_param = {'name': '', 'num': '', 'time': '20160802 14:30'}
    phone_num = ''
    send_sms(phone_num, msg_param, sms_config)
