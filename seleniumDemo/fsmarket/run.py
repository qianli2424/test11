# -*- coding=utf8 -*-
#@author:qianli  date：2020/1/9
# 文件说明：
import unittest
from seleniumDemo.fsmarket.common.HTMLTestRunnerNew import HTMLTestRunner
from seleniumDemo.fsmarket.testcase import TestLogin, TestUserInfo

suite = unittest.TestSuite()
loader = unittest.TestLoader()
suite.addTests(loader.loadTestsFromModule(TestLogin))
suite.addTests(loader.loadTestsFromModule(TestUserInfo))
with open('report.html','wb') as f:
    runner = HTMLTestRunner(
        stream=f,
        verbosity=2,
        title='客服发消息测试报告',
        description='客服发消息的详细测试结果',
        tester='千里'
    )
    runner.run(suite)