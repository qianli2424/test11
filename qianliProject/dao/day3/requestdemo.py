# -*- coding=utf8 -*-
#@author:qianli
# 文件说明：
import json
import requests

baseurl='https://api.weixin.qq.com/cgi-bin/token'
header = {'Accept-Encoding': 'gzip, deflate'}
params = {'grant_type':'client_credential','appid':'wx508a5cacbbfc1141','secret':'fa4fc7f17ddead12d7cdcd994e7d2543'}
response = requests.get(url=baseurl,headers=header,params=params)
print(response.text)


url = 'http://192.168.81.128/fsmarket/user.php'    #请求URL
header = {'Content-Type': 'application/x-www-form-urlencoded'} #请求头
param = ''  #请求参数query
data = 'username=qianli11&email=qianli11%40qq.com&password=123456&confirm_password=123456&extend_field5=13555556666&agreement=1&act=act_register&back_act=&Submit=%E5%90%8C%E6%84%8F%E5%8D%8F%E8%AE%AE%E5%B9%B6%E6%B3%A8%E5%86%8C'   #请求体
data = json.dumps({'a':'123'})
res = requests.post(url=url,headers=header,params=param,data=data)
print(res.text)


res = requests.request(method='post',url='/',headers=None,params={},data='')