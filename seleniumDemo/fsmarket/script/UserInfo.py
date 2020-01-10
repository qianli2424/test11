# -*- coding=utf8 -*-
#@author:qianli  date：2020/1/9
# 文件说明：
from selenium.webdriver.common.by import By
from seleniumDemo.fsmarket.common.BasePage import BasePage

class UserInfo(BasePage):
    email_loc = (By.NAME,"email")
    username = (By.ID,'username')
    result = (By.ID,'result')
    def type_email(self,email):
        ele = self.find_element(*self.email_loc)
        ele.clear()
        ele.send_keys(email)
    def type_username(self,name):
        ele = self.find_element(*self.username)
        ele.clear()
        ele.send_keys(name)
    def result(self):
        result = self.find_element(*self.result)
        return result

def user_info(email,name):
    page = UserInfo()
    page.open('user.php?act=profile')
    page.type_email('laoluo@163.com')
    page.type_username('name')
    result = page.result
    return result
