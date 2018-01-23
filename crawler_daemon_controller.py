# -*- coding: utf-8 -*-
import argparse
from crawler_daemon_proxy import CrawlerServerProxy
from db.db import DB
from datetime import date
import os, sys

parser = argparse.ArgumentParser()
parser.add_argument('cmd', nargs='?')
args = parser.parse_args()

cmd = args.cmd

cmd = 'allcsv'

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

    print p.download_a_csv('63359486', '2017-12-23')

    # for s in shops.keys():
    #     dates = shops[s]
    #     for d in dates:
    #         print p.download_a_csv(s, d)
