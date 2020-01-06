# -*- coding=utf8 -*-
#@author:qianli  date：2020/1/6
# 文件说明：
# -*- coding=utf8 -*-
#@author:qianli  date：2020/1/6
# 文件说明：
import json
import re
import requests

def send(msgurl,body):
    baseurl='https://api.weixin.qq.com/cgi-bin/token'
    header = {'Accept-Encoding': 'gzip, deflate'}
    params = {'grant_type':'client_credential','appid':'wx508a5cacbbfc1141','secret':'fa4fc7f17ddead12d7cdcd994e7d2543'}
    response = requests.get(url=baseurl,headers=header,params=params)
    '''正则表达式提取器，提取的结果是一个list列表，取第0号元素'''
    token = re.findall('access_token":"(.+?)","expires_in',response.text)[0]

    param = {'access_token':token}
    response = requests.request(method='POST',url=msgurl,params=param,data=body)
    result = response.text

    return result

if __name__=='__main__':
    msgurl = 'https://api.weixin.qq.com/cgi-bin/message/custom/send'
    data = json.dumps({
        "touser": "omg-gs4FL7mlApVvbw2YPp5k8Tpc",
        "msgtype": "text",
        "text":
            {
                "content": "qianli - Hello World"
            }
    })
    response = send(msgurl=msgurl,body=data)
    print(response)