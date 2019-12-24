# -*- coding=utf8 -*-
#@author:qianli
# 文件说明：
import openpyxl
name = 'test1.xlsx'
f = open('test.txt','r')
info = f.readlines()
f.close()
try:
    #可能发生异常的代码
    print(1/0)
except Exception as e:
    #打印错误
    print(e)
else:
    #如果不发生错误，则执行以下代码
    print('h')