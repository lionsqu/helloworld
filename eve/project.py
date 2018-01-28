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
	#print "'project_list'"

	print "dialog --backtitle \"\" " #--no-cancel \\"
	print "--checklist \"hello\" 20 50 10 "
	print "Memory Memory_Size 1 Disk Disk_Size 2 "
	print "2>/tmp/project.ui.menu.tmp"	

	return 0


if __name__ == '__main__':
	argc = len(sys.argv)
	#print ("'argc=%d'"%(argc))
	if (argc == 1):
		print ""
	elif (argc == 3):
		if(sys.argv[1] == "list"):
			#print "'list'"
			project_list()
	else:
		print ""

	
 
