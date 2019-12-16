# _*_coding:utf-8 _*_
#@Author:YTS
#@文件说明：随机数大于5
import random
# import random
#
# num = random.randint(1,10)
# if num>5:
#     print('猜对了')
#     print('猜对了随机数为：',num)
# else:
#     print('猜错了随机数为：',num)


a=int(input('请随机输入一个数字:'))
num = random.randint(1,3)
if a==num:
    print('猜对了')
    print('猜对了随机数为：{}'.format(num))
else:
    print('猜错了随机数为：',num)