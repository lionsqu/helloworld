folder=$(cd "$(dirname "$0")";pwd)
source $folder/head.cmd


dialog --title "test" --cancel-label "cancel" --extra-button --help-button --exit-label "exit" --extra-label "extra" --help-label "help" --ok-label "ok"  --checklist "test" 20 50 10 \
Memory Memory_Size 1 Disk Disk_Size 2	 

result=$?
echo "result="$result
