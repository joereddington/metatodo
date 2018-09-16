#!/bin/bash
cd "$(dirname "$0")"
git clone https://github.com/joereddington/todo.txt/ temp
cd temp
cp ../takesnapshot.sh read.sh
chmod a+x read.sh
touch log.csv
git rebase  --exec ./read.sh --root --preserve-merges
mv log.csv ../charts/logsize.csv
cd ../charts
python plotPri.py  -f logsize.csv   -c -t 7 -o fear.png
cd ..
rm -Rf temp/
