# -*- coding=utf8 -*-
#@author:qianli  date：2020/1/9
# 文件说明：
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


class BasePage:
    '''基础类，用于页面对象类的继承'''
    base_url = 'http://192.168.154.129/fsmarket/'
    users = ('qianli','123456')

    '''定义生成浏览器对象'''
    def __init__(self, base_url=base_url):
        self.base_url = base_url
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        '''登录操作'''
        username = (By.ID, 'username')
        password = (By.ID, 'password')
        submit_botton = (By.NAME, 'submit')
        self.find_element(*username).send_keys(self.users[0])
        self.find_element(*password).send_keys(self.users[1])
        js = "document.documentElement.scrollTop=100"
        self.driver.execute_script(js)
        self.find_element(*self.submit_botton).click()

    '''定义操作结束后等待2秒后退出浏览器'''
    def __del__(self):
        sleep(2)
        self.driver.quit()

    '''定义打开页面的方式'''
    def open(self, url=None):
        current_url = self.base_url + url
        self.driver.implicitly_wait(10)
        self.driver.get(current_url)  # 进入到被测页面
        '''增加断言，如果打开的页面不正确，直接报错不再继续执行'''
        assert self.driver.current_url == current_url, '打开页面 %s 失败' % url

    '''重新定义定位元素的方式，使用可变参数，用户输入定位方式和元素位置'''
    def find_element(self, *loc):
        return self.driver.find_element(*loc)

    '''定位滚动条'''
    def scroll(self, point):
        js = "document.documentElement.scrollTop=" + str(point)
        self.driver.execute_script(js)