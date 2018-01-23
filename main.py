# -*- coding: utf-8 -*-

import db
from network import dzt_crawler
def crawl():
    db.init()
    db.shops_needed_to_crawl()
    db.finish()

if __name__ == '__main__':
    # dztCrawler.init()
    # dztCrawler.log_in()
    dzt_crawler.set_need_log_in_flag(True)
    print dzt_crawler.need_log_in_flag()
    dzt_crawler.set_need_log_in_flag(False)
    print dzt_crawler.need_log_in_flag()
