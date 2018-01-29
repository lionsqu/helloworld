folder=$(cd "$(dirname "$0")";pwd)
source $folder/head.cmd


dialog --title "$(python test.py)" --yesno "this is a test" 10 20

result=$?
echo "result="$result
