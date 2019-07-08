# scrapy shell

调试模式下使用xpath、css选择器案例

- 官网案例
    
    官网教程：https://docs.scrapy.org/en/latest/topics/selectors.html
    
    网页源码：
    
     https://docs.scrapy.org/en/latest/_static/selectors-sample1.html
      
        <html>
         <head>
          <base href='http://example.com/' />
          <title>Example website</title>
         </head>
         <body>
          <div id='images'>
           <a href='image1.html'>Name: My image 1 <br /><img src='image1_thumb.jpg' /></a>
           <a href='image2.html'>Name: My image 2 <br /><img src='image2_thumb.jpg' /></a>
           <a href='image3.html'>Name: My image 3 <br /><img src='image3_thumb.jpg' /></a>
           <a href='image4.html'>Name: My image 4 <br /><img src='image4_thumb.jpg' /></a>
           <a href='image5.html'>Name: My image 5 <br /><img src='image5_thumb.jpg' /></a>
          </div>
         </body>
        </html>

    使用调试模式访问：  
    
    `由于我们正在处理HTML，因此选择器将自动使用HTML解析器。`  
    >scrapy shell https://docs.scrapy.org/en/latest/_static/selectors-sample1.html
    

- 语法格式
    - 选择a标签
        - xpath: response.xpath('//a')  
        - css: response.css('a')  
        
    - 选择a标签下的文本
        - xpath: response.xpath('//a/text()')  
        - css: response.css('a::text')   
             
    - 选择a标签下的href属性内容
        - xpath: response.xpath('//a/@href')  
        - css: response.css('a::attr(href)')    
              
    - 案例：
    
        打印title
        
        - xpath打印title
            
                In [39]: response.xpath('//title/text()')
                Out[39]: [<Selector xpath='//title/text()' data='Example website'>]
                
                //下面用getall和get方法的比较，当然这里也可以用extract和extrac_first取
                In [40]: response.xpath('//title/text()').getall()
                Out[40]: ['Example website']
                
                In [41]: response.xpath('//title/text()').get()
                Out[41]: 'Example website' 
            
        - css打印title       
            
                In [47]: response.css('title::text')
                Out[47]: [<Selector xpath='descendant-or-self::title/text()' data='Example website'>]
                
                In [49]: response.css('title::text').getall()
                Out[49]: ['Example website']
                
                In [50]: response.css('title::text').get()
                Out[50]: 'Example website'    
    
- 如果没有查找到元素，则返回
    - is None
    
        示例
        
            In [51]: response.xpath('//div[@id="images"]/a/text()').get()
            Out[51]: 'Name: My image 1 '
            
            In [53]: response.xpath('//div[@id="not"]/a/text()').get() is None
            Out[53]: True
                    
- 没有查找到则返回提供的默认参数

    - .get（default=''）
    
        示例
        
           In [54]: response.xpath('//div[@id="not"]/a/text()').get(default='not find')
           Out[54]: 'not find'       

- 正则的使用

    示例
    
        In [58]: response.css('a::text').get()
        Out[58]: 'Name: My image 1 '
        
        用正则去掉 'Name：' 用.strip()去掉空格
        In [36]: response.css('a::text').re_first('Name\:(.*)').strip()
        Out[36]: 'My image 1'    
  
其他用法详见官方文档  https://docs.scrapy.org/en/latest/topics/selectors.html