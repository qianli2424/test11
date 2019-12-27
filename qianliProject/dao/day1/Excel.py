# -*- coding=utf8 -*-
#@author:qianli
# 文件说明：
import openpyxl


class excel:
    def __init__(self,filename,sheetname):
        self.file = openpyxl.load_workbook(filename)
        self.sheet1 = self.file[sheetname]

    #获取最大行数
    def maxrow(self):
        maxrow = self.sheet1.max_row
        return maxrow

    #获取最大列数
    def maxcol(self):
        pass

    #获取单元格的值
    def getcell(self,row=1,col=1):
        pass