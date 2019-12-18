# -*- coding-utf8 -*-
# author :xiaosheng
#文件说明 
#创建时间:2019/12/17




import random
score = 5



while True:
    punches = ['石头', '剪刀', '布']
    computer = random.choice(punches)
    print('系统出拳:', computer)
    player=''
    print('------石头剪刀布游戏开始------')
    player=input('请出拳:（剪刀，石头，布）')
    while player not in punches:
       print('输入错误，请重新出拳：')
       player=input()
    print('-------游戏过程------')
    print('系统出拳:',computer)
    print('我方出拳:',player)
    if (computer=='石头' and player=='布') or \
      (computer=='布' and player=='剪刀') or \
      (computer=='剪刀' and player=='石头'):
       score +=1
       print('你赢了！分数', score)

    elif computer==player:
       print('真默契，平局！')
    else:
       score -= 1
       print('你输了!分数',score)

    # zimu = input('是否继续游戏Y/N')
    # if zimu == 'N':
    #    break














