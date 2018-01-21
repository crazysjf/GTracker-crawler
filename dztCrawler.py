# -*- coding: utf-8 -*-
# 店侦探爬虫
# 按店铺分类的宝贝销量列表：左侧面板宝贝分析 => 宝贝列表
# 导出按钮的链接例子：https://www.dianzhentan.com/member/items/all/73414042/?t=all&act=out&d=2018-01-01
# 格式应该为：https://www.dianzhentan.com/member/items/all/<店铺ID>?/t=all&act=out&d=<日期>

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random
import signal
import sys
from cookie_helper import *
import db
from constants import *
import csv_processor

#driver = webdriver.PhantomJS()
driver = webdriver.Chrome()

# 设置cookie。设置之前先必须get一个dummy page
driver.get(ERROR_404_URL)
load_cookies(driver)

driver.get(SHOP_LIST_URL)

# 此处应该加入验证，确保已经登录成功
import winsound

# 等待登录成功
while True:
    if u"用户登陆" in driver.title:
        winsound.Beep(600, 1000) # 有sleep 1秒的效果
    else:
        break

eList = driver.find_elements_by_css_selector("table#shop-list-table tbody tr")

shops = []
for e in eList:
    shop_id = e.get_attribute('data-shopid')
    a = e.find_element_by_css_selector('td.shop-name span a')
    link =  a.get_attribute('href')
    name =  a.text
    shops.append((name, link, shop_id))

db.update_shops(shops)

from dztLib import *
while True:
    c = raw_input("Enter your input: ")
    print c
    if c == "p":
        print_cookies(driver)
    if c == 'd':
        dump_cookies(driver)
    if c == 'l':
        csv_processor.download_files(driver)
    if c == "q":
        break



dump_cookies(driver)
driver.quit()

