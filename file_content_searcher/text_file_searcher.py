# -*- coding: UTF-8 -*-
import os
print "===Start of Program==="
file_path=u'D:\\交大10级图片\\10\\'
Search_Content=u'高鹏飞';
#list of extentions
proc_list=['txt','html','htm','c','cpp','h','hpp','java']
#get list of files in the dir:
dlist=os.listdir(file_path)
#print dlist
for fn in dlist:
	#search in the file
	ext=fn.split('.')
	ext=ext[len(ext)-1]
	if not (ext in proc_list):
		continue
	fullname=file_path+fn
	fp=open(fullname,'r')
	for lines in fp:
		text = unicode(lines, "gbk")  
		#print unicode(Search_Content)
		if text.find(Search_Content)!=-1:
			print 'Found in:'+fn
		

if "10211042.txt" in dlist :
	print "yes. there it is."
tmp=raw_input("\nEnd of Program...")
