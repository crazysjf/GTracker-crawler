# -*- coding: utf-8 -*-
import sqlite3 as lite
import sys

db_name = "data.db"

def migrate():
    con = lite.connect(db_name)
    with con:
        cur = con.cursor()
        #cur.execute("CREATE TABLE if not exists Shops2(Id INTEGER PRIMARY KEY, Name TEXT, Link TEXT, ShopId TEXT NOT NULL, CreationDate DATETIME DEFAULT (datetime('now', 'localtime')))")
        #cur.execute('''insert into Shops2 select * from Shops''')
        cur.execute('''CREATE TABLE if not exists Goods(Id INTEGER PRIMARY KEY, Name TEXT, ShopId TEXT NOT NULL, GoodId integer not null, CreationDate DATETIME)''')
        cur.execute('''CREATE TABLE if not exists Records(Id INTEGER PRIMARY KEY, date datetime not null, GoodId TEXT NOT NULL, sales_30 integer, fav_cnt integer, view_cnt integer, review_cnt integer)''')

migrate()