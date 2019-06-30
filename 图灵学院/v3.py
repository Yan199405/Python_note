import urllib
from urllib import request

if __name__ == '__main__':
    url = 'http://www.baidu.com'

    rsp = urllib.request.urlopen(url)

#查看urlopen返回
    print(type(rsp))
    print(rsp)
    #print(rsp.read().decode('utf8'))



#查看以下返回
    print('URL: {0}'.format(rsp.geturl()))
    print('Info: \n{0}'.format(rsp.info()))
    print('Code: {0}'.format(rsp.getcode()))


