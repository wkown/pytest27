# -*- coding: utf-8 -*-
# filename:example3.py
# datetime:2014-05-14 09:31
__author__ = 'walkskyer'
"""
"""

if __name__ == "__main__":
    import sqlite3
    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    t = ('RHAT',)
    c.execute('SELECT * FROM stocks WHERE symbol=?', t)
    print c.fetchone(),'\n'

    """purchases = [('2006-03-28', 'BUY', 'IBM', 1000, 45.00),
                 ('2006-04-05', 'BUY', 'MSFT', 1000, 72.00),
                 ('2006-04-06', 'SELL', 'IBM', 500, 53.00),
                 ]
    c.executemany('INSERT INTO stocks VALUES (?,?,?,?,?)', purchases)
    conn.commit()"""

    for row in c.execute('SELECT * FROM stocks ORDER BY price'):
        print row


