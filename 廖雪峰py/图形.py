# -*- coding: UTF-8 -*-
#图形打印
i = 1
x = 4
while i <= 9:
    if i <= 5:
        print("*" * i)
    elif i > 5:
        print("*" * x)
        x -= 1
    i += 1