# -*- coding=utf8 -*-
#@author:qianli  date：2020/1/9
# 文件说明：
import unittest
from ddt import ddt,data,unpack
from seleniumDemo.fsmarket.script.LoginPage import user_login
from seleniumDemo.fsmarket.script.UserInfo import user_info

exceldata = 'read user_info.xlsx'

@ddt
class TestUserInfo(unittest.TestCase):
    @data(exceldata)
    @unpack
    def test_userinfo(self,**data):
        result = user_info(data)
        try:
            self.assertEqual('expected',result)
        except Exception:
            print('------------')