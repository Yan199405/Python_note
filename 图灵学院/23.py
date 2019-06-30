import requests
import json

baseurl = 'https://fanyi.baidu.com/sug'

#存放用来模拟form的数据一般是dict格式
data = {
    'kw': 'girl'   #gril是翻译输入英文的内容，应该是用户输入，此处属于硬编码
}


#我们需要构造一个请求头，请求头应该包含传入的数据的长度
#request要求传入的是一个dict

headers = {
    #因为使用post,至少应该包含content-length字段
    'Content-Length': str(len(data))
}
#有了headers'data'url,就可以尝试发出请求了
rsp = requests.post(baseurl, data=data, headers=headers)

print(rsp.text)
print(rsp.json())

# 把json字符串转换为字典
# json_data = json.loads(json_data)
# print('转换后类型：', type(json_data))
# print(json_data)
#
# for item in json_data['data']:
#     print(item['k'], "--", item['v'])