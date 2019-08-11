# -*- coding: utf-8 -*-
import scrapy
from Myspider.items import MyspiderItem

class ItcastSpider(scrapy.Spider):
    name = 'itcast'
    allowed_domains = ['itcast.cn']
    start_urls = ['http://www.itcast.cn/channel/teacher.shtml']

# 测试写文件，了解parse的用法
    # def parse(self, response):
    #     filename = 'teacher.html'
    #     with open(filename, 'w', encoding='utf-8') as f:
    #         f.write(response.text)

# xpath提取数据
# 选择器用法：https://github.com/Yan199405/Python_note/blob/master/cui-spider/chapter04-%E6%A1%86%E6%9E%B6/04scrapy%E9%80%89%E6%8B%A9%E5%99%A8%E7%94%A8%E6%B3%95.md
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
