# -*- coding=utf8 -*-
#@author:qianli
# 文件说明：登录注册，在用户列表中有用户名、密码、状态、错误次数
users = {'admin':['123456','unlock',0],'test':['123456','unlock',0]}
# users = [{'name':'admin','password':'123456','status':'unlock','fail':'2'},
#          {'name':'admin','password':'12345','status':'unlock','fail':'2'}]
#1.用户输入用户名和密码，判断是否成功登录，
# 如果成功登录，状态要设为unlock，失败次数要设为0
#2.如果用户名或密码为空，则直接提示
#3.如果密码错误，则提示登录失败，错误次数+1
#4.如果密码连续错误导致错误次数超过3次，则锁定该账号。账号锁定也是不能登录的
#5.如果登录失败，则提示用户还有几次机会
while True:
    name=input("请输入用户名")
    if name==" ":
        print("用户名不能为空")
    elif name not in users.keys():
        print("用户名不存在")
    else:
        while True:
            passwd=input("请输入密码")
            if passwd==" ":
                print("密码不能为空")
            elif users[name][0]!=passwd:
                print("密码错误")
                users[name][2]+=1
                print("你还有{}次机会".format(3-users[name][2]))
            if users[name][2]==3:
                print("密码超出错误次数，被锁定")
                break
        break