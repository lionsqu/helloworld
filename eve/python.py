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

data =  """<goods></goods>
	"""

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
