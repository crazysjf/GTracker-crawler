# -*- coding: utf-8 -*-
import scrapy


class QuotesSpider(scrapy.Spider):
    name = "sycm"
    start_urls = [
        # 生意参谋登录地址
        'https://sycm.taobao.com/custom/login.htm?_target=http://sycm.taobao.com/portal/home.htm'

        #'https://sycm.taobao.com/bda/download/excel/items/effect/ItemEffectExcel.do?dateRange=2017-12-24|2017-12-24&dateType=recent1&orderDirection=false&orderField=itemPv&type=0&device='
    ]

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'quotes-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)