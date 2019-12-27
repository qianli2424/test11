# -*- coding=utf8 -*-
#@author:qianli
# 文件说明：

def info(**args):   #对列表做操作，双星是对字典做操作
    print(args)

info(name='qianli',age=18)
#在输入参数的时候，name='qianli' name会变成key，'qianli'会变成value
#name不要引号，=后边的value值如果是字符串则又需要引号