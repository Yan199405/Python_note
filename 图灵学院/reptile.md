# 0 爬虫准备工作
- 参考资料
    - python 网络数据采集，图灵工业出版
    - 精通python爬虫框架Scrapy,人民邮电出版社
    - [python3网络爬虫]（http://blog.csdn.net/c406495762/article/details/72858983）
    - [Scrapy官方教程]（https://scrapy-chs.readthedocs.io/zh_CN/0.24/intro/tutorial.html）
    
- 前提知识
    - url
    - http
    - web前端,html,css,js
    - ajax
    - re,xpath
    - xml
    
# 1.爬虫简介
- 爬虫定义：按照一定规则，自动抓取万维网信息的程序或脚本

- 两大特性：
    - 能按作者要求下载数据或内容
    - 能自动在网上流窜

- 三大步骤：
    - 下载网页
    - 提取正确的信息
    - 根据一定的规则跳到另外的网页执行上述的两步

- 爬虫分类
    - 通用爬虫（百度）
    - 专用爬虫（聚焦爬虫）
    
- python网络包简介
    - python2.x:
        
        urllib,urllib2,urllib3,httplib,httplib2,requests
        
        urllib和urllib2配合使用或者requests
        
    - python3.x:
    
        urllib,urllib3,httplib2,requests
        
        urllib.requests
   
# 2.urllib
- 包含模块
    - urllib.request: 打开和使用urls
    - urllib.error: 包含urllib.request产生的错误，用try捕捉
    - urllib.parse: 包含解析url的方法
    - urllib.robotparse: 解析robots.txt文件
    - 案例V1
    
- 网页编码问题的解决
    - chardet: 可以自动检测页面的编码格式，但是可能有误
    - 需要安装，conda install chardet
    - 案例v2
    
- urlopen 的返回对象
    - 案例v3
    - geturl: 返回请求对象的url
    - info: 请求反馈对象的meta信息
    - getcode: 返回http 请求状态码
    
- request.data 的使用
    - 访问网络的两种方法
        - get
            - 利用参数给服务器传递信息
            - 参数为dict,然后用parse编码
            - 案例v4
        - post
            - 一般向服务器传递参数使用
            - post是把信息自动加密处理
            - 如果我们使用post信息，需要用到data参数
            - 使用post,意味着http请求头可能需要更改：
                
                Content-Type:application/x-www.form-urlencode                
                Content-Length:数据长度                
                简而言之，一旦更改请求方法，请注意与其它请求头部信息相适应
                
            - urllib.parse.urlencode可以将字符串自动转成上面的
                - 案例v5
            - 为了更多的设置请求信息（仿浏览器），单纯的通过urlopen函数已经不太好用了
            - 需要利用request.Request 类
                - 案例v6
            
                
- urllib.error
    - URLError产生的原因：
    
        - 没网       
        - 服务器连接失败  
        - 指不到服务器      
        - 是OSError的子类
        - 案例v7
    - HTTPError，是URLError的一个子类
        - 案例v8                   
        
    - 两者区别：
        - HTTPError是对应的HTTP请求的状态码，如果是400以上的则引发
        - URLError对应的是网络出现问题，包括状态码错误
        - 关系OSError --> URLError --> HTTPError

- UserAgent
    - UserAgent: 用户代理，简称UA，属于heads的一部分，服务器通过UA来判断访问者身份
    - 常见的UA值，使用的时候可以直接复制粘贴，也可以用浏览器访问的时候抓包
        
        一些UA类型：https://blog.csdn.net/xumesang/article/details/77678583
        
    - 设置UA可以通过两种方式
        - heads
        - add_header
        - 案例v9
        
- ProxyHandler处理（代理服务器）
    - 使用代理ip，是爬虫常用的手段
    - 获取代理服务器的地址：
        - www.xicidaili.com
        - www.goubanjia.com
    - 代理建议比较多避免被封
    - 基本使用步骤：
        1、设置代理地址
        2、创建ProxyHandler
        3、创建Opener
        4、安装Opener
    - 案例v10

- cookie & session
    - 由于http的无记忆性，人们为了弥补这个缺憾，采用的一个补充协议
    - cookie是发放给用户（浏览器）的一段信息，session是保存在服务器上对应的另一半信息，用来记录用户信息
    - cookie和session的区别：
        - 存放位置不同
        - cookie不安全
        - session会保存在服务器上一段时间，会过期
        - cookie单个不超过4k，很多浏览器限制一个站点最多保存20个
    - session的存放位置
        - 存在服务端
        - 一般情况，session是放在内存中或数据库中
        - 案例v11,可以看到没有cookie就是未登录状态
    - 使用cookie登录
        - 案例v12,直接把cookie复制下来，放入请求头
        - http模块包含一些关于cookie的模块，通过它们可以自动使用cookie
            - CookieJar
                - 管理存储cookie，向传出的http请求添加cookie
                - cookie存储在内存中，CookieJar实例回收后cookie将消失
            - FileCookieJar（filename，delayload=None,policy=None）:
                - 使用文件管理cookie
                - filename是保存cookie的文化部
            - MozillaCookieJar（filename，delayload=None,policy=None）
                - 创建与mocilla浏览器cookie.txt兼容的FileCookieJar实例
            - LwpCookieJar（filename，delayload=None,policy=None）
                - 创建与libwww-perl标准兼容的Set-cookie3格式的FileCookieJar实例
            - 它们的关系：CookieJar → FileCookieJar → MozillaCookieJar&LwpCookieJar
            
        - 利用cookjar访问网站案例：v13
            - 自动使用cookie登录，大致流程是：
            - 打开登录页面后自动通过用户名密码登录
            - 自动提取返回的cookie
            - 利用cookie访问隐私页面
        - handler是Handler的实例，常见参看案例代码：
            - 用来处理复杂请求
        
                    创建cookiejar的实例
                    cookie = cookiejar.CookieJar()
                    生成cookie的管理器
                    cookie_handler = request.HTTPCookieProcessor(cookie)
                    创建http请求管理器
                    http_handler = request.HTTPSHandler()                
                    生成https管理器
                    https_handler = request.HTTPSHandler()                
                    创建请求管理器
                    opener = request.build_opener(http_handler,https_handler,cookie_handler)
        
        - 创立handler后，使用opener打开，打开后相应的业务由相应的handler处理
        
        - cookie作为一个变量，打印出来
            - 案例v14
            - cookie的属性：
            
                    name : 名称
                    value : 值
                    domain : 可以访问的域名
                    ...
        
        - cookie 的保存-FileCookieJar
            - 案例v15
            
                    创建filecookiejar的实例
                    filename = 'cookie.txt'
                    cookie = cookiejar.MozillaCookieJar(filename)
            
        - cookie的读取
            - 案例v16
            
                    cookie = cookiejar.MozillaCookieJar()
                    cookie.load('cookie.txt', ignore_expires=True, ignore_discard=True)


- SSL
    - SSL证书：
    - 遇到不信任的证书如何忽略：
        - 案例v17
        
                利用非认证上下文环境替换认证的上下文环境
                ssl.create_default_https_context = ssl._create_unverified_context   

- js加密
    - 有的反爬虫策略采用js对需要传输的数据进行加密处理
    - 经过加密，传输的就是密文，但是
    - 加密函数或者过程一定是在浏览器上完成，也就一定会把代码（js代码）暴露给使用者
    - 通过阅读加密算法，就可以模拟出加密过程，从而破解
        -  案例 v18-1、v18-2
        
- ajax
    - 异步请求
    - 一定会有url,请求方法，可能有数据
    - 一般使用json格式
        - 案例：v20 爬取豆瓣电影
        
# Request-献给人类
- HTTP for Humans更简洁，更友好
- 继承了urllib的所有特性
- 底层使用的是urllib3
- 开源地址：https://www.github.com/requests/requests
- 中文文档地址：http://docs.python-requests.org/zh_CN/latest/index.html
- 安装：pip install requests
- 使用：
    - get请求：
        - requests.get(url)
        - requests.request('get',url)
        - 可以带有harders和parmas参数
        - 案例v21
        
    - get返回内容：
        - 案例v22
    
    - post 
        - rsp = requests.post(url,data=data)
        - 案例v23
        - date,headers要求dict类型
        
    - proxy
        
            proxies = {
            "http":"address of proxy"
            "https":"address of proxy
            }
            
            rsp = requests.request("get","http://xxxxxx",proxies = proxies}
            
        - 代理有可能报错，如果使用的人多，考虑安全问题，可能会被强行关闭
        
    - 用户验证
        - 代理验证
        
                #可能需要使用HTTP basic Auth,可以这样
                #格式为 用户名：密码@地址
                proxy = {"http":"china:123456@192.168.1.123:4444"}
                rsp = requests.get("http://baidu.com",proxies=proxy)
         
    - web客户端验证
        - 如果遇到web客户端验证，需要添加auth=(user,password)
                
                auth=("test1","123456")  #授权信息
                rsp = requests.get("http://baidu.com",auth=auth)
    
    - cookie 
        - requests可以自动处理cookie信息
        - 案例v24
                
                rsp = requests.get("http://xxxxxxxxxxxx")
                #如果对方服务器给传送过来cookie信息，则可以通过反馈的cookie属性得到
                cookiejar=rsp.cookies
                
                #可以将cookiejar转换为字典
                cookiedict = requests.utils.dict_from_cookiejar(cookiejar)
    - session 
        - 跟服务器端的session不是一个性质
        - 模拟一次会话，从客户端访问服务器开始，到客户端访问断开
        - 能让我们跨请求时保存某些参数，比如在同1个session实例中发出的所有请求之间保存cookie   
            
                #创建session对象，可以保持cookie值
                ss = requests.session()
                
                headers = {"User-Agent":"xxxxxxxxxxxx"}
                
                data = {"name":"xxxxxxxxxxxx"} 
                
                #此时，由创建的session管理请求,负责发出请求
                ss.post(url,data=data,headers=headers) 
                rsp = ss.get('xxxxxxxxxxxxxx')    
                
    - https请求验证ssl证书
        - 参数verify负责表示是否验证ssl证书，默认是True
        - 如果不需要验证ssl证书，则设置为False
            
                rsp = requests.get("https://www.baidu.com",verify=False)
                      
                
                
                
                
                
                
                
                
                
                
                      