# -*- coding=utf8 -*-
#@author:qianli  date：2020/1/2
# 文件说明：

class excel:
    def __init__(self,filename,sheetname):
        self.filename = filename
        self.sheet = sheetname

    def dictrow(self,row=2,start=2,end=7):
        row = {}
        for i in range(start,end+1):
            key = self.sheet.cell(row=1,column=i).value
            value = self.sheet.cell(row=row,column=i).value
            row[key]=value  #把数据追加到字典中
        return row
    def dictall(self,start,end):
        maxrow = self.sheet.max_row
        data = []
        for rownum in range(2,maxrow+1):
            rowvalue = self.dictrow(row=rownum,start=start,end=end)
            data.append(rowvalue)
        return data