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



import ConfigParser


class ConfigFile:
	def open(self, filename):
		self.config = ConfigParser.ConfigParser()
		self.filename = filename
		print 

	def close(self):
		self.config.close()
		print

	def read(self):
		self.config.read(self.filename)
		print

	def write(self):
		file = open(self.filename, "w")
		self.config.write(file)
		file.close()	
		print

	def getsections(self):
		result = self.config.sections()
		return result

	def getitems(self, section):
		result = self.config.items(section)
		return result

	def get(self, section, item):
		result = self.config.get(section, item)
		return result
		
	def set(self, section, item, value):
		self.config.set(section, item, value)
		print


