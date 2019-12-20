# -*- coding=utf8 -*-
#@author:qianli
# 文件说明：

list = ['admin','test','root']  #这3个值都有对应的下标
map = {'name1':'admin','name2':'test'}    #下标不用数字来表示，用字符串来表示
#map要求key不能相同
info = {'name':'admin','age':18,'job':['ceo','cto'],'money':{'house':5,'gupiao':1000}}
for x in info:  #得到的竟然是下标（key）
    print(x,end=',,,')
    print(info[x])      #value，会得到value值
print()
print('--------------------')
name = list[0]
name = info['money']['gupiao']
name = info['job'][1]
print(name)

#修改值
list[0] = 'qianli'
print(list)
info['age'] = 23
print(info)
info['son'] = 'deng'    #对一个没有的key进行赋值，就是追加个元素。
print(info)
info.pop('age')         #踢掉某个下标（key）
del(info['money'])      #删一个元素
print(info)
