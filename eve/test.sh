#dialog --title "Input your name:" --inputbox "Name:" 10 30 2>/tmp/name.test

dialog --title "" --form "hello" 15 45 5 "asjdf" 1 1 "afd" 1 15 15 0 2>/tmp/test.tmp

result=sudo cat /tmp/test.tmp

echo $result

