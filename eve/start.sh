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


dialog --title "目录" \
--backtitle "Github工具箱 v0.1 Copyright (c) 2018 Zhengfeng Qu (Lions) \
Suzhou,China." \
--no-cancel --menu "请选择操作：" 15 50 8 \
1 "Github操作" 2 "Git操作" 3 "退出" \
2>/tmp/start.sh.menu.tmp

result=$?
#debug
if [ test $debug ]; then echo "result="${result}; fi

selected=$(sudo sed -n '1p' /tmp/start.sh.menu.tmp)
#debug 
if [ test $debug ]; then  echo "selected="${selected}; fi

case $selected in
1)
	sh $suite_folder/github.ui
	;;
2)
	sh $suite_folder/git.ui
	;;
3)
	exit 0;
	;;
esac

