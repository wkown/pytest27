# -*- coding:utf-8 -*-
import requests
import os.path
from urlparse import urlparse
import json
import sqlite3

"""
"""

comments_url = 'https://api.shuidichou.com/api/cf/v4/detail/get'
comments_post_param = {
'anchorId':'',
'infoUuid':	'',
'size':100,
}


def getInfoUuid(info_url):
    url_parse = urlparse(info_url)
    return os.path.basename(url_parse.path)


def insert_data(data, params=None):
    if params is None:
        params = {}
    content = None
    if data['headImgUrl']:
        headImg = requests.get(data['headImgUrl'])
        if params.has_key('saveImgFile') and not params['saveImgFile']:
            content = buffer(headImg.content)
        else:
            file_name = os.path.basename(os.path.basename(data['headImgUrl']))
            with open('%s.jpg' % file_name, 'wb') as f:
                f.write(headImg.content)
                f.close()
    # print headImg.content
    c.execute('INSERT INTO user VALUES (?,?,?,?,?,?,?,?,?,?,?,?)',
              [data['id'], data['userId'], data['userThirdId'], data['nickname'],
               data['headImgUrl'], data['amt'], data['comment'], json.dumps(data['comments']),
               data['time'], data['isShare'], data['goodsOrderExtVo'], content])


if __name__ == "__main__":

    arg_url = raw_input('input URL:')
    comments_post_param['infoUuid'] = getInfoUuid(arg_url)
    print comments_post_param

    flag = True

    conn = sqlite3.connect('./data.db')
    c = conn.cursor()
    c.execute("""CREATE TABLE [user](
    [id] BIGINT NOT NULL DEFAULT 0,
    [userId] BIGINT,
    [userThirdId] BIGINT,
    [nickname] CHAR,
    [headImgUrl] CHAR,
    [amt] DECIMAL,
    [comment] TEXT,
    [comments] TEXT,
    [time] BIGINT,
    [isShare] BOOL,
    [goodsOrderExtVo] CHAR,
    [headImg] IMAGE
    )
""")

    while flag:
        resp = requests.post(comments_url, comments_post_param)
        print resp.content
        content_json = json.loads(resp.content)
        print content_json
        data = content_json['data']
        list = data['list']
        for user_data in list:
            insert_data(user_data)

        comments_post_param['anchorId'] = data['anchorId']
        flag = data['hasNext']
        conn.commit()

    conn.close()