# 页面解析和数据提取
- 结构数据：先有结构，再谈数据
    - JSON文件
        - JSON Path
        - 转换成Python类型进行操作（json类）
    - XML
        - 转换成Python类型（xmltodict）
        - XPath
        - CSS选择器
        - 正则
- 非结构化数据：先有数据，再谈结构
    - 文本
    - 电话号码
    - 邮箱地址
    - 通常处理此类数据，我们使用正则表达式（re）
    - HTML文件
        - 正则
        - XPath
        - CSS选择器
        
# 正则表达式
- 一套规则可以在字符串文本中进行搜改查
- 案例v25,mach的基本使用
- 正则常用方法：
    - match：从开始位置开始查找，一次匹配
    - search：从任何位置查找，一次匹配
    - findall：全部匹配，返回列表
    - finditer: 全部匹配返回迭代器
    - split：分割字符串，返回列表
    - sub: 替换
    ...
# XML 
- XML(EXtensibleMarkupLanguage)
- http://www.w3school.com.cn/xml/index.asp
- 案例：v28
- 概念：父节点，子节点，先辈节点，兄弟节点，后代节点

#XPath
- XPath（XML Path Language），是一门在XML文档中查找信息的语言
- 官方文档：http://www.w3school.com.cn/xpath/index.asp
- XPath开发工具：
    - 开元的XPath开发工具：XMLQuire
    - chrome插件：xpath helper
    - Firefox插件：XPath   CHecker
- 常用路径表达式：
    - nodename：选取此节点的所有子节点
    - /：从根节点开始选
    - //：选取元素，而不考虑元素的具体位置
    - . :当前节点
    - .. :父节点
    - @：选取属性
    - 案例：
        - bookstore：选取bookstore下的所有节点
        - /bookstore：选取根元素
        - bookstore/book：选取bookstore的所有为book的子元素
        - //book：选取book子元素
        - //@lang：选取名为lang的所有属性
- 谓语（Predicates）
    - 谓语用来查找某个特定的节点，被镶嵌在方括号中
    - /bookstore/book[1]：选取第一个属于bookstore下叫book的元素
    - /bookstore/book[last()]:选取最后一个属于bookstore下叫book的元素
    - /bookstore/book[last()-1]:选取倒数第二个属于bookstore下叫book的元素
    - /bookstore/book[position()<3]:选取属于bookstore下叫book的前两个元素
    - /bookstore/book[@lang]:选取属于bookstore下叫book的，含有属性lang的元素
    - /bookstore/book[@lang="cn"]:选取属于bookstore下叫book的，含有属性lang的值是cn的元素
    - /bookstore/book[@price < 90]:选取属于bookstore下叫book的，含有属性price，且值小于90的元素
    - /bookstore/book[@price < 90]/titlt:选取属于bookstore下叫book的，含有属性price，且值小于90的元素的子元素title
    
- 通配符
    - ‘*’：任何元素节点
    - ‘@*’：匹配任何属性节点
    - node（）：匹配任何类型的节点
    ...
# lxml库
- python的HTML/XML的解析器
- 官方文档：http://lxml.de/index.html
- 功能：
    - 解析HTML
    - 文件读取
    - etree和XPath的配合使用
# css选择器 BeautifulSoup4
- 现在使用BeautifulSoup4
- 安装: BeautifulSoup
- 几个常用提取工具的比较
    - 正则： 很快，不好用，不用安装
    - beautifulsoup4：慢，使用简单，安装简单
    - lxml：比较快，使用简单，安装简单
    - 案例：v33.py
- 四大对象
    - Tag
        - 对应Html中的标签
        - 可以通过soup.tag_name
        - 案例： v34.py
    - NavigableString
        - 对应内容值
            
    - BeautifulSoup
        - 表示的是一个文档的内容，大部分把它当做tag对象
    - Comment
        - 特殊类型的NavagableString对象
        - 其输出则内容不包括注释符号
- 遍历文档对象
    - contents:tag 的子节点以列表的方式给出
    - children： 子节点以迭代形式返回
    - descendants：所子孙节点
    - strings
    - 案例：v34.py 第二部分
- 搜索文档对象
    - findall（name，attrs，recursive，text，**kwargs）
        - name：按照那个字符串搜索，可以传入的内容为
            - 字符串
            - 正则表达式
            - 列表
        - keywortd参数，可以用来表示属性
        - text：对应tag的文本值
        - 案例：34.py  第三部分
- css选择器
    - 使用soup.select,返回一个列表
    - 通过标签名称：soup.select('title')
    - 通过类名：soup.select('.content')
    - id查找：soup.select("#name_id")
    - 组合查找：soup.select("div #input_content")
    - 属性查找：soup.select("img[class='photo'])
    - 获取tag内容:tag.get_text
    - 案例：35.py
    
# 动态HTML
## 爬虫跟反爬虫
## 动态HTML介绍
- JavaScrapt
- jQuery
- Ajax
- DHTML
- Python采集动态数据
    - 从Javascript代码入手采集
    - Python第三方库运行Javascript，直接采集你在浏览器看到的页面
## Selenium + PhantomJS
- Selenium:web自动化测试工具
    - 安装：pip install --upgrade pip
    - 自动加载页面
    - 获取数据
    - 截屏
- PhantomJS(幽灵)
    - 基于Webkit的无界面的浏览器
    - Selenium 库有一个WebDriver的API
    - webDriver可以跟页面上的元素进行各种交互，可以进行爬取
    - 案例v36
    
- chrome + chromedriver
    - 下载安装chrome
    - 下载安装chromedriver
        
- Selenium操作主要分两大类：
    - 得到UI元素
        - find_element_by_id
        - find_elements_by_name
        - find_elements_by_xpath
        - ...
    - 基于UI元素操作的模拟
        - 单击
        - 右键
        - 拖拽
        - 输入
        - 可以通过导入ActionsChains类来做到
    - 案例：v37
                
    

    
     
    
    

    
    
    
    
    