#从wsgiref模块导入
from wsgiref.simple_server import make_server
#导入我们自己编写的application函数：
from hello import application

#创建一个服务器，ip地址为空，端口8000，处理函数式application
httpd = make_server('',8000,application)
print('Serving http on port 8000...')
#开始监听http请求

httpd.serve_forever()