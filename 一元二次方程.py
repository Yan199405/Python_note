#-*- coding:utf-8 -*-
#解一元二次方程
#请定义一个函数quadratic(a, b, c)，接收3个参数，返回一元二次方程：ax2 + bx + c = 0 的两个解


# 提示：计算平方根可以调用math.sqrt()函数：

# >>> import math
# >>> math.sqrt(2)
# 1.4142135623730951
#----------------------------------这是自己写的-------------------------------
import math
def Error():
	print ('ERROR!代尔塔不能小于零，请重新输入...')

def quadratic(a, b, c):
	delta=b*b-4*a*c

	if delta<0:
		Error()
	elif delta==0:
		x=-b/(2*a)
		return x,x
	else:
		x1=(-b + math.sqrt(delta))/(2*a)
		x2=(-b - math.sqrt(delta))/(2*a)
		return x1,x2
	
a=int(input("Please input 'a' :"))
b=int(input("Please input 'b' :"))
c=int(input("Please input 'c' :"))

print(quadratic(a,b,c))

#----------------------------------这是网上搜的-------------------------------
		# import math
		# def Quadrartic(a,b,c):
				# x1=(-b+math.sqrt(b1*b1-4*a1*c1))/(2*a)
				# x2=(-b-math.sqrt(b1*b1-4*a1*c1))/(2*a)
				# return(x1,x2)
		# def Error1():
			# print("错误1：二次项系数不能为0，请重新输入：")
			# print("")
		# def Error2():
			# print("错误2：代尔塔不能小于0，请重新输入：")
			# print("")

		# while True:
			# a1=float(input("请输入二次项系数：（不能等于0）"))
			# b1=float(input("请输入一次项系数："))
			# c1=float(input("请输入常数项："))		
			# if a1!=0 and (b1*b1-4*a1*c1)>=0:
				# print (Quadrartic(a1,b1,c1))
				# print ("Done")
				# print ("")	
			# else:
				# if a1==0:
					# Error1()
				# if (b1*b1-4*a1*c1)<0:
					# Error2()		