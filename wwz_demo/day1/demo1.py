#!/usr/bin/python3
# _*_ coding:utf-8 _*_
# @Author:啊志
# @Time:2019/9/23 9:20
import random
num=random.randint(1,10)
a=input("请输入一个数：")
if a==num:
    print("恭喜你猜对了,本次随机数为:{}".format(num))
else:
    print("猜错了,本次随机数为:{}".format(num))


