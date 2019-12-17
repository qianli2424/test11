#!/usr/din/python3
# -*- coding:utf8 -*-
# @Author:欢
'''
猜拳
1.计算机出拳与player玩家出拳
2.对出拳进行比较，分辨电脑赢还是玩家赢还是平局
3.设计玩一次之后就显示是否继续游戏，输入y或Y都可继续
4.玩的时候，你有底分5分，赢+1，输-1，平局不加分。每次游戏结束都显示你的总分数
5.如果总分数小于0，就不能再玩了，提示game over
6.还可以计算胜率问题
'''
import random

print('------------------------猜拳----------------------')

lowest_mark = 5                                   # 底分
win_rate = ''                                     # 胜率
tie = 0                                           # 平局
match_won = 0                                     # 赢
fail = 0                                          # 输
count = 0                                         # 场次
x =''


while x !='y':
    computer =random.choice(['石头','剪刀','布'])  # 电脑出拳
    input1 =input('玩家出拳：')                    # 玩家出拳

# 判断猜拳
    if (computer=='石头')and(input1=='石头') or (computer=='剪刀')and(input1=='剪刀') or (computer=='布')and(input1=='布'):
        print('平局！电脑出拳：{},玩家出拳：{}'.format(computer,input1))
        tie +=1
        count +=1
    elif (computer=='石头')and(input1=='剪刀') or (computer=='剪刀')and(input1=='布') or (computer=='布')and(input1=='石头'):
        print('你输了！电脑出拳：{},玩家出拳：{}'.format(computer,input1))
        fail +=1
        lowest_mark -=1
        count +=1
    elif (computer=='石头')and(input1=='布') or (computer=='剪刀')and(input1=='石头') or (computer=='布')and(input1=='剪刀'):
        print('你赢了！电脑出拳：{},玩家出拳：{}'.format(computer,input1))
        lowest_mark +=1
        match_won +=1
        count +=1

    print('你的总分数为：{}分，总共玩了：{}场,赢了：{}场,输了：{}场,平局：{}场,胜率：{}%'.format(lowest_mark,count,
           match_won,fail,tie,match_won/count*100))

    x =input('是否继续游戏，输入任意键继续，y 退出')
# 判断游戏是否继续
    if x=='y':
        break

# 判断玩家分数
    if lowest_mark == 0:
        print('game over')
        break














