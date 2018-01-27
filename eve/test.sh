folder=$(cd "$(dirname "$0")";pwd)
echo $folder

source $folder/head.cmd

#ls -d * >/tmp/dir.tmp


folder1=$(getfirstsubfolder)
echo ${folder1}


test=$(ls -d *)
echo ${test}


ls -d */>/tmp/dir.tmp
folder=$(sudo sed -n '1p' /tmp/dir.tmp)
echo ${folder}
