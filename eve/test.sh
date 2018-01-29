folder=$(cd "$(dirname "$0")";pwd)
source $folder/head.cmd


dialog --title "test" --checklist "test" 20 50 10 \
$(python test.py) \
2>/tmp/test.tmp

result=$?
echo "result="$result
