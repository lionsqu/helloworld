#! /usr/bin/python
# coding:utf-8
#
# Github Tool Suite v0.1
# Copyright (c) 2018 Zhengfeng Qu (Lions) Suzhou,China.
# Email: lionsqu@yahoo.com
#
# This program is free software; you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the
# Free Software Foundation;
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the email: lionsqu@yahoo.com.
#



import sys
from head import Head
from config import ConfigFile


#Dialog操作类
class Dialog(object):
	#获得对话框类型列表
	def List(self):
		config = ConfigFile()
		config.open("dialog.ini")
		config.read()

		result = config.getsections()
		i = 0
		for section in result:
			title = config.get(section, "title")
			print ("%s %s"%(section,title)),	
			
		return 0		

	#对话框预览
	def Preview(self, i):
		config = ConfigFile()
		config.open("dialog.ini")
		config.read()
	
		result = config.get(i, "short")
		print result,




if __name__ == '__main__':
	argc = len(sys.argv)
	if (argc == 2):
		if (sys.argv[1] == "list"):
			dialog = Dialog()
			dialog.List()	

	elif (argc == 3):
		if (sys.argv[1] == "preview"):
			dialog = Dialog()
			dialog.Preview(sys.argv[2])



