# -*- coding: utf-8 -*-
import sqlite3 as lite

db_name = "data.db"

def migrate():
    con = lite.connect(db_name)
    with con:
        cur = con.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS Shops(Id INTEGER PRIMARY KEY, Name TEXT, Link TEXT, ShopId TEXT NOT NULL, CreationDate DATETIME DEFAULT (datetime('now', 'localtime')))")


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