#-*- coding=utf8 -*-
#author:caodaliang
import random

b = 0
while b <3:
    num =int(random.randint(1,8))  #生成随机整数
    a=int(input('输入一个数:'))
    if num>5:
        print('这个随机数是:',num)
    if a==num:                  #判断，当满足某个条件时
        print('猜对了')        #做这个事情
        print('系统生成的随机数就是',num)
    if a!=num:                       #否则
        print('猜错了,随机数为:',num)
    if a>num:
        print('你的数大了:',num)
    if a<num:
        print('你的数小了:',num)
    b +=1
    ,


# '''
# 代码优化：
# 1.判断这个数是否大于5，进行输出。并且输出这个随机数的具体值
# 2.产生手工输入，让我们可以手工输入一个数，保存到变量中
# 3.然后再与num进行比较，如果==，则是猜对了，如果!=则是猜错了
# 4.带预习：猜测结果是猜对了，你的数小了，你的数大了
# 5.游戏只玩一次，不好玩。我想猜3次（循环）
# 6.万一第1次就猜对了，肯定游戏结束（结束语句）
# '''