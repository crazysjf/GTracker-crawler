# -*- coding: utf-8 -*-
import pickle
import os

cookie_file = "cookies.pkl"

def load_cookies(driver):
    if os.path.exists(cookie_file):
        cookies = pickle.load(open(cookie_file, "rb"))
        for cookie in cookies:
            driver.add_cookie(cookie)


# 保存cookie
def dump_cookies(driver):
    c = driver.get_cookies()
    pickle.dump(c, open(cookie_file, "wb"))
    driver.quit()

def print_cookies(driver):
    cookie = "; ".join([item["name"] + "=" + item["value"] + "\n" for item in driver.get_cookies()])
    print cookie
