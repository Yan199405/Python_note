# -*- coding: utf-8 -*-

'''练习
杨辉三角定义如下：

          1
         / \
        1   1
       / \ / \
      1   2   1
     / \ / \ / \
    1   3   3   1
   / \ / \ / \ / \
  1   4   6   4   1
 / \ / \ / \ / \ / \
1   5   10  10  5   1
把每一行看做一个list，试写一个generator，不断输出下一行的list：'''
def triangles():
    a=[1]
    while True:
        yield a
        b=[0]+a
        c=a+[0]
        a=[b[n]+c[n] for n in range(0,len(c))]
