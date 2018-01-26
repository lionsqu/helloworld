git_cmd=$1
git_num=$#

#test
echo $git_cmd
echo $git_num

case $git_cmd in
"init")
	echo "init"
	git init
	case $git_num in
	1)
		echo "Git初始化当前目录\n"
		git init
		;;
	2)
		echo "Git初始化目录:"$2
		git init $2
		;;
	esac

	exit
	;;
"clone")
	git clone $2 $3
	exit
	;;	
"add")
	git add
	exit
	;;
"commit")
	git commit
	exit
	;;
"pull")
	git pull
	exit
	;;
"push")
	git push
	exit
	;;
"status")
	git status
	exit
	;;
"diff")
	git diff
	exit
	;;
"rm")
	git rm
	exit
	;;
"log")
	git log
	exit
	;;
*)
	echo "default"
	exit
	;;
esac

