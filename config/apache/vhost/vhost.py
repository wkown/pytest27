# -*- coding:utf-8 -*-
__author__ = 'walkskyer'
"""
用于自动化部署apache虚拟主机
"""
import ConfigParser
import os
import sys
import platform

if __name__ == "__main__":
    argv_len = len(sys.argv)
    if argv_len <= 2:
        print "usage:python vhost.py Sub_domain Primary_domain [website_root]"  # vhost_path vhost_template_file
        exit(0)

    if argv_len == 3:
        sub_domain = sys.argv[1]
        primary_domain = sys.argv[2]
    website_root_path = None
    if argv_len == 4:
        website_root_path = sys.argv[3]

    #读取配置文件并使用配置信息配置信息
    config = ConfigParser.SafeConfigParser()
    file_path = os.path.dirname(os.path.realpath(__file__))
    config.read('%s/conf_vhost.ini' % file_path)
    cfg_common = dict(config.items('common'))

    vhost_path = vhost_template = ''
    vhost_path = cfg_common['vhost_path']
    vhost_template = cfg_common['vhost_template']
    if not website_root_path:
        website_root_path = cfg_common['website_root_path']

    if not os.path.isdir(vhost_path):
        os.mkdir(vhost_path)

    #添加虚拟机配置信息
    vhost_template = vhost_template.replace('{website_root_path}', website_root_path)
    vhost_template = vhost_template.replace('{sub_domain}', sub_domain)
    vhost_template = vhost_template.replace('{domain}', primary_domain)
    f = open("%s/%s_%s.conf" % (vhost_path, primary_domain, sub_domain), 'wb')
    f.write(vhost_template)
    f.close()


    if not os.path.isdir(website_root_path):
        os.mkdir(website_root_path)

    website_path = '%s/%s' % (website_root_path, sub_domain)
    if not os.path.isdir(website_path):
        os.mkdir(website_path)


    #创建虚拟机工作目录
    index_template = """
    <html>
    <head><title>Hello welcome to {sub_domain}.{domain}</title></head>
    <body>
    Hello welcome to {sub_domain}.{domain}
    </body>
    </html>
    """
    index_template = index_template.replace('{sub_domain}', sub_domain)
    index_template = index_template.replace('{domain}', primary_domain)

    f = open("%s/index.html" % website_path, 'wb')
    f.write(index_template)
    f.close()

    if platform.system() == 'Linux':
        os.system(cfg_common['apache_restart_cmd'])
        os.system('%s %s' % (cfg_common['website_chown'], website_path))
    print 'vhost config is finished, you can visit: %s.%s' % (sub_domain, primary_domain)