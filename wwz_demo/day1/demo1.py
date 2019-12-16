#!/usr/bin/python3
# _*_ coding:utf-8 _*_
# @Author:啊志
# @Time:2019/9/23 9:20
import random
n=1
while n<4:
    num=random.randint(1,10)
    a=int(input("请输入一个数:"))
    if a==num:
        print("恭喜你猜对了,本次随机数为:{}".format(num))
        # break
    else:
        print("猜错了,本次随机数为:{}".format(num))
    # b=input("是否继续游戏，按任意键继续，按n/N结束")
    n += 1








