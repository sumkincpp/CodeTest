sed -n '/blah/{n;p;}' logfile
awk '/blah/{getline; print}' logfile
