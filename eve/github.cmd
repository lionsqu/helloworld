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


github_base="https://github.com/"

#repository
function github_repository_clone() {
	local access_url=${github_base}$1/$2.git
	
	#debug
	echo ${access_url} 
	
	#${suite_folder}/git.cmd clone ${access_url} $2
	${suite_folder}/git.cmd clone ${access_url} 
	return
}

github_cmd=$1
github_num=$#

case $github_cmd in
#repository
"init")
	case $github_num in
	1)
		#git init .
		;;
	2)
		#git init $2
		;;	
	*)
		exit 255
		;;
	esac
	;;
"clone")
	case $github_num in
	1)
		;;
	2)
		#git clone $2
		;;
	3)
		github_repository_clone $2 $3
		;;
	*)
		exit 255
		;;
	esac
	;;
"remove")
        case $github_num in
        1)
                ;;
        2)
		#git rm $2
		#rm -rf $2
                ;;
        *)
                exit 255
                ;;
        esac
	;;
"push")
        case $github_num in
        1)
		#git push
                ;;
        2)
                ;;
        *)
                exit 255
                ;;
        esac
	;;
"pull")
        case $github_num in
        1)
		#git pull
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
        case $github_num in
        1)
                ;;
        2)
		#git commit $2 $3 
                ;;
	3)
		#git commit $2 $3 $4
		;;
        *)
                exit 255
                ;;
        esac
	;;
#code
"add")
	;;
"mv")
	;;
"rm")
	;;
"reset")
	;;
"log")
        case $github_num in
        1)
		#git log
                ;;
        2)
                ;;
        *)
                exit 255
                ;;
        esac
	;;
"status")
        case $github_num in
        1)
		#git status
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

