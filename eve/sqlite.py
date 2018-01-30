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



import sqlite3


class Sqlite(object):
	def __init(self):
		print 

	def open(self, filename):
		self.conn = sqlite3.connect(filename)	
		self.cursor = self.conn.cursor()	
	
	def close(self):
		if hasattr(self, "conn") and self.conn:
			self.conn.close()	

	def execute(self, sql = None):
		print sql
		self.cursor.execute(sql)
		self.conn.commit()
	
	pass


