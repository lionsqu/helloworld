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


def project_list():
	print "Memory Memory_Size 1 Disk Disk_Size 2 "

	return 0


#if __name__ == '__main__':
	argc = len(sys.argv)
	debug = False 
	if debug == True :print ("argc=%d"%argc) 
	if (argc == 2):
		if ( sys.argv[1] == "list" ):
			project_list()
	
 
