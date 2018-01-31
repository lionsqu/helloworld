#! /bin/sh
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



suite_folder=$(cd "$(dirname "$0")";pwd)
source $suite_folder/head.cmd

result=$#
echo ${result}
case $result in
0)
	sh database.ui
	;;
1)
	;;
2)
	operate=$1
	#echo ${operate}
	case $operate in
	"create")
		python database.py "create" $2	
		;;
	"open")
		sh database.ui "open" $2
		;;
	"list")
		sh database.ui "list" $2
		;;
	"remove")
		python database.py "remove" $2
		;;
	esac
	;;
esac


