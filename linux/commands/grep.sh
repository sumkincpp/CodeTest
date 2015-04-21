# grepping without filename (flag -h)
grep -h blabla .

# print only match
grep -o 'bla' .
grep -o '{.*}' .

# -ignore case or -i
grep -io 'bla' .

# -I  - skip binaries, 
# --exclude-dir="\.svn"
grep -r --include=\*.{cpp,h} --exlclude="" piuu .

# inverted match
grep -v doc .

# match aaa and bbb
grep 'aaa\|bbb' .

# extended regexp
grep -E 'pattern1|pattern2' filename

# grep only whole line containing `meooow`
grep -w ^meooow file.txt

# unbuffered grep by line
tail -f file | grep --line-buffered my_pattern
