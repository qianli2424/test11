# -*- coding=utf8 -*-
#@author:qianli  date：2020/1/9
# 文件说明：
import re

from selenium.webdriver.common.by import By
from seleniumDemo.fsmarket.common.BasePage import BasePage
'''该功能有几个输入框就定义几个方法外加获取实际结果的方法'''
class LoginPage(BasePage):
    '''元素的定位方式和属性值'''
    username = (By.ID, 'username')
    password = (By.ID, 'password')
    submit_botton = (By.NAME, 'submit')

    '''输入用户名，密码和点击登录按钮'''
    def type_username(self, username):
        self.find_element(*self.username).send_keys(username)

    def type_password(self, password):
        self.find_element(*self.password).send_keys(password)

    def select_cars(self,index=0,value=None,visibleText=None):
        if index!=0:
            pass
        elif value!=None:
            pass
        elif visibleText!=None:
            pass
        else:
            pass

    def submit(self):
        self.find_element(*self.submit_botton).click()

    def result(self):
        result = self.find_element(*self.username).text
        res = re.findall('abc(.*?)ab',result)[0]
        return res

'''用户登录的操作过程，使用方法描述整个过程'''
def user_login(url,username,password):
    page = LoginPage('http://192.168.154.129/fsmarket/')
    page.open(url)
    page.type_username(username)
    page.type_password(password)
    page.scroll(100)
    page.submit()
    result = page.result()
    return result