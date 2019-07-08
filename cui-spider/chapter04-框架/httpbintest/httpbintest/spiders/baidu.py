# -*- coding: utf-8 -*-
import scrapy


class BaiduSpider(scrapy.Spider):
    name = 'baidu'
    allowed_domains = ['www.baidu.com']
    start_urls = ['http://www.baidu.com/']

    def make_requests_from_url(self, url):
        self.logger.debug('Try first time!')
        return scrapy.Request(url=url, meta={'download_timeout': 10}, callback=self.parse, dont_filter=True)

    def parse(self, response):
        print(response.text)
