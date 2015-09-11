# -*- coding:utf-8 -*-
__author__ = 'walkskyer'

import apiUtil as api

"""
测试程序
"""
def run(url, select_group, config,):

    item = config.get_item(url, select_group)
    print "Current url(%s) in testing:" % item.url
    if item is None:
        print "The item is None, may be your url is not correct!"
        return None

    #GET field input
    get_val = {}
    if len(item.getField) > 0:
        print 'please input the GET field:'
        for i in xrange(0, len(item.getField)):
            field = item.getField[i]
            get_val[field['field']] = raw_input("%s(%s):" % (field['label'], field['field']))
    #POST field input
    post_val = {}
    if len(item.postField) > 0:
        print 'please input the POST field:'
        for i in xrange(0, len(item.postField)):
            field = item.postField[i]
            post_val[field['field']] = raw_input("%s(%s):" % (field['label'], field['field']))
        #print post_val

    hc = api.HttpClient(host=config.get_common_config('host'))
    url = item.url

    if len(get_val) > 0:
        url = hc.create_url(url, get_val)

    if len(post_val) > 0:
        return hc.post(url, post_val)

    return hc.get(item.url, get_val)
if __name__ == "__main__":
    configName = raw_input('configName:')
    filename = "test_template/%s.json" % configName
    config = api.ApiConfig(filename)
    while True:
        select_group = raw_input('Select a group or command(ls):')
        if select_group == 'ls':
            for item in config.get_groups():
                print "%s:%s" % (item['name'], item['field'])
            continue
        if not config.has_group(select_group):
            print 'There is not a group named: %s ' % select_group
            continue
        while True:
            url = raw_input('Input a url or command(ls|back):')
            if url == 'ls':
                for item in config.get_group_items(select_group):
                    print "%s:%s" % (item.name, item.url)
                continue

            if url == '' or url == 'back':
                print "Change Group!"
                break
            next_op = None
            while True:
                if next_op is None or next_op == '' or next_op == 'continue':
                    print '*********** start *************'
                    print run(url, select_group, config)
                    print '***********  end  *************\n'

                next_op = raw_input('The next?(back|continue|reload|help):')

                if next_op == 'back':
                    break
                if next_op == 'reload':
                    print 'Reload the config file'
                    config.load_config(filename)
                    continue
                if next_op == 'help':
                    print "" \
                          "back: Back to up level\n" \
                          "continue or empty: Continue test this url\n" \
                          "reload : Reload the config file and continue test this url\n" \
                          "help : Show this message"
                    raw_input('Press any key to continue ...')
                    continue
