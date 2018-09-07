#!/bin/bash
cd "$(dirname "$0")"
git commit -a -m "Update before chart" 
rm log.csv
cp regression/takesnapshot.sh read.sh
chmod a+x read.sh
touch log.csv
git rebase  --exec ./read.sh --root --preserve-merges
mv log.csv charts/logsize.csv
cd charts
python plotPri.py  -f logsize.csv   -c -t 7 -o fear.png
cd ..
rm read.sh #cleaning up afteroutselves. 
git commit -a -m "Chart included" 
git push origin master

