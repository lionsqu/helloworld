folder=$(cd "$(dirname "$0")";pwd)
#source $folder/head.cmd


function text() {
	return 1
}


function test() {
	#return 1
	#return
	echo 9
	text
}


test

result=$?

echo $result


