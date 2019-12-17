#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Author:tan
# @Time:2019/12/16 16:51
# @Email:1164355091@qq.com
import random

for i in range(1,4):
    num=random.randint(1,10)
    num_1=int(input('请输入一个数'))
    if num_1==num:
        print('系统随机数为{}'.format(num),'您输入的数为{}'.format(num_1))
        print('猜对了')
        break
    else:
        print('系统随机数为{}'.format(num),'您输入的数为{}'.format(num_1))
        print('猜错了')