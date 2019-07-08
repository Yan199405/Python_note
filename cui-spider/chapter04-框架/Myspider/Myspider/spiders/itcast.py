# -*- coding: utf-8 -*-
import scrapy
from Myspider.items import MyspiderItem

class ItcastSpider(scrapy.Spider):
    name = 'itcast'
    allowed_domains = ['itcast.cn']
    start_urls = ['http://www.itcast.cn/channel/teacher.shtml']



    # def parse(self, response):
    #     filename = 'teacher.html'
    #     with open(filename, 'w', encoding='utf-8') as f:
    #         f.write(response.text)

# xpath提取数据
    def parse(self, response):
        teachers = response.xpath("//div[@class='li_txt']")
        for teacher in teachers:
            item = MyspiderItem()
            name = teacher.css('h3::text').get()
            title = teacher.css('h4::text').get()
            info = teacher.css('p::text').get()
            item['name'] = name
            item['title'] = title
            item['info'] = info
            yield item
