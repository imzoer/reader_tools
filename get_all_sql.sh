cat wr.log|grep "sql:"|awk -F'sql:' '{print $2}'|grep -v ATTACH|sort|uniq -c|sort -k 1 > sql.txt
