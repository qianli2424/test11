# -*- coding=utf8 -*-
#@author:qianli  date：2020/1/2
# 文件说明：
import requests

kwargs = {'method':'GET','url':'https://api.weixin.qq.com/cgi-bin/token','params':{'grant_type':'client_credential','appid':'wx508a5cacbbfc1141','secret':'fa4fc7f17ddead12d7cdcd994e7d2543'}}
'''
requests.request()方法中，能输入的是：(method='GET',url=url,params=param)
但是request()方法支持输入可变参数，如果是字典，则写法为： requests.request(**kwargs)
这个**kwargs需要满足参数规则：{'method':'GET','url':'url','params':'param'}
即**kwargs中的key为参数名称，value为后面的用户输入值
'''
res = requests.request(**kwargs)
print(res.text)

assert 'mthod' in kwargs




url='https://api.weixin.qq.com/cgi-bin/token'
param = {'grant_type':'client_credential','appid':'wx508a5cacbbfc1141','secret':'fa4fc7f17ddead12d7cdcd994e7d2543'}
res = requests.request(method='GET',url=url,params=param)
print(res.text)
args = ['a','b','c']
def func(*args):
    pass    #*args是多个数据，args则为1个列表
def fun(**kwargs):
    kwargs是字典     #有key和value，key被认为参数名称，value被认为是输入值