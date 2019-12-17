# -*- coding=utf8 -*-
#@author:qianli
# 文件说明：基本数据类型，有5种基本数字类型，他们之间可以相互转换，可以通过type()获取类型

#input()方法是通过输入得到一个值保存到变量中，但是默认是 str字符串型
#在python中有五种数字类型 int 整数  float 小数（浮点数） complex复数 long长整数 bool布尔
#还有4种字符类型：str字符串,list列表，tuple元组，dict字典
#数字是可以进行数学计算的，字符是不能进行数学计算
#因为python定义的变量，不需要声明变量类型。可以让变量很灵活
# 但是这时候可能会出现经过几次处理就不知道是什么类型了，可以用type(var)查看类型
# id(var)用来判断该变量在内存中的存储位置
var = 1.5     #给var赋值了1，所以此时var是一个整数，值为1
print(id(var))
var = 1   #给var赋值1.2，所以此时var是一个小数，值为1.2
var = 'hello'
str = 'hello'
print(var)
print(type(var))
print(id(var))
print(id(str))