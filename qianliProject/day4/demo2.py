# -*- coding=utf8 -*-
#@author:qianli
# 文件说明：
x,y=1,0
min = x if x<y else y
list1 = [x*x for x in range(1,10)]
print(list1)

t = tuple(list1)
print(t)

t2 = (1,2,3)
t3 = list(t2)
print(t3)