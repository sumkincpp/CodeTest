# uniq by column
# http://stackoverflow.com/questions/1915636/is-there-a-way-to-uniq-by-column


awk -F"," '!_[$1]++' file

# -t\| - separator
# -k by column 1 & 3
sort -u -t\| -k 1,1 -k 3,3 test.txt
