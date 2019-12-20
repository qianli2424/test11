# -*- coding=utf8 -*-
#@author:qianli
# 文件说明：
info = {'name':'admin','age':18,'job':['ceo','cto'],'money':{'house':5,'gupiao':1000}}

x = info.values()       #会得到一个特殊的列表
y = info.keys()         #会得到一个特殊的列表
z = info.items()        #把元素拉出来，组到列表中
print(z)