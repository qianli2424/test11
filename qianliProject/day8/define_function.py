# -*- coding=utf8 -*-
#@author:qianli
# 文件说明：往excel中保存户口信息，进行用户登录。登录姓名、性别、年龄

def info(name,sex,age=0):
    if name=='' or sex=='':
        print('姓名或性别未输入')
    else:
        msg = [name,sex,age]
    return msg