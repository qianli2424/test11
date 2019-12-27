# -*- coding=utf8 -*-
#@author:qianli
# 文件说明：

#猜数字，我想猜数字这个事情封装成一个方法
import random

def guessnum(userinput):
    computer = random.randint(1,10)
    if int(userinput)==computer:
        result = '恭喜你，猜对了'
    else:
        result = '对不起，没猜对，正确答案为：'+str(computer)+'，您的答案为：'+str(userinput)
    return result

def formatinput(userinput):
    if userinput=='shitou' or userinput=='shi tou':
        userinput='石头'
    elif userinput=='jiandao' or userinput=='jian dao':
        userinput='剪刀'
    elif userinput=='bu':
        userinput='布'
    return userinput
def getscore():
    #去读excel的最后一行，分数列的数据
    pass
def guessquan(input):
    userinput = formatinput(input)
    computer = random.choice(['石头','剪刀','布'])
    result = ''
    score = getscore()
    if userinput== computer:
        result = '平局'
    elif userinput>computer:
        score = score+1
        result = '玩家赢'
    elif userinput<computer:
        score = score-1
        result = '玩家输'
    else:
        result = '其他错误'
    return userinput, computer, result, score