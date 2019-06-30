from urllib import request, parse
'''
破解有道词典
'''

def youdao(key):
    url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'

    data = {
        'i':'gril',
        'from':'AUTO',
        'to':'AUTO',
        'smartresult':'dict',
        'client':'fanyideskweb',
        'salt':'15564209362043',
        'sign':'587525df5c53ab63367dfc89618bdfe9',
        'ts':'1556420936204',
        'bv':'470df6afd582fe67e18c2221dab59fb3',
        'doctype':'json',
        'version':'2.1',
        'keyfrom':'fanyi.web',
        'action':'FY_BY_REALTlME'
    }
    #参数data需要是bytes
    data = parse.urlencode(data).encode()
    headers = {
        'Accept':'application/json, text/javascript, */*;q=0.01',
       # 'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh,zh-CN;q=0.9,zh-TW;q=0.8,en;q=0.7',
        'Connection':'keep-alive',
        'Content-Length':'237',
        'Content-Type':'application/x-www-form-urlencoded;charset=UTF-8',
        'Cookie':'OUTFOX_SEARCH_USER_ID=-1351299443@10.169.0.83;JSESSIONID=aaateSfcfrU379zvA6HPw;OUTFOX_SEARCH_USER_ID_NCOO=1171279639.482143;___rl__test__cookies = 1556420936198',
        'Host': 'fanyi.youdao.com',
        'Origin': 'http://fanyi.youdao.com',
        'Referer': 'http://fanyi.youdao.com /',
        'User-Agent': 'Mozilla/5.0(WindowsNT10.0;Win64;x64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/70.0.3538.77Safari/537.36',
        'X-Requested With': 'XMLHttpRequest'
    }
    req = request.Request(url,data=data,headers=headers)
    rsp = request.urlopen(req)
    html = rsp.read().decode()

    print(html)

if __name__ == '__main__':
    youdao('gril')