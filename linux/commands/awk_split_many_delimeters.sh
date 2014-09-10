$ echo "a,b=c"  | awk -F '(,|=)' '{print $2}'
b
