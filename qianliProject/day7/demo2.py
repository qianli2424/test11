# -*- coding=utf8 -*-
#@author:qianli
# 文件说明：
import os

if os.path.exists('edit2.txt'):
    print('存在')
    print()
    print('hello world')
else:
    f = open('edit2.txt','w')
    f.close()