# -*- coding: utf-8 -*-
import argparse
from crawler_daemon_proxy import CrawlerServerProxy
from db.db import DB
from db import csv_processor
from datetime import date
import os, sys

parser = argparse.ArgumentParser()
parser.add_argument('cmd', nargs='?')
args = parser.parse_args()

cmd = args.cmd

cmd = 'allcsv'

# test
shop_id = '63359486'
date = date(2017, 12, 23)
f = r'D:\projects\20160816-GTracker-taobao-data-analyzer\src\GTracker-crawler\network\csv/63359486-2017-12-23.csv'
csv_processor.import_to_db(shop_id, date, f)
sys.exit()

if cmd == "allcsv":
    #p = CrawlerServerProxy().proxy
    db = DB()
    p  = CrawlerServerProxy().proxy

    print os.path.abspath(__file__)
    sys.exit

    # shops = db.shops_needed_to_crawl()
    # print shops
    if p.need_log_in():
        print 'need log in'
        sys.exit()

    shop_id = '63359486'
    date = date(2017,12,23)
    f =  p.download_a_csv(shop_id, str(date))
    print f
    f = 'D:\projects\20160816-GTracker-taobao-data-analyzer\src\GTracker-crawler\network\csv/63359486-2017-12-23.csv'
    csv_processor.import_to_db(shop_id, date, f)

    # for s in shops.keys():
    #     dates = shops[s]
    #     for d in dates:
    #         print p.download_a_csv(s, d)
