# -*- coding=utf8 -*-
#@author:qianli
# 文件说明：模拟完成一个注册的功能

'''
1.注册功能有用户名、密码和确认密码，需要输入这三个内容方可提交注册
2.需要进行注册的判断，理论上会有为空判断
3.核心判断：密码和确认密码必须相同，否则会失败
4.用户名不能是已被注册过的用户名
5.注册完成之后，需要查看我已注册过多少用户
6.继续注册请按Y，结束注册请按N
'''
username_list = []
userinfo_list = []

while True:
    name = input('请输入用户名：')
    password = input('请输入密码：')
    password2 = input('请输入确认密码：')

    if name not in username_list and name!='' and password!='' and password2!='' and password==password2:
        #注册成功，我把要注册信息写入进来
        userinfo = [name,password,password2]
        userinfo_list.append(userinfo)  #注册成功，写入用户表
        #username_list.append(name)      #把用户列表单独写进来
        print('注册成功')
    elif name in username_list:
        print('用户名已被注册')
    elif password!=password2:
        print('两次密码不一致')
    elif name=='' or password=='' or password2=='':
        print('用户名、密码或确认密码为空，注册失败')
    else:
        print('对不起，注册失败')

    #把userinfo_list列表中的username提取出来，形成一个用户列表
    for user in userinfo_list:
        username_list.append(user[0])