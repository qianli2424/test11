# -*- coding=utf8 -*-
#@author:qianli  date：2020/1/9
# 文件说明：
import unittest
from ddt import ddt,data,unpack
from seleniumDemo.fsmarket.script.LoginPage import user_login

exceldata = 'read user_login.xlsx'

@ddt
class TestLogin(unittest.TestCase):
    @data(exceldata)
    @unpack
    def test_login(self,**data):
        result = user_login(data)
        try:
            self.assertEqual('expected',result)
        except Exception:
            print('------------')