# _*_coding:utf-8 _*_
#@Author:YTS
#@文件说明：猜拳

'''
1.计算机出拳与player玩家出拳
2.对出拳进行比较，分辨电脑赢还是玩家赢还是平局
3.设计玩一次之后就显示是否继续游戏，输入y或Y都可继续
4.玩的时候，你有底分5分，赢+1，输-1，平局不加分。每次游戏结束都显示你的总分数
5.如果总分数小于0，就不能再玩了，提示game over
6.还可以计算胜率问题
'''
import random

end_points=5 #底分
count=1 #次数
win=0   #赢
fail=0  #败
deuce=0 #平局

while count<10:
    player = input('玩家出：')
    fist = random.choice(['石头','剪刀','布'])
    print('电脑出:',fist)

    if player==fist:
        print('平局')
        deuce = deuce+1
        get=input('是否继续y/n')
        if get != 'y':
            break

    elif (player=="石头" and fist=="剪刀") or(player=="剪刀" and fist=="布") or (player=="布" and fist=="石头"):
        print('66666玩家赢了，您的分数为：',end_points+1)
        end_points = end_points+1
        win = win+1
        get=input('是否继续y/n')
        if get != 'y':
            break

    else:
        print('很遗憾电脑赢了，您的分数为：',end_points-1)
        end_points = end_points-1
        fail = fail+1
        get=input('是否继续y/n')
        if get != 'y':
            break

    if end_points<=0:
        break
    count += 1

print('game over 当前游戏已结束')
print('您一共赢了：{}，输了：{}，平局：{}，总局数：{}，胜率为：{}%'.format(win,fail,deuce,count,win/count*100))

