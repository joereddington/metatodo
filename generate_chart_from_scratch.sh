#!/bin/bash
cd "$(dirname "$0")"
git clone https://github.com/joereddington/todo.txt/ temp
cd temp
git rebase  --exec ../takesnapshot.sh --root --preserve-merges
mv log.csv ../log.csv
cd ../
python plotPri.py  -f log.csv   -c -t 7 -o fear.png
rm -Rf temp/
git commit -a -m "update chart" 
git push origin master
