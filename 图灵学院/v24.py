import requests

url = 'http://www.baidu.com'

rsp = requests.get(url)

cookiejar = rsp.cookies

#将cookiejar转换成字典

cookiedict = requests.utils.dict_from_cookiejar(cookiejar)

print('type(cookiedict):', type(cookiedict))
print(cookiedict)