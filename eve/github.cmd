github_cmd=$1
github_num=$#

#test
echo $github_cmd
echo $github_num

case $git_cmd in
"clone")
	sh git.cmd clone 
	;;
esac
