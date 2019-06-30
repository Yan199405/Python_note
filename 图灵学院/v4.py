from urllib import request, parse
'''
掌握对url进行参数编码的方法
需要使用parse模块
'''
if __name__ == '__main__':
    url = 'http://www.baidu.com/s?'
    wd = input("input your keyword:")
    #要想使用data需要使用dict
    qs = {
        'wd':wd
    }
    #转换URL编码
    qs = parse.urlencode(qs)
    print(qs)

    fullurl = url +qs
    print(fullurl)

    rsp = request.urlopen(fullurl)
    html = rsp.read()
    html = html.decode()
    print(html)