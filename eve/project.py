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



import sys, os
from head import Head
from sqlite import Sqlite


#项目管理器操作类
class Project(object):
	#类初始化方法
	def __init__(self):
		print

	#建立项目
	def Create(self, project_name):
		print
        	sqlite = Sqlite()

        	print ("project_name=%s"%(project_name))

        	sqlite.open("project.db")

        	sqlite.execute("create table if not exists projects(id integer primary key autoincrement, project_name varchar(128))")

        	sqlite.execute("insert into projects(project_name)values('%s')"%(project_name))

        	sqlite.close()

        	result = True
        	if(result == True):
                	path=os.getcwd()
                	os.makedirs("%s/%s/../projects/%s"%(path, Head.FolderPrefix, project_name))

        	return 0


	
	#删除项目
	def Remove(self, name):
		print

	#获得项目列表
	def List(self):
		#print "Memory Memory_Size 1 Disk Disk_Size 2 "

		sqlite = Sqlite()
		sqlite.open("project.db")	

		result = sqlite.execute("select * from projects")
		i = 0
		for record in result:
			for field in record:
				print field,
			i = i + 1
			print i,
		#print ("\\")

		sqlite.close()

		return 0

	pass


if __name__ == '__main__':
       	argc = len(sys.argv)
       	debug = False 
       	if debug == True :print ("argc=%d"%argc) 
       	if (argc == 2):
               	if ( sys.argv[1] == "list" ):
			project = Project()
			project.List()       
       	elif (argc == 3):
               	if ( sys.argv[1] == "create" ):
                      	#print "project_create"
			project = Project()
			project.Create(sys.argv[2])

