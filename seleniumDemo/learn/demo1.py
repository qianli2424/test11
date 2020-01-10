# -*- coding=utf8 -*-
#@author:qianli  date：2020/1/8
# 文件说明：
from selenium import webdriver

#启动一个浏览器，也就是生成一个浏览器对象，要指明启动chrome浏览器
driver = webdriver.Chrome()
driver.get('http://www.baidu.com')
names = ['tj_trnews','tj_trhao123','tj_trmap','tj_trvideo','tj_trtieba','tj_trxueshu']
'''通过name属性查找到这个元素，把这个元素保存为ele_news'''
for name in names:
    driver.find_element_by_name(name).click()    #对这个元素进行点击操作
    print(driver.current_url)   #输出当前的url值
    driver.back()
driver.quit()   #退出整个浏览器
driver.close()  #关掉当前页面