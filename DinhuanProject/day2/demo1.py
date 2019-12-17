#!/usr/din/python3
# -*- coding:utf8 -*-
# @Author:欢
'''
1.扑点球，由系统生成1,2,3三个数字表示点球的位置
2.底分为5分，扑对+1，扑错了-1，每猜一次显示分数
3.如果底分为0，游戏结束，或者游戏次数大于10次，也结束
'''

import random

print('--------------------扑点球游戏------------------------')
print('----------------------开始----------------------------')

lowest_mark = 5                                   # 底分
count = 0                                         # 次数

while count < 10:
    input1 = int(input('请输入点球的位置数：'))  # 手工输入位置数
    num_random = random.randint(1,3)             # 系统生成随机数

    # 判断是否扑对点球
    if input1 == num_random:
        print('恭喜你扑对了！你扑的位置{}，点球的位置{}'.format(input1,num_random))
        lowest_mark = lowest_mark+1
    else:
        print('你扑错了！你扑的位置{}，点球的位置{}'.format(input1, num_random))
        lowest_mark = lowest_mark-1

    print('你还有{}分'.format(lowest_mark))
    count +=1

    # 判断底分
    if lowest_mark == 0:
        print('---------------------游戏结束------------------------')


print('---------------------游戏结束------------------------')






