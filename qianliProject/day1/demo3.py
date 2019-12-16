# -*- coding=utf8 -*-
# author:qianli
# 文件说明：if判断语句
import random

num = random.randint(1,10)  #生成随机整数

if 3==num:                  #判断，当满足某个条件时
    print('猜对了')        #做这个事情
    print('系统生成的随机数就是3')
else:                       #否则
    print('猜错了')
'''
代码优化：
1.判断这个数是否大于5，进行输出。并且输出这个随机数的具体值 
2.产生手工输入，让我们可以手工输入一个数，保存到变量中
3.然后再与num进行比较，如果==，则是猜对了，如果!=则是猜错了
'''
