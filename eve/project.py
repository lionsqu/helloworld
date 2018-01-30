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
from sqlite import Sqlite


def project_list():
	print "Memory Memory_Size 1 Disk Disk_Size 2 "

	sqlite = Sqlite()
	sqlite.open("project.db")	

	sqlite.execute("select * from projects")

	sqlite.close()

	return 0


def project_create(project_name):
	sqlite = Sqlite()

	sqlite.open("project.db")

	sqlite.execute("create table if not exists projects(id integer primary key autoincrement, project_name varchar(128))")

	sqlite.execute("insert into projects(project_name)values(%s)"%(project_name))

	sqlite.close()

	return 0


if __name__ == '__main__':
	argc = len(sys.argv)
	debug = False 
	if debug == True :print ("argc=%d"%argc) 
	if (argc == 2):
		if ( sys.argv[1] == "list" ):
			project_list()
	
	elif (argc == 3):
		if ( sys.argv[1] == "create" ):
			project_create(sys.argv[2]) 
