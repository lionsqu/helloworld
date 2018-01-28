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
#debug
#echo $suite_folder
source $suite_folder/head.cmd


git_cmd=$1
git_num=$#

case $git_cmd in
#repository
"init")
	case $git_num in
	1)
		git init .
		;;
	2)
		git init $2
		;;	
	*)
		exit 255
		;;
	esac
	;;
"clone")
	case $git_num in
	1)
		git clone $2
		;;
	2)
		git clone $2 $3
		;;
	3)
		git clone $3 $4 
		;;
	*)
		echo $git_num
		exit 255
		;;
	esac
	;;
"remove")
        case $git_num in
        1)
                ;;
        2)
		#git rm $2
		rm -rf $2
                ;;
        *)
                exit 255
                ;;
        esac
	;;
"push")
        case $git_num in
        1)
		git push
                ;;
        2)
                ;;
        *)
                exit 255
                ;;
        esac
	;;
"pull")
        case $git_num in
        1)
		git pull
                ;;
        2)
                ;;
        *)
                exit 255
                ;;
        esac
	;;
#branch
"branch")
	;;
"commit")
        case $git_num in
        1)
                ;;
        2)
		git commit $2 $3 
                ;;
	3)
		git commit $2 $3 $4
		;;
        *)
                exit 255
                ;;
        esac
	;;
#code
"add")
        case $git_num in
        1)
                ;;
        2)
                git add $2 
                ;;
        3)
                ;;
        *)
                exit 255
                ;;
        esac
	;;
"mv")
	;;
"rm")
	;;
"reset")
	;;
"log")
        case $git_num in
        1)
		git log
                ;;
        2)
                ;;
        *)
                exit 255
                ;;
        esac
	;;
"status")
        case $git_num in
        1)
		git status
                ;;
        2)
                ;;
        *)
                exit 255
                ;;
        esac
	;;

*)
	exit 255
	;;
esac






#debug
#git_check_version(){
#	echo "git_check_version"
#	if [ version_gt $ver1 $ver2 ]; then
#		echo $ver1 $ver2
#	fi 
#	if [ version_le $ver1 $ver2 ]; then
#		echo $ver1 $ver2
#	fi 
#	if [ version_lt $ver1 $ver2 ]; then
#		echo $ver1 $ver2
#	fi 
#	if [ version_ge $ver1 $ver2 ]; then
#		echo $ver1 $ver2
#	fi 
#}
#
#
#
#git_cmd=$1
#git_num=$#
#
#test
#echo $git_cmd
#echo $git_num
#git_check_version
#
#
#case $git_cmd in
#"init")
#	echo "init"
#	git init
#	case $git_num in
#	1)
#		echo "Git初始化当前目录\n"
#		git init
#		;;
#	2)
#		echo "Git初始化目录:"$2
#		git init $2
#		;;
#	esac
#
#	exit
#	;;
#"clone")
#	git clone $2 $3
#	exit
#	;;	
#"add")
#	git add $2 $3
#	exit
#	;;
#"commit")
#	git commit $2 $3
#	exit
#	;;
#"pull")
#	git pull
#	exit
#	;;
#"push")
#	git push
#	exit
#	;;
#"status")
#	git status
#	exit
#	;;
#"diff")
#	git diff
#	exit
#	;;
#"rm")
#	git rm
#	exit
#	;;
#"log")
#	git log
#	exit
#	;;
#"config")
#	case $2 in
#	"--global")
#		case $3 in
#		"user.name")
#			git config --global user.name $4
#			exit
#			;;
#		"user.email")
#			git config --global user.email $4
#			;;
#		esac
#		;;
#	esac
#	exit
#	;;
#*)
#	echo "default"
#	exit
#	;;
#esac
#
