# -*- coding=utf8 -*-
#@author:qianli
# 文件说明：
import random

goal = random.choice(['左','中','右'])
player = input('请输入扑点球的方向：')
if player==goal:
    print('扑到了点球')
print(goal)

