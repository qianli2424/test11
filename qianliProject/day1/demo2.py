# -*- coding=utf8 -*-
# author:qianli
# 文件说明：输入input语句

#做程序，是需要输入用户的数据。输入用户数据有两种方式，一种是直接定义变量，一种是input
#定义变量，在python中非常简单，变量名=值 即可，不需要设置变量类型。
name = 'xiang'   #定义一个变量
print('welcome'+name)
print(name*3,'i love you')
#input()是输入的意思，是通过控制台做手工输入，并且把输入的结果保存到name2中
#一般输入都会给出提示消息，说需要输入什么样的数据，在input中直接写便可
name2 = input('please input your name:')
print('your name is:',name2)
#int()方法强制转为整数
#str()方法强制转为字符串
#float()方法强制转为小数
age=int(input('请输入你的年龄：'))
print('你的年龄为：',age,'岁')
print('你明年的年龄为：',age+1)
fatherAge = age*2-10
print('你爸的年龄为：',fatherAge)
fatherAge=input('请输入你爸的年龄：')
motherAge=input('请输入你妈的年龄：')
age = fatherAge-motherAge
print('你爸比你妈大：',age,'岁')