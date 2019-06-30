#请使用迭代查找一个list中最小和最大值，并返回一个tuple：
def findMinAndMax(L):
    if len(L)==0:
        return(None, None)
    min=L[0]
    max=L[0]
    for a in L:
        if a < min:
            min = a
        elif a > max:
            max = a
    return ('min:',min,'max:',max)
