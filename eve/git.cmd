source ./head.cmd

git_check_version(){
	echo "git_check_version"
	if [ version_gt $ver1 $ver2 ]; then
		echo $ver1 $ver2
	fi 
	if [ version_le $ver1 $ver2 ]; then
		echo $ver1 $ver2
	fi 
	if [ version_lt $ver1 $ver2 ]; then
		echo $ver1 $ver2
	fi 
	if [ version_ge $ver1 $ver2 ]; then
		echo $ver1 $ver2
	fi 
}



git_cmd=$1
git_num=$#

#test
echo $git_cmd
echo $git_num
git_check_version


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
	git add $2 $3
	exit
	;;
"commit")
	git commit $2 $3
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
"config")
	case $2 in
	"--global")
		case $3 in
		"user.name")
			git config --global user.name $4
			exit
			;;
		"user.email")
			git config --global user.email $4
			;;
		esac
		;;
	esac
	exit
	;;
*)
	echo "default"
	exit
	;;
esac

