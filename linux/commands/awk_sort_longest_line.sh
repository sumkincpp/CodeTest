cat file | awk '{ print length($0) " " $0; }' $file | sort -r -n | cut -d ' ' -f 2-
