'''
使用参数headers和params
研究返回结果
'''

import requests
url = 'http://www.baidu.com/s?'

kw = {
    'wd':'王八蛋'
}

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
}

rsp = requests.get(url, params=kw, headers=headers)

print('rsp.text:', rsp.text)
print('rsp.content:', rsp.content)
print('rsp.url:', rsp.url)
print('rsp.encoding:', rsp.encoding)
print('rsp.status_code:', rsp.status_code)#请求返回码