# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random

def send_key_with_random_interval(e, s):
    for c in s:
        # 延迟0.1-0.6秒
        time.sleep(0.1 + random.random() / 2)
        e.send_keys(c)

def doThings():
    usernameE = driver.find_element_by_id("TPL_username_1")
    passwordE = driver.find_element_by_id("TPL_password_1")
    #usernameE.clear()
    #passwordE.clear()
    send_key_with_random_interval(usernameE, 'crazydandan66:jinfei')
    send_key_with_random_interval(passwordE, 'jinfeiabc123')
    time.sleep(0.5)
    driver.find_element_by_id("J_SubmitStatic").click()

    # driver.get_cookies()取得cookie
    cookie = "; ".join([item["name"] + "=" + item["value"] + "\n" for item in driver.get_cookies()])
    print cookie

# 生意参谋登录地址
loginUrl = 'https://sycm.taobao.com/custom/login.htm?_target=http://sycm.taobao.com/portal/home.htm'
downloadUrl =  'https://sycm.taobao.com/bda/download/excel/items/effect/ItemEffectExcel.do?dateRange=2017-12-24|2017-12-24&dateType=recent1&orderDirection=false&orderField=itemPv&type=0&device='

#driver = webdriver.PhantomJS()
driver = webdriver.Chrome()
driver.get(loginUrl)


# 登录框嵌在iframe里面，需要进行切换
f = driver.find_element_by_css_selector('div.login-box iframe')
driver.switch_to.frame(f)
try:
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "TPL_username_1"))
    )
    #doThings()
    while True:
        time.sleep(5)
        cookie = "; ".join([item["name"] + "=" + item["value"] + "\n" for item in driver.get_cookies()])
        print cookie

finally:
    print "finished"
    #driver.quit()
