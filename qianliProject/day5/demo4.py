# -*- coding=utf8 -*-
#@author:qianli
# 文件说明：
import openpyxl

user = ['admin','123456','unlock',2]
file = openpyxl.load_workbook('linux.xlsx')
sheet = file['Sheet1']
maxrow = sheet.max_row


for i in range(len(user)):
    sheet.cell(maxrow+1,i+1).value = user[i]