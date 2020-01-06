# -*- coding=utf8 -*-
#@author:qianli  date：2020/1/6
# 文件说明：
import json
import unittest
from qianliProject.dao.HTMLTestRunnerNew import HTMLTestRunner
from qianliProject.dao.day4.sendmsg import send

class SendTest(unittest.TestCase):
    def test_sendmsg_success(self):
        body = json.dumps({
            "touser": "omg-gs4FL7mlApVvbw2YPp5k8Tpc",
            "msgtype": "text",
            "text":
                {
                    "content": "qianli - Hello World"
                }
        })
        data = {'msgurl': 'https://api.weixin.qq.com/cgi-bin/message/custom/send', 'body': body}
        expected = '{"errcode":0,"errmsg":"ok"}'
        result = send(**data)
        #result = send(msgurl='',body='')
        try:
            self.assertEqual(expected,result)
        except Exception:
            print('----------测试失败---------')
            print('预期结果为：{}，实际结果为：{}'.format(expected,result))
        else:
            print('*********测试通过**********')
    def test_sendmsg_fail(self):
        body = json.dumps({
            "touser": "omg-gs4FL7mlApVvbw2YPp5k8",
            "msgtype": "text",
            "text":
                {
                    "content": "qianli - Hello World"
                }
        })
        data = {'msgurl': 'https://api.weixin.qq.com/cgi-bin/message/custom/send', 'body': body}
        expected = '{"errcode":40003,"errmsg":"invalid openid hint"}'
        result = send(**data)
        # result = send(msgurl='',body='')
        try:
            self.assertEqual(result,expected)
        except Exception:
            print('----------测试失败---------')
            print('预期结果为：{}，实际结果为：{}'.format(expected, result))
        else:
            print('*********测试通过**********')

if __name__=='__main__':
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    suite.addTests(loader.loadTestsFromModule(SendTest))
    with open('report.html','wb') as f:
        runner = HTMLTestRunner(
            stream=f,
            verbosity=2,
            title='客服发消息测试报告',
            description='客服发消息的详细测试结果',
            tester='千里'
        )
        runner.run(suite)