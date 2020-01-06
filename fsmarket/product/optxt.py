# -*- coding=utf8 -*-
#@author:qianli  date：2020/1/4
# 文件说明：文本文档txt的操作

f = open('lib.txt','r',encoding='utf8') #读的标准语法
content = f.readlines()     #读到全部内容到列表中
print(content)      #打印输出结果
'''要把读出来的每一个元素转为字典'''
allbook=[]
for ele in content:
    print(ele)  #读出来后发现多了空行，所以需要去\n并且要把每个元素拆出来
    line = ele.strip('\n').split(',')   #拆完后会得到一个列表
    '''列表要转字典，可以往空字典中追加数据，一行数据加在一个字典中'''
    dictline={}
    dictline['bookid']=line[0]  #把第0个元素加入到bookid的字典元素中
'''要把for循环的结果（字典，一个图书数据）保存到列表中，表示完事'''
allbook.append(dictline)


f=open('lib.txt','a',encoding='utf8')
bookinfo = '4,python从入门到放弃,第3排第3个位置'
f.write('\n'+bookinfo)   #:w
f.close()           #:q
