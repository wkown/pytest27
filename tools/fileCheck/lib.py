# -*- coding:utf-8 -*-
import hashlib
import os
import re

sign_style = {
    'html': '<!--sign{%s}-->'
}
sign_re = {
    'html': '<!--sign{.*?}-->'
}

def md5(s, raw_output=False):
    res = hashlib.md5(s)
    if raw_output:
        return res.digest()
    return res.hexdigest()


def sign2file(sign_val, file_path, target_file=None):
    """
    将签名写入文件
    :param sign_val:
    :param file_path:
    :param target_file:
    :return:
    """
    file_type = 'html'

    sign_val = sign_style[file_type] % sign_val

    f = open(file_path)
    content = f.read()
    f.close()

    if file_type == 'html':
        content = content.replace('</body>', '%s</body>' % sign_val)

    if not target_file:
        target_file = file_path

    f = open(target_file, 'wb')
    f.write(content)
    f.close()


def retrieve_sign(content, filename=None):
    """
    从已签名文件中获取签名
    :param content:
    :param filename:
    :return:
    """
    f_type = 'html'
    match = re.search(sign_re[f_type], content)
    if not match:
        return None

    sign_str = match.group(0)
    match = re.search('\{(.*?)\}', sign_str)

    sign_ret = ''
    if match:
        sign_ret = match.group(1)

    return sign_str, sign_ret


def signature_file(file_path):
    """
    输入文件名，返回文件签名
    :param file_path:
    :return:
    """

    filename = os.path.basename(file_path)

    f = open(file_path)
    content = f.read()
    f.close()

    return sign(filename, content)


def sign(filename, content):
    """
    生成签名
    :param filename:
    :param content:
    :return:
    """
    md5_filename = md5(filename)
    md5_content = md5(content)
    return md5('%s:%s' % (md5_filename, md5_content))


def signature_check(file_path):
    """
    验证签名，通过返回true否则返货false
    :param file_path:
    :return:
    """
    result = False
    filename = os.path.basename(file_path)

    f = open(file_path)
    content = f.read()
    f.close()

    sign_str, sign_ret = retrieve_sign(content)
    content = content.replace(sign_str, '')
    sign_val = sign(filename, content)
    if sign_ret == sign_val:
        result = True
    return result


def send_sms(msg):
    """
    发送短信
    :param msg:
    :return:
    """

    return True
