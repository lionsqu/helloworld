function form_paras() {
	local result;
	
	$result=$(sudo sed -n '$2p' $1);
	
	#debug
	#if [ test $debug ]; then echo "result="$result fi

	echo $result;	
}

function version_gt() { 
	test "$(echo "$@" | tr " " "\n" | sort -V | head -n 1)" != "$1"; 
}
function version_le() { 
	test "$(echo "$@" | tr " " "\n" | sort -V | head -n 1)" == "$1"; 
}
function version_lt() { 
	test "$(echo "$@" | tr " " "\n" | sort -rV | head -n 1)" != "$1"; 
}
function version_ge() { 
	test "$(echo "$@" | tr " " "\n" | sort -rV | head -n 1)" == "$1"; 
}

function terminal_lines() {
	tput lines
}
function terminal_cols() {
	tput cols
}

