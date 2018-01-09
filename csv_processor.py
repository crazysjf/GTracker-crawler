# -*- coding: utf-8 -*-
# 负责下载csv文件，检查哪些需要下载，并将下载的文件导入数据库。

import os
from constants import *
import db
import urllib2
import csv
import re

from datetime import datetime,timedelta, date


CSV_DIR = 'csv/'
#https://www.dianzhentan.com/member/items/all/71007028/?t=all&act=out&d=2018-01-07
#file_url = DZT_BASE_URL + 'member/items/all/73414042/?t=all&act=out&d=2018-01-02'
file_url_pattern = DZT_BASE_URL + 'member/items/all/%s/?t=all&act=out&d=%s'

def download_one_file(driver, shop_id, date_str):
    '''下载单个文件。'''
    cookies = [item["name"] + "=" + item["value"] for item in driver.get_cookies()]
    cookiestr = ';'.join(item for item in cookies)

    file_url = file_url_pattern % (shop_id, date_str)
    headers = {'cookie':cookiestr}
    req = urllib2.Request(file_url, headers = headers)
    try:
        response = urllib2.urlopen(req)
        text = response.read()

        file_name = CSV_DIR + shop_id + '-' + date_str + '.csv'
        fd = open(file_name, 'w')
        fd.write(text)
        fd.close()
        print '###get %s success!!' % file_name
    except:
        print("Unexpected error:", sys.exc_info()[0])
        raise

def download_files(driver):
    '''下载所有文件'''
    if not os.path.exists(CSV_DIR):
        os.makedirs(CSV_DIR)

    shops = db.get_all_shops()

    for shop in shops:
        now = datetime.now()
        for d in range(1,30):
            delta = timedelta(days=d)
            t = now - delta
            date_str = t.strftime("%Y-%m-%d")

            download_one_file(driver, shop[3], date_str)

def to_int(str):
    '''把str转为整数。如果成功返回整数，否则返回None'''
    try:
        return int(str)
    except:
        return None

GOOD_ID_PATTERN = re.compile(r'.*id=([0-9]*)$')
def get_good_id(link):
    '''从连接中获取商品ID'''
    m = GOOD_ID_PATTERN.match(link)
    if m == None:
        return None
    else:
        return m.group(1)


def import_to_db(shop_id, date, file):
    '''将csv文件导入数据库.
    date: datetime.date对象
    '''
    csv_reader = csv.reader(open(file, 'rb'))

    for i, row in enumerate(csv_reader):
        if i == 0:
            continue
        # 所有元素解码
        _row = map(lambda x: x.decode('GB2312'), row)
        title = _row[2]
        link = _row[3]
        creation_time = _row[4]
        view_cnt    = to_int(_row[6])
        fav_cnt     = to_int(_row[10])
        review_cnt  = to_int(_row[11])
        sales_30    = to_int(_row[12])

        good_id = get_good_id(link)
        # good_id没有就什么都不用做了
        if good_id == None:
            # 此处需要error log
            continue

        if not db.good_exists(good_id):
            good = (title, shop_id, good_id, creation_time)
            db.insert_good(good)

        if not db.record_exists(good_id, date):
            r = (date, good_id, sales_30, fav_cnt, view_cnt, review_cnt)
            db.insert_record(r)

if __name__ == "__main__":
    csv_file = CSV_DIR + '33531012-2017-12-10.csv'
    date = date(2017,12,10)
    import_to_db('33531012', '2017-12-10', csv_file)