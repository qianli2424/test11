# -*- coding=utf8 -*-
#@author:qianli  date：2020/1/9
# 文件说明：
from time import sleep
from selenium import webdriver

d = webdriver.Chrome()
d.get('https://www.baidu.com')
d.find_element_by_css_selector('input[maxlength="255"]').send_keys('python')
sleep(3)