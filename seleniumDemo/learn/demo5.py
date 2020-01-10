# -*- coding=utf8 -*-
#@author:qianli  date：2020/1/10
# 文件说明：
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('http://localhost/fsmarket/user.php')
info = driver.find_element(By.CSS_SELECTOR,'a.card_login').text
print(info)