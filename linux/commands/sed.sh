$ echo " test test test  " | sed -re 's/(^ *| *$)//'
test test test  

# Sed lines from 10 to 20
sed -n '10,20' 192.168.100.6_full.snmmpwalk

# Sed to end of file
sed -n '100,$p' 192.168.100.6_full.snmmpwalk
