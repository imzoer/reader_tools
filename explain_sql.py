# -*- coding: utf-8 -*-
"""

脚本用于分析sql索引使用情况
cat wr.log|grep "sql:"|awk -F'sql:' '{print $2}'|sort|uniq -c|sort -k 1|grep -v ATTACH >sql.txt

"""
import shutil
import sys
import subprocess
import os

db_path="/Users/masonqwli/11049/WRReader"

f=open('sql.txt', 'r')
for line in f:
    line=line.strip()
    print "sql:",line
    times=line.split(" ")[0]
    sql=line.replace(times,"")
    cmd="sqlite3 "+db_path+" 'explain query plan "+sql+"'"
    print "sql execute times:",times
    os.system(cmd)
    print ""
f.close()
