# -*- coding: utf-8 -*-
import sqlite3 as lite

db_name = "data.db"

def migrate():
    con = lite.connect(db_name)
    with con:
        cur = con.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS Shops(Id INTEGER PRIMARY KEY, Name TEXT, Link TEXT, ShopId TEXT NOT NULL, CreationDate DATETIME DEFAULT (datetime('now', 'localtime')))")
        cur.execute("CREATE TABLE IF NOT EXISTS Goods(Id INTEGER PRIMARY KEY, Name TEXT, Link TEXT, ShopId TEXT NOT NULL, CreationDate DATETIME DEFAULT (datetime('now', 'localtime')))")
        cur.execute("CREATE TABLE IF NOT EXISTS Records(Id INTEGER PRIMARY KEY, Name TEXT, Link TEXT, ShopId TEXT NOT NULL, CreationDate DATETIME DEFAULT (datetime('now', 'localtime')))")


# 更新店铺信息，对于已存在的店铺不进行处理
# shops格式:((名称，链接，店铺id)
def update_shops(shops):
    con = lite.connect(db_name)
    with con:
        cur = con.cursor()
        for shop in shops:
            print shop[2]
            cur.execute("SELECT COUNT(*) FROM Shops WHERE ShopId=?", (shop[2],))
            # 如果记录不存在就插入
            if cur.fetchone()[0] == 0:
                cur.execute("INSERT INTO Shops(Name, Link, ShopId) VALUES(?,?,?)", shop)



def get_all_shops():
    con = lite.connect(db_name)
    rows = None
    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM Shops")
        rows = cur.fetchall()

    return rows

def good_exists(good_id):
    con = lite.connect(db_name)
    with con:
        cur = con.cursor()
        cur.execute('select * from goods where GoodId = ?', (good_id,))
        if cur.fetchone() == None:
            return False
        else:
            return True

def insert_good(good):
    '''
    插入商品
    :param good: 格式：(Name, ShopId, GoodId, CreationDate) 
    :return: 
    '''
    con = lite.connect(db_name)
    with con:
        cur = con.cursor()
        cur.execute("INSERT INTO Goods(Name, ShopId, GoodId, CreationDate) VALUES(?,?,?,?)", good)

def record_exists(good_id, date):
    '''判断某店铺某天的数据是否存在'''
    con = lite.connect(db_name)
    with con:
        cur = con.cursor()
        cur.execute("select * from records where GoodId=? and date=?", (good_id, date))
        if cur.fetchone() == None:
            return False
        else:
            return True

def insert_record(r):
    con = lite.connect(db_name)
    with con:
        cur = con.cursor()
        cur.execute("INSERT INTO Records(date, GoodId, sales_30, fav_cnt, view_cnt, review_cnt) VALUES(?,?,?,?,?,?)", r)



if __name__ == '__main__':
    good_exists('123')