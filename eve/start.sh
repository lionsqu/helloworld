#! /bin/sh
#
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


#debug
#sh python.cmd
#sh git.cmd
#sh github.cmd
#sh github.ui

source ./head.cmd

dialog --title "目录" --no-cancel --menu "请选择操作：" 12 35 5 \
1 "Github操作" 2 "Git操作" 3 "退出" 2>/tmp/start.sh.menu.tmp

result=$?
#debug
if [ test $debug ]; then echo "result="${result}; fi

#selected=$form_paras "/tmp/start.sh.menu.tmp" "1"
selected=form_paras '"/tmp/start.sh.menu.tmp"' '"1"'
#debug 
if [ test $debug ]; then  echo "selected="${selected}; fi

case $selected in
1)
	sh ./github.ui
	;;
2)
	sh ./git.ui
	;;
3)
	exit 0;
	;;
esac

