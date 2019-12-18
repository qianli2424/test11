#!/usr/din/python3
# -*- coding:utf8 -*-
# @Author:欢
#  while循环语句加if判断语句
import random

b = 1
num = random.randint(1,10)                     # 生成随机整数

while b<4:
    a = int(input('请输入一个1-10的随机整数为：'))    # 手工输入数字

    if a == num:                                     # 判断，当满足这个条件时，输出以下信息
        print('恭喜你猜对了！本次系统生成随机数为：{}'.format(num))
        break                                        # 强制结束
    elif a > num:
        print('你猜的数大了，下次继续努力。\n系统生成的随机数为：{}'.format(num))
        b += 1
    elif a < num:
        print('你猜的数小了，下次继续努力。\n系统生成的随机数为：{}'.format(num))
        b += 1
    else:
        print('猜错了，下次继续努力')

    # input('是否继续游戏？按任意继续')


'''
代码优化：
1.判断这个数是否大于5，进行输出。并且输出这个随机数的具体值
2.产生手工输入，让我们可以手工输入一个数，保存到变量中
3.然后再与num进行比较，如果==，则是猜对了，如果!=则是猜错了
4.带预习：猜测结果是猜对了，你的数小了，你的数大了
5.游戏只玩一次，不好玩。我想猜3次（循环）
6.万一第1次就猜对了，肯定游戏结束（结束语句）
'''