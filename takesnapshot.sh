#!/bin/bash
grep -v "^x" *.todo.txt > open.txt
SIZE=$(wc -l open.txt)
rm open.txt
TIME=$(git show -s --format="%ai")
ETIME=$(git show -s --format="%at")


git show -s
echo $TIME, $ETIME, ${SIZE/ open.txt/}
echo $TIME, $ETIME, ${SIZE/ open.txt/} >> log.csv
