#
# piupiupiu links ->
#  -- http://www.math.utah.edu/docs/info/gawk_4.html Useful One Line Programs
#

# longest input line
awk '{ if (length($0) > max) max = length($0) } END { print max }' data 

# print lines with length > 80
awk 'length($0) > 80' data

# print lines where at least 1 field
awk 'NF > 0' data

# 7 rand numbers
awk 'BEGIN { for (i = 1; i <= 7; i++) print int(101 * rand()) }' 

# summing 5th column :)
ls -lg files | awk '{ x += $5 } ; END { print "total bytes: " x }'

# : separtor -- get users & sort
awk -F: '{ print $1 }' /etc/passwd | sort

# awk `wc -l` :)
awk 'END { print NR }' data
