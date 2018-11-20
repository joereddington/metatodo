cd ../todo.txt/
cat todo.txt  | grep -v "x (" | head -n 1 | sed 's/.* (/ (/g'

