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
    req.sms_param = json.dumps(msg_param)
    req.rec_num = phone_num
    req.sms_template_code = sms_config['template_code']
    try:
        resp = req.getResponse()
        print (resp)
    except Exception, e:
        print (e)
        return False
    return True

if __name__ == '__main__':
    from conf import load_config

    conf = load_config()
    sms_config = {
        'appkey': conf.get('sms', 'appkey'),
        'secret': conf.get('sms', 'secret'),
        'sign_name': conf.get('sms', 'sign_name'),
        'template_code': conf.get('sms', 'template_code'),
    }
    if sms_config['template_code'] == 'SMS_12910783':
        msg_param = {'name': 'hello world', 'num': '000', 'time': '20160802 14:30'}
    else:
        msg_param = {'name': 'hello world', 'dirs': '567', 'num': '234', 'time': '20160802 14:30'}
    phone_num = ''
    if not phone_num:
        phone_num = raw_input('手机号:')
    print send_sms(phone_num, msg_param, sms_config)
