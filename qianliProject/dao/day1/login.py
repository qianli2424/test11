# -*- coding=utf8 -*-
#@author:qianli
# 文件说明：定义一个Login类，有输入项username和password，有login方法
class Login:
    #__init__函数一般是用来赋值的
    def __init__(self,username,password):
        self.name = username
        self.password = password

    def login(self):
        if self.name=='admin' and self.password=='123456':
            print('登录成功')
            return {'errcode':0,'errmsg':'login success'}
        else:
            print('登录失败')
            return {'errcode':1,'errmsg':'login fail'}

a = Login('admin1','123456')         #Login()实例化哪个类，产生这个类的对象，实例化是调用__init__方法
a.login()