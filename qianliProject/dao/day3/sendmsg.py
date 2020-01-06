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
'''正则表达式提取器，提取的结果是一个list列表，取第0号元素'''
token = re.findall('access_token":"(.+?)","expires_in',response)[0]

msgurl = 'https://api.weixin.qq.com/cgi-bin/message/custom/send'
param = {'access_token':token}
body = json.dumps({
    "touser":"omg-gs4FL7mlApVvbw2YPp5k8Tpc",
    "msgtype":"text",
    "text":
    {
         "content":"qianli - Hello World"
    }
})
response = requests.request(method='POST',url=msgurl,params=param,data=body)
result = response.text
expected = '{"errcode":0,"errmsg":"ok"}'
'''对客服发消息的结果进行断言，增加了try except语法进行结果处理'''
try:
    assert result==expected
except Exception:
    print('-----------------测试失败-----------------')
    print('预期结果为：{},实际结果为：{}'.format(expected,result))
else:
    print('*****************测试成功*****************')