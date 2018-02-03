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
from config import ConfigFile


def getsections():
	config = ConfigFile()

	config.open("dialog.ini")
	config.read()

	result = config.getsections()
	i = 0
	for section in result:
		#i = i + 1
		#print i,
		#print ("%s"%section),
		title = config.get(section, "title")
		print ("%s %s"%(section,title)),	



def preview(i):
	config = ConfigFile()

	config.open("dialog.ini")
	config.read()

	result = config.get(i, "code")
	print result,



if __name__ == '__main__':
	argc = len(sys.argv)
	if (argc == 2):
		if (sys.argv[1] == "getsections"):
			getsections()

	elif (argc == 3):
		if (sys.argv[1] == "preview"):
			preview(sys.argv[2])



