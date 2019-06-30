#-*- coding: utf-8 -*-
#允许计算两个数的乘积，变成可接收一个或多个数并计算乘积：
def product(*k):
	j=1
	if k==():
	   raise TypeError
	else:
		for n in k:
			j=j*n
	return j