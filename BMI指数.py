#-*- coding: utf-8 -*-
#BMI公式（体重除以身高的平方）
# 低于18.5：过轻
# 18.5-25：正常
# 25-28：过重
# 28-32：肥胖
# 高于32：严重肥胖
# 用if-elif判断并打印结果：
height = float(input('请输入你的身高：'))
weight = float(input('请输入你的体重：'))
BMI = weight/(height**2)
if BMI > 32:
	print('您已严重超重！！！')
elif BMI >= 28:
	print('您处于肥胖，请注意！！')
elif BMI >= 25:
	print('您已过重！')
elif BMI >= 18.5:
	print('体重正常。')
else:
	print('太轻！！！！')