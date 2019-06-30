# -*- coding: utf-8 -*-
'''
访问一个网站
更改自己的UA进行伪装
'''

from urllib import request,error

if __name__ == '__main__':
    url = 'http://www.baidu.com'

    try:
        #1、使用head方法伪装UA
        # headers = {}
        # headers['User-Agent'] = 'Mozilla/5.0 (Windows; U; Windows NT 5.2) Gecko/2008070208 Firefox/3.0.1'
        # req = request.Request(url, headers=headers)

        #2、使用add_header方法
        req = request.Request(url)
        req.add_header("User-Agent", 'Opera/9.27 (Windows NT 5.2; U; zh-cn)')

        #正常访问
        rsp = request.urlopen(req)
        html = rsp.read().decode()
        print(html)

    except error.HTTPError as e:
        print('HTTPError: {0}'.format(e))

    except error.URLError as e:
        print('URLError: {0}'.format(e))

    except Exception as e:
        print('Exception:{0}'.format(e))

print('DONE>...')