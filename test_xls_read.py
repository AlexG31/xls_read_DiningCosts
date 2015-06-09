# -*- coding: utf-8 -*- 
import xlrd
print 'Program started.'
data = xlrd.open_workbook('log.xls')
table=data.sheets()[0]
val=table.col(4)[2]
print 'val=',val
date_str=table.cell_value(0,4)
print 'str val=',date_str


