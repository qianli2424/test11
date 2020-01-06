# -*- coding=utf8 -*-
#@author:qianli  date：2020/1/6
# 文件说明：
import json
import re
import requests


baseurl='https://api.weixin.qq.com/cgi-bin/token'
header = {'Accept-Encoding': 'gzip, deflate'}
params = {'grant_type':'client_credential','appid':'wx508a5cacbbfc1141','secret':'fa4fc7f17ddead12d7cdcd994e7d2543'}
response = requests.get(url=baseurl,headers=header,params=params)
print(response.text)
dict1 = response.json()
result = dict1['expires_in']
expected = 7201
try:
    assert result==expected
except Exception:
    print('-----------------测试失败-----------------')
    print('预期结果为：{},实际结果为：{}'.format(expected,result))
else:
    print('*****************测试成功*****************')

