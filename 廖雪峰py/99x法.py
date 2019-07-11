# -*- coding：UTF-8 -*-
#九九乘法表
#参考http://www.runoob.com/python3/python3-99-table.html
for i in range (1,10):
	for j in range (1,i+1):
		print('{}x{}={}\t'.format(i,j,i*j),end='')
	print()