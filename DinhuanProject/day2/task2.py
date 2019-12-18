#!/usr/din/python3
# -*- coding:utf8 -*-
# @Author:欢

import random

print('------------------------猜拳----------------------')

lowest_mark = 5                                   # 底分
win_rate = ''                                     # 胜率
tie = 0                                           # 平局
match_won = 0                                     # 赢
fail = 0                                          # 输
count = 0                                         # 场次
x ='Y'


while x.upper()=='Y':
    computer =random.choice(['石头','剪刀','布'])  # 电脑出拳
    input1 =input('玩家出拳：')                    # 玩家出拳

# 赋值
    if input1=='shitou' or input1=='shi tou':
        input1='石头'
    if input1=='jiandao' or input1=='jian dao':
        input1='剪刀'
    if input1=='bu':
        input1='布'

# 判断猜拳
    if (computer=='石头'and input1=='石头') or (computer=='剪刀'and input1=='剪刀') or (computer=='布'and input1=='布'):
        print('平局！电脑出拳：{},玩家出拳：{}'.format(computer,input1))
        tie +=1
        count +=1
    elif (computer=='石头'and input1=='剪刀') or (computer=='剪刀'and input1=='布') or (computer=='布'and input1=='石头'):
        print('你输了！电脑出拳：{},玩家出拳：{}'.format(computer,input1))
        fail +=1
        lowest_mark -=1
        count +=1
    elif (computer=='石头'and input1=='布') or (computer=='剪刀'and input1=='石头') or (computer=='布'and input1=='剪刀'):
        print('你赢了！电脑出拳：{},玩家出拳：{}'.format(computer,input1))
        lowest_mark +=1
        match_won +=1
        count +=1

    print('你的总分数为:%.2f分，总共玩了：%.2f场,赢了：%.2f场,输了：%.2f场,平局：%.2f场,胜率：%.2f%%' % (lowest_mark, count,
                match_won, fail, tie,match_won / count * 100))
    print('-------------------------------------------------------------------------------------')

    # 判断玩家分数
    if lowest_mark == 0:
        print('game over')
        break

    # 判断游戏是否继续
    # x再次赋值，当x不等于y,又不等于n时， 使x可以进入子循环中
    x ='m'
    while x.upper() !='Y' and x.upper() !='N':
        x =input('是否继续游戏，Yes or No ?')
        x =x.strip()[0]             # 去空格，取首个字母
