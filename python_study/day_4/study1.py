# -*- coding-utf8 -*-
# author :xiaosheng
#文件说明 

import  openpyxl

users = {'admin':['123456','unlock',0],'test':['123456','unlock',0]}

# users = [{'name':'admin','password':'123456','status':'unlock','fail':'0'},{'name':'test','password':'123456','status':'unlock','fail':'0'}]
#1.用户输入用户名和密码，判断是否成功登录，
# 如果成功登录，状态要设为unlock，失败次数要设为0
#2.如果用户名或密码为空，则直接提示
#3.如果密码错误，则提示登录失败，错误次数+1
#4.如果密码连续错误导致错误次数超过3次，则锁定该账号。账号锁定也是不能登录的
#5.如果登录失败，则提示用户还有几次机会

print('请登录')
error = 3
while True:
    if users[name][2]==3:
     # users[name][1] = 'lock'
     print('错误次数超过3次锁定该账号')
     print(users)
     break

    name = input('输入用户名')
    password = input('输入密码')

    if name == '' or password == '':
        users[name][2] += 1
        error -= 1
        print('用户名或密码为空!登入机会还', error)
        continue

    elif name not in users.keys():
        users[name][2] += 1
        error -= 1
        print('用户名不存在!登入机会还',error)
        continue

    elif users[name][0] != password:
        users[name][2] += 1
        error -= 1
        print('密码错误!登入机会还', error)
        continue

    elif name !='' and name in users.keys() and users[name][0]!='' and users[name][0]==password and \
            users[name][1]!='lock' and users[name][2]<=3:
        users[name][1]='unlock'
        users[name][2]=0
        print('登入成功')
        print(users[name])
        break






