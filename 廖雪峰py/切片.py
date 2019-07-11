#利用切片操作，实现一个trim()函数，去除字符串首尾的空格，注意不要调用str的strip()方法：
def trim(s):
    while s!='' and s[0]==' ':
        s=s[1:]
    while s!='' and s[-1]==' ':
        s=s[:-1]
    return s
