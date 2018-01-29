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

from misc import utils, constants
import os

dir = os.path.dirname(os.path.abspath(__file__))

class DB:
    db_name = os.path.join(dir, "data.db")

    def __init__(self, db_path = None):
        '''初始化
        db_path:data.db所在目录，如果没有则为当前工作目录。
        '''
        if db_path != None:
            self.db_name = db_path + self.db_name
        self.con = lite.connect(self.db_name)
        self.cur = self.con.cursor()

    def __del__(self):
        self.finish()

    def commit(self):
        self.con.commit()

    def finish(self):
        self.con.commit()
        self.con.close()

    # 更新店铺信息，对于已存在的店铺不进行处理
    # shops格式:((名称，链接，店铺id)
    def update_shops(self, shops):
        for shop in shops:
            print shop[2]
            self.cur.execute("SELECT COUNT(*) FROM Shops WHERE ShopId=?", (shop[2],))
            # 如果记录不存在就插入
            if self.cur.fetchone()[0] == 0:
                self.cur.execute("INSERT INTO Shops(Name, Link, ShopId) VALUES(?,?,?)", shop)



    def get_all_shops(self):
        self.cur.execute("SELECT * FROM Shops")
        rows = self.cur.fetchall()

        return rows

    def good_exists(self, good_id):
        self.cur.execute('select * from goods where GoodId = ?', (good_id,))
        if self.cur.fetchone() == None:
            return False
        else:
            return True

    def insert_good(self, good):
        '''
        插入商品
        :param good: 格式：(Name, ShopId, GoodId, CreationDate) 
        :return: 
        '''
        self.cur.execute("INSERT INTO Goods(Name, ShopId, GoodId, CreationDate) VALUES(?,?,?,?)", good)

    def record_exists(self, good_id, date):
        '''判断某店铺某天的数据是否存在'''
        self.cur.execute("select * from records where GoodId=? and date=?", (good_id, date))
        if self.cur.fetchone() == None:
            return False
        else:
            return True

    def insert_record(self, r):
        self.cur.execute("INSERT INTO Records(date, GoodId, sales_30, fav_cnt, view_cnt, review_cnt) VALUES(?,?,?,?,?,?)", r)


    def get_records(self, date, good_id = None):
        param = [date]
        sql = 'select * from records where date=?'
        if good_id != None:
            sql += ' and GoodId=?'
            param.append(good_id)
        self.cur.execute(sql, param)
        r = self.cur.fetchall()
        return r

    def get_records2(self, date, shop_id):
        sql = '''select r.*, s.Name from Records r, Goods g, Shops s where
                    r.GoodId = g.GoodId and
                    g.ShopId = s.ShopId and
                    r.date = ? and
                    s.ShopId = ?'''
        self.cur.execute(sql, (date, shop_id))
        r = self.cur.fetchall()
        return r

    def get_records3(shop_id, start_date=None, end_date=None):
        sql = '''select r.GoodId, r.sales_30 from Records r, Goods g, Shops s where
                    r.GoodId = g.GoodId and
                    g.ShopId = s.ShopId and
                    s.ShopId = ?'''
        self.cur.execute(sql, (shop_id,))
        r = self.cur.fetchall()
        return r

    def get_records_with_shop_id_in_date_range(self, shop_id, start_date=None, end_date=None):
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
        self.cur.execute(sql, (shop_id, start_date, end_date))
        r = self.cur.fetchall()
        return r

    def all_shops(self):
        sql = '''select ShopId, Name, Link from Shops'''
        self.cur.execute(sql)
        r = self.cur.fetchall()
        return r


    def shops_needed_to_crawl(self):
        '''判断哪些店铺的哪些日期需要爬取。如果某个店铺在某天一条记录也没有就被判定为需要爬取
        返回格式：{ shop_id1: [date1, date2,...], 
                    shop_id2: [date3, date4,...],...}
        该函数执行需要约2分钟
         '''
        _all_shops = self.all_shops()
        result = {}
        for (shop_id, _, _) in _all_shops:
            for d in range(0, constants.DATE_RANGE):
                date = utils.start_date + timedelta(d)
                sql = '''select count(*) from Records r, Goods g, Shops s where
                            r.GoodId = g.GoodId and
                            g.ShopId = s.ShopId and
                            g.ShopId = ? and
                            r.date = ?'''
                self.cur.execute(sql, (shop_id, date))
                r = self.cur.fetchall()[0]
                if r[0] == 0:
                    #print shop_id, date
                    if result.has_key(shop_id):
                        result[shop_id].append(date)
                    else:
                        result[shop_id] = [date]
        return result


if __name__ == '__main__':
    print DB('../').good_exists('123')