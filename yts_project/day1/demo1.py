# _*_coding:utf-8 _*_
#@Author:YTS
#@文件说明：随机数大于5

import random

num = random.randint(1,10)
if num>5:
    print('猜对了')
    print('猜对了随机数为：',num)
else:
    print('猜错了随机数为：',num)

