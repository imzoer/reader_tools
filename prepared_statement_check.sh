adb pull /sdcard/perf .
cat 145*.txt|grep statementPtr|awk -F":" '{print $2}'|sort|uniq -c|sort -rk 1 > PreparedStatement.txt
cat PreparedStatement.txt|grep -E "= \d{3,}"
