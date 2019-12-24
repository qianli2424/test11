# -*- coding=utf8 -*-
#@author:qianli
# 文件说明：

f = open('edit.txt','r')
#把=切割掉，变成一个列表。列表的第0个值为key，第1个值为value组成dict
text = f.readlines()
map = {}
for line in text:
    info = line.split('=')
    key = info[0]
    value = info[1].strip('\n')
    map[key] = value        #这是在字典中加元素
print(map)