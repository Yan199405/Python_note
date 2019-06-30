# -*- coding: utf-8 -*-
from urllib import request, parse
from http import cookiejar

# 创建cookiejar的实例
cookie = cookiejar.CookieJar()
# 生成cookie的管理器
cookie_handler = request.HTTPCookieProcessor(cookie)
# 创建http请求管理器
http_handler = request.HTTPSHandler()

# 生成https管理器
https_handler = request.HTTPSHandler()

# 创建请求管理器
opener = request.build_opener(http_handler, https_handler, cookie_handler)


def login():
    '''
    负责初次登录
    需要输入用户名和密码，用来获取登录cookie的凭证
    :return:
    '''

    # 此url需要从登录from 的action属性中提取
    url = 'https://www.shcaee.com/login.jsp'

    # 此键值需要从登录form的两个对应input中提取name属性
    data = {
        'user.account': 'xxx',
        'user.userPwd': 'xxx',
        'loginCode':'XFUT'
    }
    # 把数据进行编码
    data = parse.urlencode(data)
    # 创建一个请求对象
    req = request.Request(url, data=data.encode())
    # 使用opener发起请求
    rsp = opener.open(req)


'''
执行完login()后把cookie打印出来
'''


if __name__ == '__main__':
    login()
    print(cookie)
    for item in cookie:
        print('type:', type(item))
        print(item)
        for i in dir(item):
            print(i)