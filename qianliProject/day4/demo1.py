# -*- coding=utf8 -*-
#@author:qianli
# 文件说明：
userlist = [['admin',123456],['test',123456],['root',123456],['mysql',123456],['sa',123456]]
for user in userlist:
    for a in user:
        print(a,end='\t')
    print()     #什么都不做，但会换行

for x in 'abcdefg':
    print(x,end='\t')
print()
for x in [1,2,3,4,5,6,7,8]:
    print(x)
range(0,9)  #产生0-9的整数序列数
for x in range(len(userlist)):
    print(x,end='-----------')
'''
temp = []
for user in userlist:
    print(user)
    name = user[0]
    temp.append(name)
print(temp)
'''
