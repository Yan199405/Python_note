
'''
利用parse模块模拟post请求
分析百度词典
分析步骤：
1、打开f2调试
2、network-里发现输入gril每输入一个字母都有请求变化，请求地址是Request URL: https://fanyi.baidu.com/sug
3、network-ALL-Hearders查看到name：sug的fromdata中kw：gril
4、返回内容的格式是json,所以我们要使用json包负责处理json格式
'''

from urllib import request, parse
import json

'''
大致流程是：
1、利用data构造内容，然后urlopen打开
2、返回一个json格式的结果
3、结果就应该是一个grid的释义
'''

baseurl = 'https://fanyi.baidu.com/sug'

#存放用来模拟form的数据一般是dict格式
data = {
    'kw': 'girl'   #gril是翻译输入英文的内容，应该是用户输入，此处属于硬编码
}
#需要使用parse模块对data进行编码
data = parse.urlencode(data).encode('utf-8')     #data必须通过.encode()转换为bytes

#我们需要构造一个请求头，请求头应该包含传入的数据的长度
#request要求传入的是一个dict

headers = {
    #因为使用post,至少应该包含content-length字段
    'Content-Length': len(data)
}
#有了headers'data'url,就可以尝试发出请求了
rsp = request.urlopen(baseurl, data=data)
json_data = rsp.read().decode('utf-8')
print(json_data)

# 把json字符串转换为字典
json_data = json.loads(json_data)
print('转换后类型：', type(json_data))
print(json_data)

for item in json_data['data']:
    print(item['k'], "--", item['v'])
