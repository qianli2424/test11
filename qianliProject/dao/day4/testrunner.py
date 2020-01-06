# -*- coding=utf8 -*-
#@author:qianli  date：2020/1/6
# 文件说明：
import unittest
from qianliProject.dao.HTMLTestRunnerNew import HTMLTestRunner
from qianliProject.dao.day4 import SendTest

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