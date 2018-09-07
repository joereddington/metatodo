#!/bin/bash
SIZE=$(wc -l todo.txt)
TIME=$(git show -s --format="%ci")
ETIME=$(git show -s --format="%at")

echo $TIME, $ETIME, ${SIZE/ todo.txt/} >> log.csv
