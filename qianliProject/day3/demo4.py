# -*- coding=utf8 -*-
#@author:qianli
# 文件说明：
str = 'abcdefg123456789'
temp = list(str)
print(temp)
temp.reverse()
print(temp)
str2 = ''.join(temp)
print(str2)

info = 'hello world i love beijing'
list = info.split(' ')
print(list)
print(len(list),'----')