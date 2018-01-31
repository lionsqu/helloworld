folder=$(cd "$(dirname "$0")";pwd)
source $folder/head.cmd



python test.py create


result=$?
echo "result="$result
