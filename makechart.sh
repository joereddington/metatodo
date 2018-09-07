#!/bin/bash
cp regression/takesnapshot.sh read.sh
touch log.csv
git rebase  --exec read.sh 0fd691acb0b44d9621bbdf75779790ca14d86ef0

