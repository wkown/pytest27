# -*- coding: utf-8 -*-
# filename:mysql.py
# datetime:2014-04-02 17:38
__author__ = 'walkskyer'
"""
我自己封装的mysql适配器
"""
import MySQLdb


class MySql():
    def __init__(self):
        self.conn = None
        self.cursor = None

    def connect(self, host='localhost', user='root', passwd='', db='', charset='utf8', port=3306):
        try:
            self.conn = MySQLdb.connect(host=host, user=user, passwd=passwd, db=db, charset=charset, port=port)
            self.cursor = self.conn.cursor()
        except MySQLdb.Error, e:
            self.conn = None
            print "Mysql Error %d: %s" % (e.args[0], e.args[1])

    def insert(self, table, data=None):
        sql = 'INSERT INTO ' + table +\
              '(' + ','.join(data.iterkeys()) + ')' \
              'VALUES (' + ','.join(data.itervalues()) + ')'
        self.query(sql)

    def update(self, table, where=1, data=None):
        set_val=''
        conj=''
        for k, v in data.items():
            set_val = set_val + conj + "`" + k + "`= '" + v + "'"
            conj = ','
        sql = "UPDATE `" + table + "` SET " + set_val + " WHERE " + where + ";"
        self.query(sql)

    def delete(self, table, where=None):
        pass

    def fetchAll(self, table, where=1,order=None, offset=0, limit=20):
        sql = 'SELECT * FROM ' + table + ' WHERE ' + where + ' LIMIT ' + str(offset) + ',' + str(limit)
        self.query(sql)
        return self.cursor.fetchall()

    def fetchOne(self, table, where=1,order=None, offset=0, limit=20):
        sql = 'SELECT * FROM ' + table + ' WHERE ' + where + " LIMIT 1"
        self.query(sql)
        return self.cursor.fetchone()

    def query(self, sql=''):
        #print sql
        self.cursor.execute(sql)
        self.conn.commit()

    def close(self):
        self.cursor.close()
        self.conn.close()


if __name__ == "__main__":
    pass
