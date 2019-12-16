# -*- coding-utf8 -*-
# author :xiaosheng
#文件说明 
#创建时间:2019/12/16


# 代码优化：
# 1.判断这个数是否大于5，进行输出。并且输出这个随机数的具体值
# 2.产生手工输入，让我们可以手工输入一个数，保存到变量中
# 3.然后再与num进行比较，如果==，则是猜对了，如果!=则是猜错了
# 4.带预习：猜测结果是猜对了，你的数小了，你的数大了
# 5.游戏只玩一次，不好玩。我想猜3次（循环）
# 6.万一第1次就猜对了，肯定游戏结束（结束语句）

import random
i=1


num = random.randint(1,10)
if num>0:
    print('这个随机数:',num)

while i<=3:
    i += 1
    num2 = input('请数一个数字:')
    if int (num2) == num:
        print('猜对了:游戏结束')
        break
    elif int(num2)>num:
        print('你的数大了')
    elif int(num2)<num:
        print('你的数小了 ')
else:
     print('游戏结束')

