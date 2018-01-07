# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random
import signal
import pickle
import os


# 加载cookie
cookie_file = "cookies.pkl"

def load_cookies():
    if os.path.exists(cookie_file):
        cookies = pickle.load(open(cookie_file, "rb"))
        for cookie in cookies:
            driver.add_cookie(cookie)


# 保存cookie
def dump_cookies():
    c = driver.get_cookies()
    pickle.dump(c, open(cookie_file, "wb"))
    driver.quit()

def print_cookies():
    cookie = "; ".join([item["name"] + "=" + item["value"] + "\n" for item in driver.get_cookies()])
    print cookie


#小kk首页
shopUrl = "https://shop36252086.m.taobao.com/"
# 宝贝列表
goodsListUrl = 'https://shop36252086.m.taobao.com/#list'

dztUrl = 'https://www.dianzhentan.com/member/'

#driver = webdriver.PhantomJS()
driver = webdriver.Chrome()

#load_cookies()

driver.get(dztUrl)
load_cookies()
driver.get(dztUrl)

while True:
    c = raw_input("Enter your input: ")
    if c == "p":
        print_cookies()
    if c == 'd':
        dump_cookies()
    if c == "q":
        break


dump_cookies()
driver.quit()


