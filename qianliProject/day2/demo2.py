# -*- coding=utf8 -*-
#@author:qianli
# 文件说明：数字类型的处理

#对数字类型可以做五则运算 +（加） -（减） *（乘） /（除） %（取余） //（整除）
num1 = float(input("请输入一个数："))
num2 = float(input("请输入第二个数："))

result1 = num1/num2
result2 = num1%num2
result3 = num1//num2

print(num1,'除以',num2,'的结果为：',result1)
print('{}除以{}的结果为：{}'.format(num1,num2,result2))
print('%f整除%f的结果为：%f' %(num1,num2,result3))