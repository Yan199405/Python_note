'''
利用requests下载页面
自动检测页面编码
'''
from  urllib import request
import urllib
import chardet

if __name__ == '__main__':
    url='http://www.baidu.com'

    rsp = urllib.request.urlopen(url)

    html =  rsp.read()

    #利用 chardet自动检测

    cs = chardet.detect(html)
    print(type(cs))

    #使用get取值保证不会出错
    html = html.decode(cs.get("encoding", 'utf-8'))   #没有获取到编码就自动取utf-8
    print(html)