# _*_coding:utf-8 _*_
#@Author:YTS
#@文件说明：
file = 'abc123ASf0900'

num_count=0
num_lower=0
num_isupper=0

for i in file:
    if i.isdigit():
        num_count = num_count+1

    if i.islower():
        num_lower = num_lower+1
    if i.isupper():
        num_isupper = num_isupper+1

print('数字为{}，小写字母为{}，大写字母为{}'.format(num_count,num_lower,num_isupper))



file = 'abc123ASf0900'
print(file[1::2])