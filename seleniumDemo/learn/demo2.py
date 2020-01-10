# -*- coding=utf8 -*-
#@author:qianli  date：2020/1/8
# 文件说明：
from selenium import webdriver

d = webdriver.Chrome()
d.get('https://www.baidu.com')
eles = d.find_elements_by_class_name('mnav')
for ele in eles:
    ele.click()
    print(d.current_url)
    d.back()