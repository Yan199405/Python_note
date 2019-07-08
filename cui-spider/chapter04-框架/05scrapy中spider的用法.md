# post请求

scrapy默认是get请求，如何让scrapy进行post请求？

以post请求必应为例

- 首先创建一个httpbin的spider
  >scrapy genspider httpbin httpbin.org
- 改写spider文件

        httpbin.py
        class HttpbinSpider(scrapy.Spider):
            name = 'httpbin'
            allowed_domains = ['httpbin.org']
            start_urls = ['http://httpbin.org/post']    # 修改为post
        
            def start_requests(self):                   # 添加url、请求方式、循环遍历的方法
                yield scrapy.Request(url='http://httpbin.org/post', method='POST', callback=self.parse_post)
        
            def parse(self, response):
                pass
        
            def parse_post(self, response):             # 处理post请求的方法 打印      
                print(response.text)