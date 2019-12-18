# -*- coding=utf8 -*-
#@author:qianli
# 文件说明：


num=1
info = []
while num<5:
    name = input('请输入姓名')
    info.append(name)       #往info列表中追加name元素
    num = num+1
print(info)
#做完后，想把第1个值修改一下
temp = input('修改第1个元素的值为：')
info[0] = temp
print(info)
#列表支持增加元素，修改元素，删除元素
