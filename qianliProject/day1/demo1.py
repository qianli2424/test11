# -*- coding=utf8 -*-
# author:qianli
# 文件说明：输出语句的练习 print()

#python中注意事项：不能随便空格，因为空格会表达层次

#1.可以输出普通数据，用单引号或双引号括起来普通字符串数据
print('hello world')
#2.还可以输出数字，如果是数字则不用引号括起来
#3.可以输出语句中，输出表达式（五则运算、复杂运行等）
print(1+2)
print(3.5*5)
#4.可以对字符串做加法，乘法
#5.虽然字符串可以做加法，但是不能字符串+数字，这会报错。
print('your age is'+str(18))    #把数字强行变成字符串
print('your age is',18)
#6.有一些转义字符\n \t等。因为字符串都是ASCII码字符，用\n表示换行，\t表示tab
print('your age is\t',18)       #会产生一个tab，4个空格
#中间遇到了\t会变成4个空格，如果要改变原来含义，就需要多加一个\，变成\\t
print('the path is C:\test\python')
#在python中，可以使用r'字符串'表示原始串，防转义raw
print(r'the path is C:\test\python')
#所有的print语句都会换行，如果要不换行，可使用print('字符串',end='结束符')
print('hello',end='****')