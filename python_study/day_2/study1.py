# -*- coding-utf8 -*-
# author :xiaosheng
#文件说明 
#创建时间:2019/12/17




import random
print('------石头剪刀布游戏开始------')
punches = ['石头', '剪刀', '布']
score = 3
zimu = 'Y'
win = 0
lose = 0

while zimu == 'Y':
    computer = random.choice(punches)
    print('系统出拳:', computer)
    player=input('请出拳:（剪刀，石头，布）')
    while player not in punches:
       player=input('输入错误!请出拳:（剪刀，石头，布），请重新出拳:')
    print('-------游戏过程------')
    print('系统出拳:',computer,'我方出拳:',player)
    if computer==player:
        print('真默契!平局')
    elif (computer=='石头' and player=='布') or (computer=='布' and player=='剪刀') or (computer=='剪刀' and player=='石头'):
        win += 1
        score += 1
        print('你赢了！积分数', score)
    elif (player=='石头' and computer=='布') or (player=='布' and computer=='剪刀') or (player=='剪刀' and computer=='石头'):
        lose += 1
        score -= 1
        print('你输了!积分数',score)
    if score == 0:
        result = int(win/(win+lose) * 100)
        print('game over!你游戏的胜率:', result, '%')
        break
    zimu='A'
    while zimu !='Y' and zimu !='N':
        zimu = input('是否继续游戏Yes/No')
        zimu=zimu.strip().upper()[0]
if zimu=='N':
    result = float(win/(win+lose)*100)
    print('你游戏的胜率:',result,'%')

















