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
from head import Head


#Sqlite3数据库操作类
class Sqlite(object):
	#类初始化方法
	def __init(self):
		print 

	#打开数据库
	def open(self, filename):
		self.conn = sqlite3.connect(filename)	
		self.cursor = self.conn.cursor()	
	
	#关闭数据库
	def close(self):
		if hasattr(self, "conn") and self.conn:
			self.conn.close()	

	#数据库查询，返回数据集
	def execute(self, sql = None):
		#print sql
		result = self.cursor.execute(sql)
		return result
	
	#数据库查询，返回执行状态
	def execute(self, sql = None):
		result = self.cursor.execute(sql)
		self.conn.commit()
		return result
	
	#提交更新
	def commit(self):
		if hasattr(self, "conn") and self.conn:
			self.conn.commit()

	pass


