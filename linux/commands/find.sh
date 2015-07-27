# compose flags with `-o`
find . -name '*.png' -o -name *.jpg

#greater than 1 day
fedor@as5930 ~/tmp $ find . -mtime +1

#less than 1 day
fedor@as5930 ~/tmp $ find . -mtime -1
