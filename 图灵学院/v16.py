# -*- coding: utf-8 -*-
from urllib import request,parse
from  http import cookiejar

#创建cookiejar的实例
cookie = cookiejar.MozillaCookieJar()
cookie.load('cookie.txt', ignore_expires=True, ignore_discard=True)
#生成cookie的管理器
cookie_handler = request.HTTPCookieProcessor(cookie)
#创建http请求管理器
http_handler = request.HTTPSHandler()

#生成https管理器
https_handler = request.HTTPSHandler()

#创建请求管理器
opener = request.build_opener(http_handler,https_handler,cookie_handler)

# def login():
#     '''
#     负责初次登录
#     需要输入用户名和密码，用来获取登录cookie的凭证
#     :return:
#     '''
#
#     #此url需要从登录from 的action属性中提取
#     url = 'https://www.shcaee.com/login.jsp'
#
#     # 此键值需要从登录form的两个对应input中提取name属性
#     data = {
#         'user.account': 'caee0110',
#         'user.userPwd': 'caee0110',
#         'loginCode':'XFUT'
#     }
#     #把数据进行编码
#     data = parse.urlencode(data)
#     #创建一个请求对象
#     req = request.Request(url, data=data.encode())
#     #使用opener发起请求
#     rsp = opener.open(req)

def getHomePage():
    url = 'https://www.shcaee.com/index.jsp?token=B116A2E4945C418B19A0905000011154'
    #如果已经执行了login函数，则opener自动包含相应的cookie值
    rsp = opener.open(url)

    html = rsp.read().decode()
    with open('rsp.html','w') as f:
        f.write(html)
if __name__ == '__main__':
    getHomePage()