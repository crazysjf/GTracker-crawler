# -*- coding: utf-8 -*-
import sys
from db.db import DB
from db import csv_processor
from network.dzt_crawler import DztCrawler
from datetime import date


def try_crawl():
    '''尝试爬取所有需要爬取的文件。如果需要登录则标记需要登录并退出。'''
    c = DztCrawler()

    if c.need_log_in():
        print 'need log in'
        sys.exit()

    db = DB()
    shops = db.shops_needed_to_crawl()
    print shops

    for shop_id in shops.keys():
        dates = shops[shop_id]
        for d in dates:
            f =  c.download_a_csv(shop_id, str(d))
            print f
            csv_processor.import_to_db(shop_id, d, f)



def console():
    c = DztCrawler()
    c.console()

def import_test():
    shop_id = '63359486'
    d = date(2017,12,23)
    f = 'D:\projects\20160816-GTracker-taobao-data-analyzer\src\GTracker-crawler\network\csv/63359486-2017-12-23.csv'
    csv_processor.import_to_db(shop_id, d, f)


if __name__ == "__main__":
    try_crawl()
    #console()

