# -*- coding: utf-8 -*-
import os
from constants import *
import db
import urllib2


from datetime import datetime,timedelta


csv_dir = 'csv/'
#https://www.dianzhentan.com/member/items/all/71007028/?t=all&act=out&d=2018-01-07
#file_url = DZT_BASE_URL + 'member/items/all/73414042/?t=all&act=out&d=2018-01-02'
file_url_pattern = DZT_BASE_URL + 'member/items/all/%s/?t=all&act=out&d=%s'

def download_one_file(driver, shop_id, date_str):
    cookies = [item["name"] + "=" + item["value"] for item in driver.get_cookies()]
    cookiestr = ';'.join(item for item in cookies)

    file_url = file_url_pattern % (shop_id, date_str)
    headers = {'cookie':cookiestr}
    req = urllib2.Request(file_url, headers = headers)
    try:
        response = urllib2.urlopen(req)
        text = response.read()

        file_name = csv_dir + shop_id + '-' + date_str + '.csv'
        fd = open(file_name, 'w')
        fd.write(text)
        fd.close()
        print '###get %s success!!' % file_name
    except:
        print("Unexpected error:", sys.exc_info()[0])
        raise

def download_files(driver):
    if not os.path.exists(csv_dir):
        os.makedirs(csv_dir)

    shops = db.get_all_shops()

    for shop in shops:
        now = datetime.now()
        for d in range(1,30):
            delta = timedelta(days=d)
            t = now - delta
            date_str = t.strftime("%Y-%m-%d")

            download_one_file(driver, shop[3], date_str)


