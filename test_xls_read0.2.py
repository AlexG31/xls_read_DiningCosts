# -*- coding: utf-8 -*- 
import xlrd
def str2datenum(datestr):
	st=0
	while st<len(datestr):
		if(datestr[st]<'0' or datestr[st]>'9'):
			st=st+1
		else:
			break
	ans=0;
	while st<len(datestr) and datestr[st]!=' ':
		if datestr[st]!='-':
			ans*=10;
			ans+=int(datestr[st])-int('0')
		st=st+1

	return ans
print 'Program started.'
data = xlrd.open_workbook('log.xls')
table=data.sheets()[0]
val=table.col(4)[2]
print 'val=',val
#第四列：交易时间
date_str=table.cell_value(4,4)
print 'str val=',date_str
st_ind=str2datenum(date_str);
print 'st ind =',st_ind

cost=table.cell_value(4,5)
print 'cost today:',cost
cn=float(cost)
cn=cn+1
print 'cost +1 =',cn

print "----------------------Cost for days-----------------------------"
#list to remember date used
list_of_date=[]

print 'table . ncols=',table.ncols

print 'table . nrows=',table.nrows

tmp=table.cell_value(25,2)
print 'tmp=',tmp
print 'len=',len(tmp)

## 缴费记录不应该加入到花销中去
cs_recharge=[ur'领取圈存',ur'支付宝充值']
for i in range(1,table.nrows):
	date_str=table.cell_value(i,4)
	if(len(date_str)>0):
		#not considered before:
		date_num=str2datenum(date_str)
		if date_num in list_of_date:
			continue
		#new date:
		list_of_date.append(date_num)
		Cost=0
		## 假定它没有排过序，日期是乱的
		for j in range(1,table.nrows):
			t_date=table.cell_value(j,4)
			t_cost=table.cell_value(j,5)
			if len(t_date)>0 and len(t_cost)>0:
				t_datenum=str2datenum(t_date)
				if t_datenum==date_num and table.cell_value(j,2) not in cs_recharge:
					Cost+=float(t_cost)
		print 'Cost in',date_num,'is :',Cost

print '-------End of Program--------'
tmp=raw_input('waiting to exit....')
