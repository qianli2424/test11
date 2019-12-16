#!/usr/bin/python3
# _*_ coding:utf-8 _*_
# @Author:啊志
# 2019/12/16/19:06
# @Email:1427245437@qq.com
import random
'''
代码优化：
1.判断这个数是否大于5，进行输出。并且输出这个随机数的具体值
2.产生手工输入，让我们可以手工输入一个数，保存到变量中
3.然后再与num进行比较，如果==，则是猜对了，如果!=则是猜错了
4.带预习：猜测结果是猜对了，你的数小了，你的数大了
5.游戏只玩一次，不好玩。我想猜3次（循环）
6.万一第1次就猜对了，肯定游戏结束（结束语句）
'''
n=1
while n<4:
    num=random.randint(1,10)
    a=int(input("请输入一个数:"))
    if a==num:
        print("恭喜你猜对了,本次随机数为:{}".format(num))
    elif a<num:
        print("你的数猜小了，请重猜，本次随机数为：{}".format(num))
    elif a>num:
        print("你的数猜大了，请重猜,本次随机数为：{}".format(num))
        # break
    else:
        print("猜错了,本次随机数为:{}".format(num))
    # b=input("是否继续游戏，按任意键继续，按n/N结束")
    n += 1

