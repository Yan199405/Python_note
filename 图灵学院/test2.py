import re
import requests

url = 'http://www.baidu.com'

# response = requests.get(url)
# # 返回的是Unicode格式的数据
# html = response.text
# print(type(html),html)
#
# # 返回cookie对象
# cookiejar = response.cookies
# print(cookiejar)
# # 将cookie转为字典
# cookiedict = requests.utils.dict_from_cookiejar(cookiejar)
# print(cookiedict)

## 实现人人网登陆
ssion = requests.session()

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}

# data = {'user':'17793217774','password':'abmm1314'}

ssion.post('http://www.renren.com/SysHome.do')

response = ssion.get('http://www.renren.com/971353277/newsfeed/photo')

print(response.text)
print(ssion.cookies)
ssion.cookies=None
