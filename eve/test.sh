folder=$(cd "$(dirname "$0")";pwd)
echo $folder

source $folder/head.cmd

source $folder/python.cmd

value=$(setting_read "config" "total")
echo ${value}

