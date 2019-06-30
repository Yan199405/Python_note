# -*- coding: utf-8 -*-
from  urllib import request
import  ssl

#利用非认证上下文环境替换认证的上下文环境
ssl.create_default_https_context = ssl._create_unverified_context

url = 'https://www.shcaee.com'

rsp = request.urlopen(url)

html = rsp.read().decode()

print(html)











