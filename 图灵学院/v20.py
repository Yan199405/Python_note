'''
爬取豆瓣电影数据
了解ajax的基本
'''
from urllib import request
import json

url = 'https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action=&start=0&limit=1'

rsp = request.urlopen(url)
data = rsp.read().decode()

data = json.loads(data)

print(data)