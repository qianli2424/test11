# _*_coding:utf-8 _*_
#@Author:YTS
#@文件说明：随机数
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



# num = random.randint(1,10)
# if num>5:
#     print('猜对了')
#     print('猜对了随机数为：',num)
# else:
#     print('猜错了随机数为：',num)

b=0
while b<3:
    a=int(input('请随机输入一个整数:'))
    num = random.randint(1,10)
    if a==num:
        print('恭喜你猜对了随机数为：',num)
        break
    elif a<num:
        print('老弟猜小了随机数为：', num)
    elif a>num:
        print('老妹猜大了随机数为：', num)
    else:
        print('猜错了随机数为：',num)
    b+=1
print('游戏结束，再见')
print('测试')
