folder=$(cd "$(dirname "$0")";pwd)
source $folder/head.cmd


result=$?
echo "result="$result



function dialog_calendar() {
        echo 'dialog --title "title" --backtitle "backtitle" --calendar "date" 1 1'  
        return
}


$(dialog_calendar)
dialog_calendar > code.txt






