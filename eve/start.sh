sh python.cmd
sh git.cmd
sh github.cmd


#sh github.ui

dialog --title "目录" --menu "请选择操作：" 12 35 5 \
1 "Github操作" 2 "Git操作" 3 "退出"

result=$?
echo $result
if [ $? -eq 1 ]; then
sh github.ui;
elif [ $result -eq 2 ]; then
sh git.ui;
fi
exit 0
