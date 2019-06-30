from urllib import request
from bs4 import BeautifulSoup

url = 'http://www.baidu.com'

rsp = request.urlopen(url)
content = rsp.read()

soup = BeautifulSoup(content,'lxml')

#bs自动转码
content = soup.prettify()
print('==' * 50)
print(soup.link)
print(soup.link.name)
print(soup.link.attrs)
print(soup.link.attrs['type'])


print('==' * 50)
print(soup.title)
print(soup.title.name)
print(soup.title.attrs)
print(soup.title.string)

print('==' * 50)
print(soup.name)
print(soup.attrs)


#第二部分

print('==' * 50)
for node in soup.head.contents:
    if node.name == 'meta':
        print(node)
    if node.name =='title':
        print(node.string)
#第三部分

import re
print('=='*50)
tags = soup.find_all(re.compile('^me'),content='always')
for tag in tags:
    print(tag)
