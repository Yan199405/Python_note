# scrapy命令行详解

- 参考：https://docs.scrapy.org/en/latest/（官网）
- 获取命名帮助：
    - scrapy -h
    - scrapy `<command>` -h
    
## 全局命令和局部命令
    - 全局命令：在项目外执行的命令
        - startproject
        - genspider
        - settings
        - runspider
        - shell
        - fetch
        - view
        - version
          
    - 局部命令：必须在项目目录中执行
        - crawl
        - check
        - list
        - edit
        - parse
        - bench
        
## 创建项目：

- 创建一个名为tutorial的项目

    >scrapy startproject tutorial
    
    
        │——scrapy.cfg (部署配置文件)
        │
        └─tutorial（项目的python模块，您将从此处导入代码）
            │  items.py      保存数据结构
            │  middlewares.py     中间件
            │  pipelines.py       输出管道
            │  settings.py        配置信息，变量定义
            │  __init__.py
            │
            ├─spiders           最主要的爬虫运行代码存放位置      
            │____init__.py     

   - 全局配置为项目根目录下的scrapy.cfg
    
    例：
    
        [settings]
        default = myproject.settings
        
        如果有多个项目的话：
        [settings]
        default = myproject1.settings
        project1 = myproject1.settings
        project2 = myproject2.settings
   
   - 局部配置在spider文件中，可以取代全局配置
   

- 生成一个spider:  
   
   比如要生成一个爬取baidu的spider
   接着上一步，先进入到项目目录，执行生成spider的命令
   > cd tutorial
   
   >scrapy genspider baidu www.baidu.com
   
   还可以执行创建spider的模板
   
   例：列出可以执行的spider模板，然后创建项目的时候可以用-t指定
   >scrapy genspider -l    
   
        Available templates:
          basic
          crawl
          csvfeed
          xmlfeed
    
   >scrapy genspider -t crawl zhihu www.zhihu.com

   成功后输出：
    
       Created spider 'baidu' using template 'basic' in module:
       tutorial.spiders.baidu

-  启动项目 
    
   运行爬虫的命令
   
   >scrapy crawl baidu
   
- 检查：check
   
   检查项目中代码是否有错    
   >scrapy check
   
       (base) D:\Study\notepad\Python>scrapy check
        
        ----------------------------------------------------------------------
        Ran 0 contracts in 0.000s
        
        OK

- 其他一些常用命名
    - 打印spider列表
     >scrapy list
    
        >scrapy list
        baidu
        zhihu
    - 命令行编辑spider，会用vim打开spider文件编辑
        > scrapy edit zhihu
     
    - fetch 输出网页代码
        >scrapy fetch <url>
    
        支持的选项
        
          --spider=SPIDER： 绕过蜘蛛自动检测并强制使用特定的蜘蛛
          --headers： 打印响应的HTTP标头而不是响应的正文
          --no-redirect： 不要遵循HTTP 3xx重定向（默认是遵循它们）
 
        示例：
        
            $ scrapy fetch --nolog http://www.example.com/some/page.html
            [ ... html content here ... ]
            
            $ scrapy fetch --nolog --headers http://www.example.com/
            {'Accept-Ranges': ['bytes'],
             'Age': ['1263   '],
             'Connection': ['close     '],
             'Content-Length': ['596'],
             'Content-Type': ['text/html; charset=UTF-8'],
             'Date': ['Wed, 18 Aug 2010 23:59:46 GMT'],
             'Etag': ['"573c1-254-48c9c87349680"'],
             'Last-Modified': ['Fri, 30 Jul 2010 15:30:18 GMT'],
             'Server': ['Apache/2.2.3 (CentOS)']}
    
    - view下载并打开网页
        >scrapy view <url>
    
        支持的选项
        
          --spider=SPIDER： 绕过蜘蛛自动检测并强制使用特定的蜘蛛
          --headers： 打印响应的HTTP标头而不是响应的正文
          --no-redirect： 不要遵循HTTP 3xx重定向（默认是遵循它们）
        
    - bench 测试爬取性能
        > scrapy bench
    
-  shell 调试

   运行命令进入命令行调试
   
   >scrapy shell www.baidu.com
   

   