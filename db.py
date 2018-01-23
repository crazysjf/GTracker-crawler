# -*- coding: utf-8 -*-
'''db的用法：
按以下流程操作：
    初始化：db.init()
    数据库操作
    结束：db.finishi()
    
调用finish()的时候会自动提交数据库。
操作中途如果希望提交，可以调用db.commit().
'''
import sqlite3 as lite
from datetime import date, datetime, timedelta
import utils
import constants

db_name = "data.db"

con = None
cur = None


def init(db_path = None):
    '''初始化
    db_path:data.db所在目录，如果没有则为当前工作目录。
    '''
    global con, cur, db_name
    if db_path != None:
        db_name = db_path + db_name
    con = lite.connect(db_name)
    cur = con.cursor()

def commit():
    con.commit()

def finish():
    con.commit()
    con.close()

# 更新店铺信息，对于已存在的店铺不进行处理
# shops格式:((名称，链接，店铺id)
def update_shops(shops):
    for shop in shops:
        print shop[2]
        cur.execute("SELECT COUNT(*) FROM Shops WHERE ShopId=?", (shop[2],))
        # 如果记录不存在就插入
        if cur.fetchone()[0] == 0:
            cur.execute("INSERT INTO Shops(Name, Link, ShopId) VALUES(?,?,?)", shop)



def get_all_shops():
    cur.execute("SELECT * FROM Shops")
    rows = cur.fetchall()

    return rows

def good_exists(good_id):
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
    cur = con.cursor()
    cur.execute("INSERT INTO Goods(Name, ShopId, GoodId, CreationDate) VALUES(?,?,?,?)", good)

def record_exists(good_id, date):
    '''判断某店铺某天的数据是否存在'''
    cur.execute("select * from records where GoodId=? and date=?", (good_id, date))
    if cur.fetchone() == None:
        return False
    else:
        return True

def insert_record(r):
    cur.execute("INSERT INTO Records(date, GoodId, sales_30, fav_cnt, view_cnt, review_cnt) VALUES(?,?,?,?,?,?)", r)


def get_records(date, good_id = None):
    param = [date]
    sql = 'select * from records where date=?'
    if good_id != None:
        sql += ' and GoodId=?'
        param.append(good_id)
    cur.execute(sql, param)
    r = cur.fetchall()
    return r

def get_records2(date, shop_id):
    sql = '''select r.*, s.Name from Records r, Goods g, Shops s where
                r.GoodId = g.GoodId and
                g.ShopId = s.ShopId and
                r.date = ? and
                s.ShopId = ?'''
    cur.execute(sql, (date, shop_id))
    r = cur.fetchall()
    return r

def get_records3(shop_id, start_date=None, end_date=None):
    sql = '''select r.GoodId, r.sales_30 from Records r, Goods g, Shops s where
                r.GoodId = g.GoodId and
                g.ShopId = s.ShopId and
                s.ShopId = ?'''
    cur.execute(sql, (shop_id,))
    r = cur.fetchall()
    return r

def get_records_with_shop_id_in_date_range(shop_id, start_date=None, end_date=None):
    '''
    
    :param shop_id: 
    :param start_date: 开始日期，不指定则为30天前
    :param end_date: 结束日期，不指定则为当天
    :return: [good_id, r.date, r.sales_30
    '''
    if start_date == None:
        start_date = utils.start_date

    if end_date == None:
        end_date = utils.end_date

    sql = '''select r.GoodId, r.date, r.sales_30 from Records r, Goods g, Shops s where
                r.GoodId = g.GoodId and
                g.ShopId = s.ShopId and
                s.ShopId = ? and
                r.date >= ? and
                r.date <= ?'''
    cur.execute(sql, (shop_id, start_date, end_date))
    r = cur.fetchall()
    return r

def all_shops():
    sql = '''select ShopId, Name, Link from Shops'''
    cur.execute(sql)
    r = cur.fetchall()
    return r


def shops_needed_to_crawl():
    '''判断哪些店铺的哪些日期需要爬取。
    返回格式：{ shop_id1: [date1, date2,...], 
                shop_id2: [date3, date4,...],...}
    该函数执行需要约2分钟
     '''
    _all_shops = all_shops()
    result = {}
    for (shop_id, _, _) in _all_shops:
        for d in range(0, constants.DATE_RANGE):
            date = utils.start_date + timedelta(d)
            sql = '''select count(*) from Records r, Goods g, Shops s where
                        r.GoodId = g.GoodId and
                        g.ShopId = s.ShopId and
                        g.ShopId = ? and
                        r.date = ?'''
            cur.execute(sql, (shop_id, date))
            r = cur.fetchall()[0]
            if r[0] == 0:
                #print shop_id, date
                if result.has_key(shop_id):
                    result[shop_id].append(date)
                else:
                    result[shop_id] = [date]
    return result


if __name__ == '__main__':
    good_exists('123')