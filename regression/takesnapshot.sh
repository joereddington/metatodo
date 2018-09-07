#!/bin/bash
SIZE=$(wc -l todo.txt)
TIME=$(git show -s --format="%ai")
ETIME=$(git show -s --format="%at")


git show -s
echo $TIME
echo $TIME, $ETIME, ${SIZE/ todo.txt/} >> log.csv
