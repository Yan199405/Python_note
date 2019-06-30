'''
URLError的使用
'''

from urllib import request, error

if __name__ == '__main__':
    url = 'http://www.baidu.com'

    try:
        req = request.Request(url)
        rsq = request.urlopen(req)
        html = rsq.read().decode()
        print(html)

    except error.URLError as e:
        print('URLError: {0}'.format(e))

    except Exception as e:
        print(e)

# 在爬虫代码里一定要写错误处理