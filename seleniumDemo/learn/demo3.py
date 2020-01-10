# -*- coding=utf8 -*-
#@author:qianli  date：2020/1/8
# 文件说明：
from selenium import webdriver
from selenium.webdriver.common.by import By

news = (By.XPATH,'//div[@id="u1"]/a[1]')

d = webdriver.Chrome()
d.get('https://www.baidu.com')
#d.find_element_by_xpath('//div[@id="u1"]/a[1]').click()
d.find_element(*news).click()
print(d.title)
d.quit()