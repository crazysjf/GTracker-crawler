# -*- coding: utf-8 -*-

# from selenium import webdriver
# shopUrl = "http://shop.m.taobao.com/shop/shop_index.htm?shop_id=36252086" # 小KK
# shopGoodList = "https://shop36252086.m.taobao.com/?shop_id=36252086#list"
#
# driver = webdriver.PhantomJS()
# driver.get(shopGoodList)
# data = driver.page_source
# print data
# driver.quit()
#
#

import sqlite3 as lite
import sys
#
#
# cars = (
#     ('Audi', 52642),
#     ('Mercedes', 57127),
#     ('Skoda', 9000),
#     ('Volvo', 29000),
#     ('Bentley', 350000),
#     ('Hummer', 41400),
#     ('Volkswagen', 21600)
# )
#
#
# def insertData(con):
#     with con:
#         cur = con.cursor()
#         cur.execute("DROP TABLE IF EXISTS Cars")
#         cur.execute("CREATE TABLE Cars(Id INTEGER PRIMARY KEY, Name TEXT, Price INT)")
#         cur.executemany("INSERT INTO Cars(Name, Price) VALUES(?, ?)", cars)
#
#
# con = lite.connect('test.db')
#
# with con:
#     cur = con.cursor()
#     cur.execute("SELECT COUNT(*) FROM Cars")
#
#     row = cur.fetchone()
#     print row
#
#

a = 3
def f():
    a = 2
    print a
f()
print a
