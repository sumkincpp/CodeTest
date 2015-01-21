$ echo " test test test  " | sed -re 's/(^ *| *$)//'
test test test  

# Sed lines from 10 to 20
sed -n '10,20' 192.168.100.6_full.snmmpwalk

# Sed to end of file
sed -n '100,$p' 192.168.100.6_full.snmmpwalk

# replace foo to bar in file, not single quotes - dat's for MAC OS(bsd?)
sed -i '' -e 's/foo/bar/' target.file

#sed and print next 10-th line
sed -n '/hehee/{10n;p;}' target.file
