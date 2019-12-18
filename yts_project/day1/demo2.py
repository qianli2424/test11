# _*_coding:utf-8 _*_
#@Author:YTS
#@文件说明：
import random

print('#-#-#-#-#扑点球#-#-#-#-#')

end_points=5
time=0

while time<10:
    a=int(input('请输入你要扑的方向:'))
    num = random.randint(1,3)

    if a==num:
        end_points = end_points+1
        print('恭喜你扑到点球了分数加一为',end_points)
    else:
        end_points = end_points-1
        print('没扑到分数-1为',end_points)

    time+=1

    if end_points<0:
        break

print('您的最终得分为',end_points)
print('#############')
print('游戏结束，再见')
print('#############')