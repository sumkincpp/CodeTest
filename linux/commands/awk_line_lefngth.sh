# Show only lines with < 10 charachters
grep -r 'hehe' file.txt | awk 'length($0) < 10'
