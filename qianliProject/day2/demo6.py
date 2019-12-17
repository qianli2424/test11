# -*- coding=utf8 -*-
#@author:qianli
# 文件说明：输入一个字符串，统计这个字符串中数字多少个，大写字母多少个，小写字母多少个

file = 'abc123ASF0900'
count=1     #循环次数
i=0         #file的下标
num_count=0
'''
1.创建一个输入，为需要统计的字符串
2.然后得到这个字符串的长度
3.做循环，循环就是长度是多少，就循环多少次
4.把要统计的字符串分别把每一个字符拿出来进行比较
5.分别统计汇总
'''
len = len(file)     #文件的长度
while count<=len:
    print(file[2*i],end=',')
    if(file[i].isdigit()):
        num_count = num_count+1
    i = i+1
    count = count+1

