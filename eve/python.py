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
import ConfigParser


def config_read(section, name):
	config = ConfigParser.ConfigParser()
	config.readfp(open('config.ini'))
	value = config.get(section, name)
	return value	

def config_write(section, name, value):
	config = ConfigParser.ConfigParser()
	config.readfp(open('config.ini'))
	
	if (not config.has_section(section)):	
		config.add_section(section)
	config.set(section, name, value)
	config.write(open('config.ini', "w"))
	return	

if __name__ == '__main__':
	argc = len(sys.argv)
	if (argc == 1):
		if (__debug__ == True) :print "参数个数：1"
	elif (argc == 2):
		if (__debug__ == True) :print "参数个数：2"
	elif (argc == 4):
		if (__debug__ == True) :print "参数个数：4"
		if (sys.argv[1] == "config_read"):
			value = config_read(sys.argv[2], sys.argv[3])	
			print value	
	elif (argc == 5):
		if (sys.argv[1] == "config_write"):
			config_write(sys.argv[2], sys.argv[3], sys.argv[4])	
	else:
		if (__debug__ == True) :print "参数个数：3"


import commands
(status, output) = commands.getstatusoutput('$(dialog --title "hello" --msgbox 10 10 10)')	
print status, output


"""
import ConfigParser


config = ConfigParser.ConfigParser()


config.add_section("test")
config.set("test", "test", "hello")

config.write(open('config.ini', "w"))

config.readfp(open('config.ini'))

value = config.get("test", "test")

print value
"""







"""
import sys


print "脚本名称：", sys.argv[0]
print "参数个数：", len(sys.argv)
for i in range(1, len(sys.argv)):
	print "参数：", i , sys.argv[i]


from xml.sax import *


def xml_list(root):
        authors = []
        for authors in root.findall('./project'):
                data = {
                        "fnm": None,
                        "snm": None,
                        "email": Node,
                        "insr": []
                }
                data["fnm"] = author.findtext('./fnm')
                data["snm"] = author.findtext('./snm')
                data["email"] = author.findtext('./email')
                insr = author.findall('./insr')

                for i in insr:
                        data["insr"].append(i.attrib["iid"])
                        authors.append(data)
                return authors


xml_list


class MyHandler(ContentHandler):
	def startDocument(self):
		print "Start"

	def endDocument(self):
		print "End"

	
parser = make_parser()
parser.setContentHandler(MyHandler())

#data =  " " "<goods></goods>
#	" " "

import StringIO

parser.parse(StringIO.StringIO(data))


import xml.etree.ElementTree as ETree

def create_xml():
	root = ETree.Element("hello")
	root.set("version", "1.0")
	tree = ETree.ElementTree(root)
	tree.write("test.xml", encoding="UTF-8")
	return True

if __name__ == '__main__':
	create_xml()

"""
