'''
HTTPError的使用
'''

from urllib import request, error

if __name__ == '__main__':
    url = 'http://www.shcaee.com/test.html'

    try:
        req = request.Request(url)
        rsq = request.urlopen(req)
        html = rsq.read().decode()
        print(html)

    except error.HTTPError as e:
        print('HTTPError: {0}'.format(e))    #由于HTTPError是URLError的子类，所以有限返回的是HTTPError 的错误

    except error.URLError as e:
        print('URLError: {0}'.format(e))

    except Exception as e:
        print(e)

# 在爬虫代码里一定要写错误处理