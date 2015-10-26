# -*- coding:utf-8 -*-
__author__ = 'walkskyer'
"""
用于快速部署apache虚拟主机
"""
import ConfigParser
import os
import sys
import platform
import getopt
import argparse

def add_sub_domain(sub_domain,primary_domain,cfg_common):
    vhost_path = cfg_common['vhost_path']
    #vhost_template = cfg_common['vhost_template']
    website_root_path = cfg_common['website_root_path']
    website_log_path = cfg_common['website_log_path']

    if not os.path.isdir(vhost_path):
        os.mkdir(vhost_path)

    f = open('./vhost_tpl/domain_sub.conf')
    vhost_template = f.read()
    f.close()

    #添加虚拟机配置信息
    vhost_template = vhost_template.replace('{website_root_path}', website_root_path)
    vhost_template = vhost_template.replace('{website_log_path}', website_log_path)
    vhost_template = vhost_template.replace('{sub}', sub_domain)
    vhost_template = vhost_template.replace('{domain}', primary_domain)
    f = open("%s/%s_%s.conf" % (vhost_path, primary_domain, sub_domain), 'wb')
    f.write(vhost_template)
    f.close()

    if not os.path.isdir(website_root_path):
        os.mkdir(website_root_path)

    website_path = '%s/%s_%s' % (website_root_path, primary_domain, sub_domain)
    if not os.path.isdir(website_path):
        os.mkdir(website_path)


    #创建虚拟机工作目录
    index_template = """
    <html>
    <head><title>Hello welcome to {sub}.{domain}</title></head>
    <body>
    Hello welcome to {sub}.{domain}
    </body>
    </html>
    """
    index_template = index_template.replace('{sub}', sub_domain)
    index_template = index_template.replace('{domain}', primary_domain)

    f = open("%s/index.html" % website_path, 'wb')
    f.write(index_template)
    f.close()

def restart_server(cfg_common,website_path=None):
    if website_path == None:
        website_path = cfg_common['website_root_path']
    if platform.system() == 'Linux':
        os.system(cfg_common['apache_restart_cmd'])
        os.system('%s %s' % (cfg_common['website_chown'], website_path))


def usage():
    print "usage:python vhost.py add|init param \n" \
              "add: add a new sub domain usage: add -s sub_domain -d domain" \
              "init: init the domain config use default config usage: init -d domain"
if __name__ == "__main__":

    argv_len = len(sys.argv)


    parser = argparse.ArgumentParser(description='Config vhosts')
    #parser.add_argument('cmd', default='init', help="The commond: add|init\n")
    subparsers = parser.add_subparsers(dest='subparser_name',help='sub command')
    #add sub command
    parser_add = subparsers.add_parser('add', help='add a new sub domain')
    parser_add.add_argument('-s', dest='sub_domain', metavar='sub domain', help='sub domain e.g. www')
    parser_add.add_argument('-d', dest='primary_domain', metavar='primary domain', help='primary domain e.g. baidu.com')
    #init sub command
    parser_init = subparsers.add_parser('init', help='init the domain config use default config')
    parser_init.add_argument('-d', dest='primary_domain', metavar='primary domain', help='primary domain e.g. baidu.com')

    #args = parser.parse_args('add -s www -d baidu.com'.split())
    #args = parser.parse_args('init -d baidu.com'.split())
    args = parser.parse_args()
    #print args

    cmd = args.subparser_name
    if cmd not in ['add', 'init', 'rm']:
        usage()
        exit(0)

    for name, val in vars(args).items():
        if name == 'sub_domain':
            sub_domain = val
        elif name == 'primary_domain':
            primary_domain = val





#读取配置文件并使用配置信息配置信息
    config = ConfigParser.SafeConfigParser()
    file_path = os.path.dirname(os.path.realpath(__file__))
    config.read('%s/conf_vhost.ini' % file_path)
    cfg_common = dict(config.items('common'))

    if cmd == 'add':
        if args.sub_domain == None or args.primary_domain == None:
                print 'Need sub domain and primary domain'
                exit(0)
        add_sub_domain(args.sub_domain, args.primary_domain, cfg_common)
        print 'vhost config is finished, you can visit: %s.%s' % (args.sub_domain, args.primary_domain)
    if cmd == 'init':
        if args.primary_domain == None:
                print 'Need primary domain -d'
                exit(0)
        for sub_domain in ('www','api','test','wap'):
            add_sub_domain(sub_domain, args.primary_domain, cfg_common)
            print 'vhost config is finished, you can visit: %s.%s' % (sub_domain, args.primary_domain)
    restart_server(cfg_common)
