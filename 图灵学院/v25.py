import re

s = r'([a-z]+) ([a-z]+)'
#正则分了两个小组，以小括号为单位，'+'表示至少有一位
pattern = re.compile(s, re.I)   #s.I表示忽略大小写

m = pattern.match("Hello world wide web")

s = m.group(0) #表示返回匹配的整个子串
print(s)

a = m.span(0) #表示返回成功的整个子串的跨度
print(a)

s = m.group(1) #表示返回匹配的第一个子串
print(s)

a = m.span(1) #表示返回成功的第一个子串的跨度
print(a)

s = m.group() #等价于m.group(1),m.group(2)...

print(s)

