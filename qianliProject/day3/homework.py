# -*- coding=utf8 -*-
#@author:qianli
# 文件说明：猜拳
'''
1.计算机出拳与player玩家出拳
2.对出拳进行比较，分辨电脑赢还是玩家赢还是平局
3.设计玩一次之后就显示是否继续游戏，输入y或Y都可继续
4.玩的时候，你有底分5分，赢+1，输-1，平局不加分。每次游戏结束都显示你的总分数
5.如果总分数小于0，就不能再玩了，提示game over
6.还可以计算胜率问题
'''
import random

flag = 'Y'

while flag.upper()=='Y':
    compute = random.choice(['石头', '剪刀', '布'])
    player = input('游戏开始了，请出拳：')
    # 是赢还是输，对猜拳做判断
    if compute == player:
        print('平局')
    elif (player == '石头' and compute == '剪刀') or (player == '剪刀' and compute == '布') or (
            player == '布' and compute == '石头'):
        print('恭喜你，赢了猜拳')
    elif (player == '石头' and compute == '布') or (player == '布' and compute == '剪刀') or (
            player == '剪刀' and compute == '石头'):
        print('很遗憾，你输了')
    print('你的出拳为：' + player + '，电脑出拳为：' + compute)
    print('--------------------------------------------------------')

    flag = 'A'  #让flag既不为Y又不为N，就会进入到下面的while循环
    while flag.upper()!='Y' and flag.upper()!='N':
        flag = input('are you continue? Yes or No：')
        flag = flag.strip()[0]               #去掉空格，取首字母
