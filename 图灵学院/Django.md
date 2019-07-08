# Django系统
- 环境
    - py3.6
    - django1.8
- 参考资料
    - [django中文教程]（https://yiyibooks.cn/）
    - 《Django架站的16堂课》
# 环境搭建
- anaconda+pycharm
- anaconda使用
    - conda list：显示当前环境安装的包
    - conda env list：显示安装的虚拟环境
    - conda create -n env_name python=3.6 ：创建py3.6的虚拟环境，名称为env_name
    - 激活conda环境
        - linux：source activate env_name
        - win： conda activate env_name
    - pip install django==1.8
    

# 后台需要的流程

# 创建一个Django项目：
- 命令行启动
    - anaconda prompt 命令行 启动这个项目：
        - 创建项目：django-admin startproject tlxy
        - 启动项目：python manage.py runserver
- pycharm方式启动
    - 需要配置
# 路由系统-urls
- 创建app
    - app: 负责一个具体业务或者一类具体业务的模块
    - python manage.py startapp appname
- 路由
    - 按照具体的请求url，导入到相应的业务处理模块的一个功能模块
    - Django的信息控制中枢
    - 本质上是接收的url和对应的处理模块的映射
    - 在接收url请求的匹配上用的re
    - url的具体格式见urls.py
     
    - 注意：
        - 接受的url是什么，即如何用re对传入的url进行匹配
        - 已知的url匹配到哪个处理模块
- 子路由
    - 如果所有应用的URL都在主路由文件urls.py中，会导致文件臃肿
    = 可以把urls.py具体功能分散到各app中
        - 从Django.conf.urls导入include
        - 注意此时RE部分的写法
        - 添加include导入
    - 使用方法
        - 确保include被导入
        - 主路由中指定子路由
        
                cat urls.py
                from teacher import teacher_url
                urlpatterns = [
                   url(r'^teacher/',include(teacher_url)),
                ]
                //申明teacher开头的全部通过子路由teacher_url处理

        - 写子路由
        
                cat teacher_url.py
                urlpatterns = [
                    url(r'liudana/', tv.do_app),
                ]
                //申明路由对应的views中处理函数为do_app
        - 编写viws函数
        
                cat views.py
                def do_app(r):
                    return HttpResponse('这是个子路由')