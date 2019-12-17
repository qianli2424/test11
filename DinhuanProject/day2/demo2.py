#!/usr/din/python3
# -*- coding:utf8 -*-
# @Author:欢

a = input('请输入任意字符：')

len = len(a)
num_isdigit = 0
num_islower = 0
num_isupper = 0

for i in a:
    if i.isdigit():        # 当i 是数字时
        num_isdigit += 1
        print(i)
    elif i.islower():      # 当i是小写字母时
        num_islower +=1
        print(i)
    elif i.isupper():      # 当i是大写字母时
        num_isupper +=1
        print(i)

print('你输入的字符串中，数字共有：{},小写字母共有：{}，大写字母共有：{}'.format(num_isdigit,num_islower,
num_isupper))





