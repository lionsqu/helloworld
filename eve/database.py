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
from sqlite import Sqlite



def database_create(database_name):
	sqlite = Sqlite()
	
	sqlite.open(database_name)
	sqlite.close()

	return 0

def database_open():
	
	return 0

def database_list():

	return 0

def database_remove():

	return 0


if __name__ == '__main__':
	argc = len(sys.argv)

	print("argc=%d"%argc)
	if(argc == 2):
		print

	elif (argc == 3):
		if(sys.argv[1] == "create"):
			print("database_create")
			database_create(sys.argv[2])




