from urllib import request,parse

'''
处理js加密代码
'''
'''
通过查找，能找到JS中操作代码：
js格式化：http://tool.oschina.net/codeformat/js
1、这个是计算salt的公示：
        r = "" + (new Date).getTime(),
        i = r + parseInt(10 * Math.random(), 10);
        也就是i = "" + (new Date).getTime()+parseInt(10 * Math.random(), 10) 
2、sign：sign: n.md5("fanyideskweb" + e + i + "@6f#X3=cCuncYssPsuRUE")
md5一共需要四个字符串，第一个和第四个为固定值，i是salt,e应该就是明文密码单词
'''

def getSalt():
    '''
    salt公式是："" + (new Date).getTime()+parseInt(10 * Math.random(), 10)
    把它翻译为python代码:
    :return:
    '''
    import time,random
    salt = int(time.time()*1000) + random.randint(0,10)
    return salt

def getMD5(v):
    import hashlib
    md5 = hashlib.md5()
    md5.update(v.encode('utf-8'))   #update需要bytes格式的参数
    sign = md5.hexdigest()
    return sign

def getSign(key,salt):
    sign = "fanyideskweb" + key + str(salt) + "@6f#X3=cCuncYssPsuRUE"
    sign = getMD5(sign)
    return sign

def youdao(key):
    url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
    salt = getSalt()
    data = {
        'i':key,
        'from':'AUTO',
        'to':'AUTO',
        'smartresult':'dict',
        'client':'fanyideskweb',
        'salt':str(salt),
        'sign':getSign(key,salt),
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
        'Content-Length':len(data),
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