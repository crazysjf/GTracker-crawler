# -*- coding: utf-8 -*-

# 仅用给现有数据库中没有主图的商品加上主图

from db.db import DB
from network.main_pic_crawler import crawl_main_pic

db = DB()
gs = db.get_all_goods_with_empty_main_pic()

for i, g in enumerate(gs):
    id = g[0]
    main_pic = crawl_main_pic(id)
    db.good_update_main_pic(id, main_pic)
    print "updated:", i, id, main_pic

