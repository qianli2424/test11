# _*_coding:utf-8 _*_
#@Author:YTS
#@文件说明：
import random

print('#-#-#-#-#扑点球#-#-#-#-#')

End_points=5
time=0

while time<10:
    a=int(input('请输入你要扑的方向:'))
    num = random.randint(1,3)

    if a==num:
        End_points = End_points + 1
        print('恭喜你扑到点球了分数加一为',End_points)

    else:
        End_points = End_points - 1
        print('没扑到分数-1为',End_points)
    time+=1

    if End_points<0:
        break
print('您的最终得分为',End_points)
print('#############')
print('游戏结束，再见')
print('#############')